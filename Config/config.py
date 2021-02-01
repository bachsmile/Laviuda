# -*- encoding=utf8 -*-
__author__ = "pc"
import time
from datetime import datetime
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.cocosjs import CocosJsPoco
import json
poco = CocosJsPoco()
#----------------------------------------------------WC----------------------------------------------------------------------#
#config
#doi ngay qua miliseconds
def datetoMili(day):
    return day*86400000
#doi gio qua miliseconds
def housToMili(hous):
    return hous*3600000
#doi phu qua miliseconds
def minutetoMili(minute):
    return minute*60000
#doi giay qua miliseconds
def secToMili(sec):
    return sec*1000
#doi daytime qua miliseconds
def convertDayTimeToMili(time):
    dt = datetime(time['Y'],time['M'],time['D'],time['h'],time['m'],time['s'])
    milliseconds = int(round(dt.timestamp() * 1000))
    print(milliseconds)
    return milliseconds
#doi miliseconds sang daytime
def convertSecondstoDateTime(milliseconds):
    seconds=milliseconds/1000
    timestamp = datetime.fromtimestamp(seconds)
    return timestamp
#Time Start end End WC
timeWC={
    "start":{"Y":2020,"M":12,"D":29,"h":7,"m":0,"s":0},
    "end":{"Y":2021,"M":1,"D":5,"h":7,"m":0,"s":0}
}
#Account
user["user0"]["user"]
user={
    "user0":{
        "id":"20609637",
        "user":"zps100",
        "pass":123456      
    },
    "user1":{
        "id":"20609650",
        "user":"zps101",
        "pass":123456      
    },
    "user2":{
        "id":'20609682',
        "user":"zps102",
        "pass":123456       
    },
    "user3":{
        "id":'20609702',
        "user":"zps103",
        "pass":123456       
    },
     "user":{
        "id":'20538919',
        "user":"zpstest",
        "pass":123456       
    },
}
# user={
#     "user0":{
#         "id":"20536072",
#         "user":"zps000",
#         "pass":123456      
#     },
#     "user1":{
#         "id":"20536032",
#         "user":"zps001",
#         "pass":123456      
#     },
#     "user2":{
#         "id":'20536048',
#         "user":"zps002",
#         "pass":123456       
#     },
#     "user3":{
#         "id":'20536060',
#         "user":"zps003",
#         "pass":123456       
#     },
#      "user":{
#         "id":'20538919',
#         "user":"zpstest",
#         "pass":123456       
#     },
# }

#Feature
#Config nhiem vu thuc hien trong cac ngay
challenge={
    "day1":{
        "mission":"exchange1",
    },
    "day2":{
        "mission":"knock",
        },
    "day3":{
        "mission":"collect", #wc
        },
    "day4":{
        "mission":"win",
    },
     "day5":{
         "mission":"full",       
    },
     "day6":{
         "mission":"play",    
    },
     "day7":{
        "mission":"claim",
    }
}
# configCase["beforEvent"]["account"]
# configCase["beforEvent"]["day"]
# "day"+str(configCase["claimGift"]["day"])
#config cac account su dung trong cac case test
configCase={
    "beforEvent":{
        "day":0,
        "account":"user0"
    },
     "afterEvent":{
        "day":0,
        "account":"user1"
    },
     "day1":{
        "day":1,
        "account":"user1"
    },
     "claimGift":{
        "day":1,
        "account":"user1"
    },
     "day2":{
        "day":2,
        "account":"user1"
    },
     "noClaimGift":{
        "day":2,
        "account":"user1"
    },
     "CheckChangeAcc":{
        "day":2,
        "account":"user2"
    },
     "missionPassDayInTable":{
        "day":2,
        "account":"user2"
    },
     "autoClaimGift":{
        "day":2,
        "account":"user2"
    },
    
     "day3":{
        "day":3,
        "account":"user2"
    },
    
     "missionPassDayOpenGui":{
        "day":3,
        "account":"user2"
    },
    
     "passClaimGift":{
        "day":2,
        "account":"user1"
    },
    
     "day4":{
        "day":4,
        "account":"user1"
    },
    
     "UpdateProgressMissionFull":{
        "day":4,
        "account":"user1"
    },
     "GuiDeal":{
        "day":4,
        "account":"user1"
    },
     "day7":{
        "day":7,
        "account":"user1",
        "account2":"user3"
    },
     "endEvent":{
        "day":8,
        "account":"user2"
    },
    
}

