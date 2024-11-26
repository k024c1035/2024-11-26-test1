from flask import Flask, request

app = Flask(__name__)

# サーバールートへアクセスがあった時
@app.route('/')
def index():
    # フォームを表示する
    return """
        <html><body>
        <form action="/hello" method="GET">
          名前: <input type="text" name="name"><br>
          ひとこと: <input type="text" name="comment"><br>
          <input type="submit" value="送信">
        </form>
        </body></html>
    """

# /hello へアクセスがあった時
@app.route('/hello')
def hello():
    # nameとcommentのパラメータを取得
    name = request.args.get('name')
    comment = request.args.get('comment')

    # デフォルト値を設定
    if name is None or name.strip() == '':
        name = '名無し'
    if comment is None or comment.strip() == '':
        comment = 'コメント無し'

    # レスポンスを生成
    return """
    <html>
        <body>
            <h1>{0}さん、こんにちは！</h1>
            <p>ひとこと：{1}</p>
        </body>
    </html>
    """.format(name, comment)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
