from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('SJSoAEGKK4nj58UHAluyb6y18wAdeOUn/F163A1BEHGjI7BLUaFz/2rnRhskf2k9w/7XzOpwsCnZTcztjxjOEv/c2J0GuUd0RPcyQIfNLMzPt6WWxJ5XnMoYp4uBCsNJ7iG95AIAursQ/5xbpyq7aQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('1a3c17ab604b6365246d4d6fe5f4c7e8')

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
    return 'OK'

what_can_i_do="我目前只有2個按鈕\n然後我可以學你說話\n你也可以試試輸入\n@風景圖"



# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text=="@自我介紹":
        message = TextSendMessage(text="哈摟我叫yichengBOT\n建於2020/7/7\n沒啥功能")
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="@你會幹嘛?":
        message = TextSendMessage(text=what_can_i_do)
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text=="@風景圖":
        message = ImageSendMessage(
            original_content_url='https://images4.alphacoders.com/774/77454.jpg',
            preview_image_url='https://media.sproutsocial.com/uploads/2017/02/10x-featured-social-media-image-size.png')
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text=event.message.text)
        line_bot_api.reply_message(event.reply_token, message)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