# print("day"+str(configCase["autoClaimGift"]["day"]))
# print(configCase["passClaimGift"]["day"])
#config infor cac nhiem vu
challengePlay={
    "win":{
        "data":{
                "detailMission":poco(text="Ganar "),
                "totalX":3,
                "tacos":3,
                "gold":100000,
                "type":"win"
                },
    },
    "full":{
        "data":{
            "detailMission":poco(text="Termina el juego con "),
            "totalX":4,
            "tacos":3,
            "gold":150000
        }    
    },
    "knock":{
        "data":{
                "detailMission":poco(text="Tocar "),
                "totalX":4,
                "tacos":3,
                "gold":50000
                },
    },
    "exchange1":{
         "data":{
            "detailMission": poco(text="Cambiar una por una "),
            "totalX":25,
            "tacos":2,
            "gold":30000
           },
    },
    "collect":{
        "data":{
            "detailMission": poco(text="Coleccionar "),
            "totalX":4, 
            "tacos":4,
            "gold":80000,
            "type":"wc"
        },
    },
    "claim":{
        "data":{
            "gold":15000
        } 
    },
    "play":{
        "data":{
            "detailMission": poco(text="Jugar "),
            "totalX":20, 
            "tacos":6,
            "gold":200000
        },
    }
}
#cac bo bai can cheat vaf wildcard can cheat
cardCheat={
    "wc":{
        "card":"2c",
        "set":"ab,2b,3b,4b,5b"
    },
    "win":{
        "card":"2c",
        "set":"2t,2b,2r,ab,ac"
    },
    "lose":{
        "card":"2c",
        "set":"3t,2b,7r,9b,qc"
    },
    "full":{
        "card":"2c",
        "set":"3t,3b,3r,ab,ac"
    },
}
#deal config
dealWCConfig={
    "offerWC1":{
        "gold":16000000,
        "gold1":6500000
    },
    "offerWC2":{
        "gold":60000000,
        "gold1":15000000
    },
    "offerWC3":{
        "gold":150000000,
        "gold1":30000000
    },
}
#dataReport
dataReportConfig = {
      "Tab": "Fail",
        "Mission": "Fail",
        "CheatGold0": "Fail",
        "OpenGUI": "Fail",
        "CheatGold1": "Fail",
        "Button": "Fail",
        "BtnPlay0": "Fail",
        "BtnPlay": "Fail",
        "BtnPlay1": "Fail",
        "JoinTable":"Fail",
        "Progess": "Fail",
        "CheatFOM": "Fail",
        "Update": "Fail",
        "Update1": "Fail",
        "NoUpdate":"Fail",
        "ChooseLeave":"Fail",
        "Leave": "Fail",
        "CheatTime": "Fail",
        "TimeCheat": "Fail",
        "CheatTime1": "Fail",
        "TimeCheat1": "Fail",
        "Reload": "Fail",
        "GuiEvent": "Fail",
        "GuiEDeal": "Fail",
        "CheatFM": "Fail",
        "Bot": "Fail",
        "Knock": "Fail",
        "Exchange1":"Fail",
        "BtnBuyWC":"Fail",
        "GoldUpdate":"Fail",
        "BtnDeal":"Fail",
        "Login":"Fail",
        "UpdateTocos":"Fail",
        "MissionDay1":"Fail",
        "MissionNew":"Fail",
        "Effect":"Fail",
        "Tick":"Fail",
        "UpdateFull": "Fail",
        "UpdateAgain": "Fail",
        "ShowProg": "Fail",
        "Coutdown":"Fail",
        "After":"Fail",
        "Befor":"Fail",
        "ShowBtnJoin":"Fail",
        "noPlay":"Fail",
        "onPlay":"Fail",
        "HideProgress":"Fail"
    }
# convertDayTimeToMili(2020, 11, 26,6,59,0)   
# print(challengePlay[challenge["day2"]["mission"]]["data"]["gold"])
# Daily bonus ------------------------------------------------------
DailyBonus={"day1":20000, "day2":50000, "day3":80000, "day4":150000, "day5": 160000,
            "day6":250000, "day7":400000}
userID=''
#x=DailyBonus["day6"]
# x=DailyBonus["day3"]["bonus"]
#---------------------------------------cofig feature Vip---------------------------------------------------#
vip_pack = {
    "vip.pack_1" : {
        "id": 1,
        "price":50,
        "bonus": 0.3,
        "dailyTribute":5000000,
        "day":3
    },
    "vip.pack_2" : {
        "id": 2,
        "point":100,
        "bonus":0.5,
        "dailyTribute":6000000,
        "day":7
    },
    "vip.pack_3" : {
        "id": 3,
        "point":300,
        "bonus":1,
        "dailyTribute":7000000,
        "day":30
    }
}

pack_gold = {
    "gg_play" : {
            "iap.pack_1":2000000,
            "iap.pack_2":6500000,
            "iap.pack_3":15000000,
            "iap.pack_4":30000000,
            "iap.pack_5":60000000
    } 
}
account = {
    "user0":{
        "id":"19202812",
        "user":"vyhn0907",
        "pass":123456      
    },
    "user1":{
        "id":"20040460",
        "user":"vyhn0908",
        "pass":123456      
    }
}
gold_support = 30000


