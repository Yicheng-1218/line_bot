import requests

user_intent=""
user_entities=[]
headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'e7909763174540cd8adbc95dc2d7f3a9',
}

params ={
    # Query parameter
    'q': '我要一份大亨堡',
    # Optional request parameters, set to default values
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'true',
}
def luis_read(user_input):
    try:
        query = user_input
        params['q']=query
        r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/445b8090-2457-4d6a-b2d5-7f88b85b5806',headers=headers, params=params)
        # 顯示結果
        ret=r.json()
        user_intent=ret['topScoringIntent']
        for entity in ret['entities'] :
            user_entities.append(entity)
    except Exception as e:
        print(e)

