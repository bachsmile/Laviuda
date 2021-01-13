# -*- encoding=utf8 -*-
__author__ = "pc"
import time
from datetime import datetime
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.cocosjs import CocosJsPoco
import json
poco = CocosJsPoco()
#config
#id
# user["user0"]["user"]
user={
    "user0":{
        "id":"19400486",
        "user":"user000",
        "pass":123456      
    },
    "user1":{
        "id":"19400458",
        "user":"user001",
        "pass":123456      
    },
    "user2":{
        "id":'19400724',
        "user":"user002",
        "pass":123456       
    },
    "user3":{
        "id":'19400738',
        "user":"user003",
        "pass":123456       
    },
}
timeW="""
00:00:00
02/12/2020
"""
timeWC={
    "start":{"Y":2020,"M":12,"D":29,"h":7,"m":0,"s":0},
    "end":{"Y":2021,"M":1,"D":5,"h":7,"m":0,"s":0}
}
def datetoMili(day):
    return day*86400000
def housToMili(hous):
    return hous*3600000
def minutetoMili(minute):
    return minute*60000
def secToMili(sec):
    return sec*1000
def convertDayTimeToMili(time):
    dt = datetime(time['Y'],time['M'],time['D'],time['h'],time['m'],time['s'])
    milliseconds = int(round(dt.timestamp() * 1000))
    print(milliseconds)
    return milliseconds
# print(convertDayTimeToMili(timeWC["start"]))
<<<<<<< HEAD
def convertSecondstoDateTime(milliseconds):
    seconds=milliseconds/1000
    timestamp = datetime.fromtimestamp(seconds)
    return timestamp
=======
# def convertSecondstoDateTime(milliseconds)
#     seconds=milliseconds/1000
#     timestamp = datetime.fromtimestamp(seconds)
#     return timestamp
>>>>>>> bbaaf1c3cb853cc4b2a14bf09074e5dc3e1d8663
# print(convertSecondstoDateTime)
#Feature
#chalenge
challenge={
    "day1":{
        "mission":"exchange1",
    },
    "day2":{
        "mission":"knock",
        },
    "day3":{
        "mission":"win",
        },
    "day4":{
        "mission":"collect",
    },
     "day5":{
         "mission":"win",       
    },
     "day6":{
         "mission":"final",    
    },
     "day7":{
        "mission":"claim",
    }
}
challengePlay={
    "win":{
        "data":{
                "detailMission":poco(text="Ganar "),
                "totalX":3,
                "tacos":4,
                "gold":80000
                },
    },
    "final":{
        "data":{
            "detailMission":poco(text="Jugar "),
            "totalX":4,
            "tacos":3,
            "gold":120000
        }    
    },
    "knock":{
        "data":{
                "detailMission":poco(text="Tocar "),
                "totalX":4,
                "tacos":3,
                "gold":40000
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
            "tacos":2,
            "gold":20000
        },
    },
    "claim":{
        "data":{
            "gold":120000
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
#deal
dealWCConfig={
    "offerWC1":{
        "gold":16000000
    },
    "offerWC2":{
        "gold":60000000
    },
    "offerWC1":{
        "gold":150000000
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
      "Reload": "Fail",
      "GuiEvent": "Fail",
      "GuiEDeal": "Fail",
      "CheatFOM": "Fail",
      "Bot": "Fail",
      "Knock": "Fail",
      "Exchange1":"Fail",
      "BtnBuyWC":"Fail",
      "GoldUpdate":"Fail",
      "BtnDeal":"Fail"
    }
# convertDayTimeToMili(2020, 11, 26,6,59,0)   
# print(challengePlay[challenge["day2"]["mission"]]["data"]["gold"])
# Daily bonus ------------------------------------------------------
DailyBonus={
    "day1":{
            "bonus":20000 
    },
    "day2":{
            "bonus":50000
    },
    "day3":{
            "bonus":80000
    },
    "day4":{
            "bonus":150000
    },
    "day5":{
            "bonus":160000
    },
    "day6":{
            "bonus":250000
    },
    "day7":{
            "bonus":400000
    },    
}
# x=DailyBonus["day3"]["bonus"]
#---------------------------------------cofig feature Vip---------------------------------------------------#
vip_pack = {
    "vip.pack_1" : {
        "id": 1,
        "price":50,
        "bonus": 0.3,
        "dailyTribute":5,
        "day":3
    },
    "vip.pack_2" : {
        "id": 2,
        "point":100,
        "bonus":0.5,
        "dailyTribute":6,
        "day":7
    },
    "vip.pack_3" : {
        "id": 3,
        "point":300,
        "bonus":1,
        "dailyTribute":7,
        "day":30
    }
}

pack_gold = {
    "credit_card" : {
            "id": 1,
            "10MXN":1000000,
            "15MXN":1500000,
            "30MXN":3500000,
            "40MXN":5000000
    },
    "gg_play" : {
            "id": 2,
            "20MXN":2000000,
            "50MXN":6500000,
            "100MXN":15000000,
            "200MXN":30000000,
            "400MXN":60000000
    } 
}
account = {
    "user0":{
        "id":"19202812",
        "user":"vyhn0907",
        "pass":123456      
    },
    "user1":{
        "id":"19175089",
        "user":"nguyenvy123",
        "pass":123456      
    }
}
gold_support = 30000
# convertDayTimeToMili(2020, 11, 26,6,59,0)   
# print(challengePlay[challenge["day2"]["mission"]]["data"]["gold"])
#----------------------------------------------------WC----------------------------------------------------------------------#







