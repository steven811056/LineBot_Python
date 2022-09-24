import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Au1ZzxYHxeXYP2V3Rm0lB8p6h7o5RT+iPsRKZ422xNplakOR8QUou0Il8adSyqE3eDg2rZigZLPvuKsP71vqkHIJ18/V6SZqnvIHZsKtJd5fUQZngUexrJtIyuIuJva9B5LQGJoUfAiACGWObYMrDAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('bbd528808689c34db9f3513076ae57e7')

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        message)

    # line_bot_api.push_message(
    #     '1657249626',
    #     TextSendMessage(text='你可以開始了'))

if __name__ == "__main__":
    app.run()
# if __name__ == "__main__":
# 　　port = int(os.environ.get('PORT', 5000))
# 　　app.run(host='0.0.0.0', port=port)


