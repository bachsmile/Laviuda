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
     "user":{
        "id":'19130219',
        "user":"user",
        "pass":123456       
    },
}

timeWC={
    "start":{"Y":2020,"M":12,"D":29,"h":7,"m":0,"s":0},
    "end":{"Y":2020,"M":1,"D":5,"h":7,"m":0,"s":0}
}
# def timeBtnCheat(time,Y,M,D,h,m,s):
#     TY=0+Y
#     TM=0+M
#     TD=0+D
#     Th=0+h
#     Tm=0+m
#     Ts=0+s
#     timeW="""
# {0}:{1}:{2}
# {3}/{4}/{5}
# """
#     timeWt=timeW.format(time['h']+Th, time['m']+Tm,time['s']+Ts,time['D']+TD,time['M']+TM,time['Y']+TY)
#     return timeWt
# print(timeBtnCheat(timeWC[ "start"],1,-11,-28,0,0,0))
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
def convertSecondstoDateTime(milliseconds):
    seconds=milliseconds/1000
    timestamp = datetime.fromtimestamp(seconds)
    return timestamp
# def convertSecondstoDateTime(milliseconds)
#     seconds=milliseconds/1000
#     timestamp = datetime.fromtimestamp(seconds)
#     return timestamp
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
        "mission":"collect", #wc
        },
    "day4":{
        "mission":"win",
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
                "totalX":4,
                "tacos":4,
                "gold":80000,
                "type":"win"
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
        "set":"3t,42b,7r,9b,10c"
    },
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
        "onPlay":"Fail"
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







