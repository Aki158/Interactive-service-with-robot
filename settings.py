import os
import logging
from dotenv import load_dotenv


# 環境変数の読み込み
load_dotenv()

WEB_HOOK_URL = os.getenv('WEB_HOOK_URL')
TMDB_API_KEY = os.getenv('TMDB_API_KEY')
LOG_FILE_PASS = os.getenv('LOG_FILE_PASS')

# ログの設定
logging.basicConfig(filename=LOG_FILE_PASS, level=logging.INFO, 
                    format='%(asctime)s %(levelname)s: %(message)s')