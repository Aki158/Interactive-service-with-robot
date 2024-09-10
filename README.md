# Interactive-service-with-robot

## 概要

おすすめの映画を紹介するBOCCO emo

## 開発素材

<table>
<tr>
  <th>カテゴリ</th>
  <th>使用技術</th>
</tr>
<tr>
  <td>開発言語</td>
  <td>Python3</td>
</tr>
<tr>
  <td>インフラ</td>
  <td>ngrok</td>
</tr>
<tr>
  <td>ガジェット</td>
  <td>BOCCO emo</td>
</tr>
<tr>
  <td rowspan=2>API</td>
  <td>BOCCO emo Platform API</td>
</tr>
<tr>
  <td>TMDB</td>
</tr>
</table>

## システム構成

BOCCO emoが「おすすめの映画を教えて」と話しかけると、[BOCCO emo Platform API](https://platform-api.bocco.me/api-docs/#overview)を経由し、Webサーバーに通知されます。

Webサーバーは、TMDB APIを利用し、映画情報を取得します。

その後、映画情報をBOCCO emoに発話させます。

![image](https://github.com/user-attachments/assets/842a46e9-b288-4ffb-9e65-2595d2dc3540)

## セットアップ手順

ターミナル上で以下コマンドを実施することによりローカル環境で動作確認ができます。

1. リポジトリをクローンする
```
git clone https://github.com/Aki158/Interactive-service-with-robot.git
```

2. クローンしたリポジトリへ移動する
```
cd Interactive-service-with-robot
```

3. ngrokを起動する

```
ngrok http 8000
```

ngrokをインストールしていない場合は、[こちら](https://dashboard.ngrok.com/get-started/setup/macos)からインストールしてください

3. 環境ファイルを作成する

```
touch .env
```

4. 環境ファイルに下記をコピーして値を設定する

```
EMO_PLATFORM_API_ACCESS_TOKEN="***"
EMO_PLATFORM_API_REFRESH_TOKEN="***"
WEB_HOOK_URL="***"
TMDB_API_KEY="***"
LOG_FILE_PASS="***"
```

環境変数について

| 環境変数名 | 概要 |
| ------- | ------- |
| `EMO_PLATFORM_API_ACCESS_TOKEN` | [ダッシュボード](https://platform-api.bocco.me/dashboard/login)にログインすると表示されるアクセストークンをコピーしてください |
| `EMO_PLATFORM_API_REFRESH_TOKEN` | [ダッシュボード](https://platform-api.bocco.me/dashboard/login)にログインすると表示されるリフレッシュトークンをコピーしてください |
| `WEB_HOOK_URL` | ngrokを実行後に表示されるURLをコピーしてください<br>(例. https://***.ngrok-free.app) |
| `TMDB_API_KEY` | 映画情報を取得できるAPIです。<br>[こちら](https://weblion303.net/1262)を参考にAPIキーを取得してからコピーしてください。 |
| `LOG_FILE_PASS` | Webサーバーの情報をログとして出力するファイルのパスです。<br>設定する場合は、`app.log`のように記載してください。 |

5. Webサーバーを起動する
```python3
python3 main.py
```

## 使用方法

1. BOCCO emo の録音ボタンを押した後に「おすすめの映画を教えて」と話しかける
2. BOCCO emo から「おすすめの映画は、〜」と紹介されることを確認する

## アピールポイント

### リアルタイムな映画紹介機能

ユーザーが声でリクエストするとBOCCO emoがすぐに映画を紹介してくれます。

シンプルな機能なため、子供から大人まで誰でも使いやすいです。

### キーワードを認識した場合のみ反応

Webサーバーは、BOCCO emoからの入力情報をもとに処理します。

キーワード(おすすめの映画を教えて)がメッセージに含まれている場合のみ、TMDB APIに映画情報を取得するようにリクエストします。

TMDB APIから映画情報を取得できなかった場合は、`ごめんね、今日はおすすめの映画を見つけられなかったよ。また後で探してみるから、楽しみにしててね！`というメッセージを返します。

### ログ出力

Webサーバーへのリクエストやレスポンスの情報は、ログファイルに出力されます。

正常にリクエストが取得できなかった場合に原因を調査しやすくしています。
