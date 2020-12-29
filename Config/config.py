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
        "id":"19203300",
        "user":"bachtx0",
        "pass":123456      
    },
    "user1":{
        "id":"19130214",
        "user":"bachtx1",
        "pass":123456      
    },
    "user2":{
        "id":19130219,
        "user":"bachtx2",
        "pass":123456       
    },
    "user3":{
        "id":123,
        "user":"bachtx3",
        "pass":123456       
    }
}

#time Cheat
#time:
timeC={
    #24/11/2020 6:00:00  -> 1606172400000
    "timeD0":{
        "mili":1606172400000,
        "data":"24/11/2020 6:00:00"
    },
    #26/11/2020 06:59:00 -> 1606348740000
    "timeD01":{
        "mili":1606348740000,
        "data":"26/11/2020 06:59:00"
    },
    #26/11/2020 06:59:40 -> 1606347600000
    "timeD02":{
        "mili":1606348780000,
        "data":"26/11/2020 06:59:40"
    },
    #26/11/2020 07:30:00 -> 1606350600000
    "timeD1":{
        "mili":1606350600000,
        "data":"26/11/2020 07:30:00"
    },
    #27/11/2020 11:11:11 -> 1606450271000
    "timeD2":{
        "mili":1606450271000,
        "data":"27/11/2020 11:11:11"
    },
    #27/11/2020 23:59:00 -> 1606496340000
    "timeD21":{
        "mili":1606496340000,
        "data":"27/11/2020 23:59:00"
    },
    #28/11/2020 23:59:00 -> 1606582740000
    "timeD3":{
        "mili":1606582740000,
        "data":"28/11/2020 23:59:00"
    },
    #30/11/2020 11:11:11 -> 1606709471000
    "timeD5":{
        "mili":1606709471000,
        "data":"30/11/2020 11:11:11"
    },
    #01/12/2020 11:11:11 -> 1606795871000
    "timeD6":{
        "mili":1606795871000,
        "data":"01/12/2020 11:11:11"
    },
    #01/12/2020 23:59:00 -> 1606841940000
    "timeD7":{
        "mili":1606841940000,
        "data":"01/12/2020 23:59:00"
    },
    #02/12/2020 23:59:00 -> 1606928340000
    "timeD8":{
        "mili":1606928340000,
        "data":"02/12/2020 23:59:00"
    },
}
timeWC={
    "start":{"Y":2020,"M":11,"D":26,"h":7,"m":0,"s":0},
    "end":{"Y":2020,"M":12,"D":2,"h":7,"m":0,"s":0}
}
def convertDayTimeToMili(Y,M,D,h,m,s):
    dt = datetime(Y,M,D,h,m,s)
    milliseconds = int(round(dt.timestamp() * 1000))
    print(milliseconds)
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
                "detailMission":poco(text="Cambiar una por una "),
                "totalX":3,
                "tacos":4,
                "gold":80000
                },
    },
    "final":{
        "data":{
            "total X":4,
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
            "totalX":30,
            "tacos":4,
            "gold":40000
           },
    },
    "collect":{
        "data":{
            "totalX":4,
            "tacos":2,
            "gold":20000
        },
    },
    "claim":{
        "data":{
            "gold":120000
        } 
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
<<<<<<< HEAD
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
=======
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
# convertDayTimeToMili(2020, 11, 26,6,59,0)   
# print(challengePlay[challenge["day2"]["mission"]]["data"]["gold"])
#----------------------------------------------------WC----------------------------------------------------------------------#

>>>>>>> d9dbc169592addba88d98510bd6e86d143e1bb62


