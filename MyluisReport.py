import requests
from bs4 import BeautifulSoup

app_id='445b8090-2457-4d6a-b2d5-7f88b85b5806'
subscription_key='e7909763174540cd8adbc95dc2d7f3a9'
api_link='https://westus.api.cognitive.microsoft.com/luis/prediction/v3.0/apps/%s/slots/staging/predict?subscription-key=%s&verbose=true&show-all-intents=true&log=true&query='%(app_id,subscription_key)

def luisMain(user_input):
    res=requests.get(api_link+user_input)
    ret=res.json()
    print(ret['topIntent'])

luisMain('明天台北天氣')
