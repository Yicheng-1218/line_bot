import requests
import weather

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'e7909763174540cd8adbc95dc2d7f3a9',
}

user_mind=''
params ={
    # Query parameter
    'q': '我要一份大亨堡',
    # Optional request parameters, set to default values
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'true',
}
def get_report(user_input):
    global user_mind
    try:
        query = user_input
        params['q']=query
        r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/445b8090-2457-4d6a-b2d5-7f88b85b5806',headers=headers, params=params)
        # 顯示結果
        ret=r.json()
        #print(ret['topScoringIntent'])
        #for entity in ret['entities'] :
            #print(entity)
    except Exception as e:
        print(e)
    if ret['topScoringIntent']['intent']=='詢問天氣':
        user_mind='weather'
        for en in ret['entities']:
            if en['type']=='地點':
                city=en["entity"]
                return city
                break
    if ret['topScoringIntent']['intent']=='詢問天氣':
        user_mind='criticize'
        
