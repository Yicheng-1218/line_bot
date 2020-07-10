import twder


def get_exchange_rate(city):
    if city[0]=="台幣":
        return "你要換算啥...?"
    currencies={"美元":"USD","美金":"USD","美國":"USD",
                "港幣":"HKD","香港":"HKD",
                "英鎊":"GBP","英國":"GBP",
                "澳幣":"AUD","澳洲":"AUD",
                "加拿大幣":"CAD","加幣":"CAD","加拿大":"CAD",
                "新加坡幣":"SGD","新加坡":"SGD",
                "瑞士法郎":"CHF","瑞士":"CHF",
                "日幣":"JPY","日圓":"JPY","日本":"JPY",
                "南非幣":"ZAR","南非":"ZAR",
                "瑞典幣":"SEK","瑞典":"SEK",
                "紐幣":"NZD","紐西蘭幣":"NZD","紐西蘭":"NZD",
                "泰幣":"THB","泰銖":"THB","泰國":"THB",
                "菲律賓幣":"PHP","菲律賓":"PHP",
                "印尼盾":"IDR","印尼幣":"IDR","印尼":"IDR",
                "歐元":"EUR","歐洲":"EUR",
                "韓元":"KRW","韓國":"KRW",
                "越南幣":"VND","越南":"VND",
                "馬來幣":"MYR","馬來西亞":"MYR",
                "人民幣":"CNY","中國":"CNY","肺炎國":"CNY",
                "台幣":"twd"}    
    keys=currencies.keys()
    tlist=['現金買入','現金賣出','即期買入','即期賣出']
    currency=city[0]
    show=currency+"匯率:\n"
    if currency in keys:
        if len(city)==3:
            citys_coin=[]
            for i in range(2):
                citys_coin.append(currencies[city[i]])
            return countingRate(citys_coin,city[2])
        for i in range(4):
            exchange=float(twder.now(currencies[currency])[i+1])
            show=show+tlist[i]+":"+str(exchange)+"\n"
        return show
    else:
        return "無此貨幣資料"

def countingRate(citys_info,number):
    result=''
    if citys_info[0]=="twd":
        result=number/float(twder.now(citys_info[1])[2])
        return '%.2f'%result
    else:
        result=number*float(twder.now(citys_info[0])[3])
        return '%.2f'%result

