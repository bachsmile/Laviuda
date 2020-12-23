import requests
import json
from airtest.core.api import *
HTTP_PROXY = "http://172.28.103.34:3128"
HTTPS_PROXY = "https://172.28.103.34:3128"
#-----------Link-----------------------------#
# from test.Autotest.Lavuavi.Function.Cheat.Cheat.api import *
#--------------------------------------------#
# Lấy access token mới mỗi lần dùng tool cheat
ACCESS_TOKEN = "ya29.a0AfH6SMCnBwnSAFh_JwFbHzxBIOPDRo1NrKhLCbNw7Ow26t9EII2tstz1PpbOS5azx1imHlays4YIo7rauGqLNewn9jTv0oyZjIgQnRm7yzowxofGipMvarsWJjr7797vk9ooJEzC19IDAAXGRuobx09InHDYu674C1CjpBgpXh2e"
SERVER_HOST = "http://49.213.81.43:10021"
BASE_URL = SERVER_HOST + "/api/"

proxyDict = {
    "http": HTTP_PROXY,
    "https": HTTPS_PROXY,
    "ftp": ""
}

header = {
    "content-type": "application/json",
    "sessionKey": ACCESS_TOKEN
}

def api_postDoFunction(userId, id, params):
    """"
        Send post function to admin tool back end
    """
    url = BASE_URL + "doFunction"
    
    data = {
        "gameId": "laviuda",
        "mode": "PRIVATE",
        "userId": userId,
        "id": id,
        "params": params
    }
    print("--------------API--------%s-------%s-----%s" % (id,params,url))
    r = requests.post(url, data=json.dumps(data), headers=header, timeout=1000)
    res = json.loads(r.text)
    print(res)
    return r.status_code

def api_get():
    """"
        Send get to admin tool back end
    """
    url = BASE_URL + "profile/getUserInfo"

    params = {
        "gameId": "laviuda",
        "mode": "private"
    }

    r = requests.get(url, headers=header, params=params)
    res = json.loads(r.text)
    print("--------------API---------------%s" % res)
    return r.status_code

def api_changeTimeServer(timeInMilliseconds):
    """"
        Send cheat time server
    """
    url = BASE_URL + "webmin/cheatTime"

    data = {
        "gameId": "laviuda",
        "mode": "PRIVATE",
        "time": timeInMilliseconds
    }
    print("--------------URL---------------%s" % url)
    r = requests.post(url, data=json.dumps(data), headers=header)
    return r.status_code

#Cheat gold
def cheatGold(idU,gold):
    try:
        cheat = api_postDoFunction(idU, "ADD_GOLD", [gold])
        print(cheat)
        print("cheat gold success")
        return True
    except:
        print("Error cheat gold")
        return False
def cheatBuyDeal(idU,deal):
    try:
        if deal == 1:
            cheat = api_postDoFunction(idU, "CHEAT_BUY_EVENT_TACOS_DEAL", ["megaDeal"])
        if deal == 2:
            cheat = api_postDoFunction(idU, "CHEAT_BUY_EVENT_TACOS_DEAL", ["superDeal"])
        if deal == 3:
            cheat = api_postDoFunction(idU, "CHEAT_BUY_EVENT_TACOS_DEAL", ["thirdDeal"])
        else:
            return False
        print(cheat)
        print("cheat deal success")
        return True
    except:
        print("Error cheat deal")
        return False
# a = api_postDoFunction("19130214", "CHEAT_NUM_OBTAIN_MISSION", [1])
# a = api_postDoFunction("19130214", "CHEAT_PAYMENT_VIP", ["vip.pack_1"])
#megaDeal, superDeal,thirdDeal
# a = api_postDoFunction("19008332", "CHEAT_BUY_EVENT_TACOS_DEAL", ["megaDeal"])


# a = api_postDoFunction("19130214", "ADD_GOLD", [1000000])
# a = api_changeTimeServer(1606350600000)
# # assert_equal(a, 200, "Cheat OK")
# if a==200:
#     print('ok')
# a = api_postDoFunction("19130214", "CHEAT_NUM_OBTAIN_MISSION", [2])
# print(a)
#############################
#time:
#24/11/2020 6:00:00  -> 1606172400000
#26/11/2020 06:59:00 -> 1606348740000
#26/11/2020 06:59:20 -> 1606348760000
#26/11/2020 07:30:00 -> 1606350600000
#27/11/2020 11:11:11 -> 1606450271000
#27/11/2020 23:59:00 -> 1606496340000
#28/11/2020 23:59:00 -> 1606582740000
