from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import InvalidSignatureError

from linebot.models import *

from web_spider import WeatherGet,MemeSend

from flask import current_app as app1


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

what_can_i_do="我目前只有3個按鈕\n而且我可以學你說話\n你也可以試試問我問題"



# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input=event.message.text

    if input=="@自我介紹":
        reply_text = "哈摟我叫yichengBOT\n建於2020/7/7\n沒啥功能"
    elif input=="@你會幹嘛?":
        reply_text = what_can_i_do
    elif input=="@meme":
        reply_picture = ImageSendMessage(original_content_url=MemeSend(),preview_image_url=MemeSend())
        line_bot_api.reply_message(event.reply_token, reply_picture)
    elif input=="@新北市天氣":
        reply_text=WeatherGet('新北市')
    else:
        reply_text = input

    message = TextSendMessage(text=reply_text)
    line_bot_api.reply_message(event.reply_token, message)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
