from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import InvalidSignatureError

from linebot.models import *

from weather import WeatherGet

from Getmeme import MemeSend

from flask import current_app as app1

import twd

import luis
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
    app1.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

what_can_i_do="我目前只有3個按鈕\n你可以問我天氣或是匯率\n找梗圖輸入@meme"



# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input=event.message.text

    if input=="@自我介紹":
        reply_text = "哈摟我叫yichengBOT\n建於2020/7/7\n沒啥功能\n可以一直刷梗圖給你"
    elif input=="@你會幹嘛":
        reply_text = what_can_i_do
    elif input=="@meme":
        meme_jpg=MemeSend()
        reply_picture = ImageSendMessage(original_content_url=meme_jpg,preview_image_url=meme_jpg)
        line_bot_api.reply_message(event.reply_token, reply_picture)
    else:
        luis.get_report(input)
        if luis.user_mind=="weather":
            reply_text=WeatherGet(luis.get_report(input))

    message = TextSendMessage(text=reply_text)
    line_bot_api.reply_message(event.reply_token, message)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
