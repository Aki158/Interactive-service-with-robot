import random
import requests
import logging

import settings


def get_recommended_movie():
    URL = "https://api.themoviedb.org/3/movie/popular"    
    PAGE = random.randint(1, 10)
    PARAMS = {
        'api_key': settings.TMDB_API_KEY,
        'page': PAGE,
        'language': 'ja-JP'
    }
    HEADER = {
        "method": "get",
        "accept": "application/json"
    }
    NOT_FOUND_MOVIE_INFO = "ごめんね、今日はおすすめの映画を見つけられなかったよ。また後で探してみるから、楽しみにしててね！"

    try:
        response = requests.get(URL, params=PARAMS, headers=HEADER)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Failed to get movie data: {e}")
        return NOT_FOUND_MOVIE_INFO

    json_data = response.json()
    filtered_movies = []
    ALLOW_ORIGINAL_LANGUAGES = ['ja', 'en']

    for movie in json_data['results']:
        if movie['original_language'] in ALLOW_ORIGINAL_LANGUAGES:
            movie_title = movie.get('title')

            if movie_title:
                filtered_movies.append(movie_title)

    if filtered_movies:
        return f"おすすめの映画は、{random.choice(filtered_movies)}だよ！気になったら、調べてみてね！"
    else:
        return NOT_FOUND_MOVIE_INFO
