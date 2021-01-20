import requests
import json
from airtest.core.api import *
HTTP_PROXY = "http://172.28.103.34:3128"
HTTPS_PROXY = "https://172.28.103.34:3128"
#-----------Link-----------------------------#
# from test.Autotest.Lavuavi.Function.Cheat.Cheat.api import *
#--------------------------------------------#
# Lấy access token mới mỗi lần dùng tool cheat
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjBjNTU0NWMzLTUxNDItNGMyNi1iODZkLTA3YzUxM2ZmODg4NiIsIm5hbWUiOiJCw6FjaC4gVHLhuqduIFh1w6JuIiwiZW1haWwiOiJiYWNodHhAdm5nLmNvbS52biIsIm9pZCI6IjE5ZDMyODgxLTY4ZmItNGMzMS04NzVkLWE0ZmQwMzEzN2FjMyIsImFkZHJlc3MiOiIxLjUzLjI1NS4xNDUiLCJleHBpcmVkIjoxNjExMTk0MjI5NTA1LCJ0eXBlIjoiYXp1cmUiLCJ1c2VybmFtZSI6ImJhY2h0eEB2bmcuY29tLnZuIiwiaWF0IjoxNjExMTA2NTUzLCJleHAiOjE2MTExOTI5NTN9.wjmm4J2nNRHRH59G27NFbtwUXGAO8_UXEvozDqSbD1w"
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
        "mode": "PRIVATE_2",
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
        "mode": "PRIVATE_2",
        "time": timeInMilliseconds
    }
    print("--------------URL---------------%s" % url)
    r = requests.post(url, data=json.dumps(data), headers=header)
    return r.status_code
# api_changeTimeServer(1609199400000)
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
def cheatBuyGold(idU, pack):
    try:
        cheat = api_postDoFunction(idU, "CHEAT_PAYMENT_IAP", [pack])
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
def cheatFinishedMision(idU,day):
    try:
        cheat = api_postDoFunction(idU, "CHEAT_FINISH_MISSION_TACOS_BUS", [day])
        print(cheat)
        print("cheat finished mission success")
        return True
    except:
        print("Error finished mission")
        return False
def getGold(userId):
    try:
        """"
            Send post module to admin tool back end
        """
        url = BASE_URL + "player/getModel"

        data = {
            "gameId": "laviuda",
            "mode": "PRIVATE_2",
            "userId": userId,
            "modelName":"UProfileModel"
        }
        print("--------------API-------------%s" % (url))
        r = requests.post(url, data=json.dumps(data), headers=header, timeout=1000)
        res = json.loads(r.text)['modelData']
        gold=json.loads(res)['gold']
        print(gold)
        return gold
    except json.decoder.JSONDecodeError:
        print('Failed JSON')
def getModel(userId,modelName):
    try:
        """"
            Send post module to admin tool back end
        """
        url = BASE_URL + "player/getModel"

        data = {
            "gameId": "laviuda",
            "mode": "PRIVATE_2",
            "userId": userId,
            "modelName":"event."+modelName
        }
        print("--------------API-------------%s" % (url))
        r = requests.post(url, data=json.dumps(data), headers=header, timeout=1000)
        res = json.loads(r.text)
        print(res)
        return res
    except json.decoder.JSONDecodeError:
        print('Failed JSON')
# getModel(19130219,"UEventTacosBusModel")
# getGold(19130219)
