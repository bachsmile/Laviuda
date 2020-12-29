#--------------Tile----------------------------------------#
__author__ = "QC"
__title__ ="List Function"
__desc__="""
    Tong hop danh sach cac function test Feature
"""
#--------------End Tile------------------------------------#
#--------------Import LIB----------------------------------#
import json
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.cocosjs import CocosJsPoco
from poco.exceptions import PocoTargetTimeout
#--------------End Import Lib------------------------------#
#--------------Import FILE---------------------------------#

# from Lavuavi.Config.Api import *
#link cheat:
from Lavuavi.Config.Api import *
#----------------------------------------------------------#
from Lavuavi.Config.config import *
from Lavuavi.Report.report import *
from Lavuavi.Img.img import *
#--------------End Import FILE-----------------------------#
#--------------Connect Device------------------------------#

if not cli_setup():
    auto_setup(__file__)
    
#--------------End Connect---------------------------------#
#--------------Poco----------------------------------------#

poco = CocosJsPoco()

#--------------End Poco------------------------------------#
# script content
#--------------bien----------------------------------------#

#-------------end bien-------------------------------------#
#----------------------------Function-------------------------------------------------#
#Function general:----------------->
    #Login
    #CheckUpdateGold
    #KillApp
def killApp():
try:
    clear_app("com.zingplay.laviuda")
    print('kill App')
    return True
except:
    print('error kill App')
    return False
    #openApp
def openApp():
    try:
        start_app("com.zingplay.laviuda")
        print('open App')
        return True
    except:
        print('error open App')
        return False
#Function DB:---------------------->
def kill_app():
    home()
    time.sleep(60)
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    Laviuda.click()
def log_out():
    data={
        "status":"Fail"
    }
    try:
        poco("btnPlay").exists
    except:
        print("Please back to lobby page!")
    else:
        print("Success!")
    poco("iconSetting").click()
    poco("bgLobbyLayer2").click()
    touch(Template(r"tpl1608523320839.png", record_pos=(0.097, 0.08), resolution=(1280, 720)))
    data["status"]="True"
    reportdailybonus(data)
def log_in():
    poco = CocosJsPoco()
    poco("btnSwitch").exists()
    poco("btnGuest").click()
def log_in_FB():
    poco("btnFacebookNormal").click()
    time.sleep(5)
def log_in_gg():
    poco = CocosJsPoco()
    poco("btnGooglePlus").exists()
    poco("btnGooglePlus").click()  
    #touch(Template(r"tpl1608609498145.png", record_pos=(-0.179, -0.024), resolution=(1920, 1080)))
    #touch(Template(r"tpl1608620394570.png", record_pos=(-0.182, 0.034), resolution=(1280, 720)))
    
    touch(Template(r"tpl1608889559766.png", record_pos=(-0.211, 0.057), resolution=(1920, 1080)))


    #touch(Template(r"tpl1608620797537.png", record_pos=(0.355, -0.17), resolution=(1280, 720)))
    


def gold_number():
    gold=poco("lbGold").get_text()
    dec=["M","K","B"]
    for index in range(len(dec)):
        don_vi=gold.endswith(dec[index])
        #print(don_vi)
        if don_vi== True:
            #print(dec[index])
            num = gold.split(dec[index]) 
            if dec[index]=="M":  
                num = gold.split("M")  #print(num)
                number= num[0]         #print(number)
                number= float(number)    #print(type(number)) 
                number=number*1000000
                #print(number)
            elif dec[index]=="K":
                num = gold.split("K")   #print(num) 
                number= num[0]          #print(number)
                number= float(number)   #print(type(number))
                number=number*1000
                #print(number)
            elif dec[index]=="B":
                num = gold.split("B")   #print(num)
                number= num[0]          #print(number)
                number= float(number)   #print(type(number))
                number=number*1000000000
                #print(number)
    return number
def update_golp():    
    data={
    "status":"Fail"
    }
    gold_befor2= gold_number()
    poco("btnClaim").click()
    gold_after2= gold_number()
    if DailyBonus["day2"]["bonus"]==(gold_after2 - gold_befor2):    
        data["status"]="True"
    else: 
        data["status"]="False"
    reportdailybonus(data)
    return 3

def cheatGold(idU,gold):
    try:
        cheat = api_postDoFunction(idU, "ADD_GOLD", [gold])
        print(cheat)
        print("cheat gold success")
        return True
    except:
        print("Error cheat gold")
        return False
    
def killApp():
    try:
        clear_app("com.zingplay.laviuda")
        print('kill App')
        return True
    except:
        print('error kill App')
        return False
def openApp():
    try:
        start_app("com.zingplay.laviuda")
        print('open App')
    except:
        print('error open App')
def reloadLobby():
    try:
        poco = CocosJsPoco()
        poco("btnPlay").click()
        sleep(1)
        poco("btnLeaveGame").click()
        print('reload lobby')
        return True
    except:
        print('error reload lobby')
        return False
timeWC={"Y":2020,"M":12,"D":7,"h":8,"m":0,"s":0}
    #"end":{"Y":2020,"M":12,"D":2,"h":7,"m":0,"s":0} 
def convertDayTimeToMili(time):
    print("milliseconds")
    dt = datetime(time['Y'],time['M'],time['D'],time['h'],time['m'],time['s'])
    milliseconds = int(round(dt.timestamp() * 1000))
    print(milliseconds)
    return milliseconds  
# def cheatGoldEmpty(gold):
#     try:
#         poco("btnCheat").click()
#         if exists(Template(r"tpl1608102257956.png", record_pos=(0.186, 0.083), resolution=(2400, 1080))):
#             touch(Template(r"tpl1608102257956.png", record_pos=(0.186, 0.083), resolution=(2400, 1080)))
#         else:
#             touch(Template(r"tpl1608102303058.png", record_pos=(0.184, 0.083), resolution=(2400, 1080)))
#         text(gold)
#         poco("btnSendCheatPlayer").click()
#         poco("btnCheat").click()
#         print("cheat gold success")
#         return True
#     except:
#         print("Error cheat gold")
#         return False
def cheat_gold(gold):
    poco("lbTimeServer").click()
    time.sleep(2)
    #poco("pnGold").long_click()
    gold =str(gold)
    touch(Template(r"tpl1609131029797.png", record_pos=(0.064, 0.102), resolution=(1920, 1080)))
    time.sleep(3)
    text(gold)
    time.sleep(3)
    poco("btnSendCheatPlayer").click()
    poco("lbTimeServer").click()
def cheatGold(idU,gold):
    try:
        cheat = api_postDoFunction(idU, "ADD_GOLD", [gold])
        print(cheat)
        print("cheat gold success")
        return True
    except:
        print("Error cheat gold")
        return False
def check_gold(a, c):     #a: gold before, c: config
    d=a-c
    cheat_gold(1000000)
    time.sleep(5)
    poco("btnClaim").click()
    cheatGold(19501203,d)
    gold_curent=cheatGold(19501203,d)
    gold=gold_number()
    if d>=1000000:
        d=99
    elif d>=1000000000:
        d=99999999  
    print(gold)
    if 2*a== gold :
        if gold_curent-1 != gold and 2*a != gold_curent + d:
            print("Update gold sai")
            data["status"]="false"
            print("false")
        else:
            print("update gold dung")
            data["status"]="true"
    else:
        Print("Update gold wrong")
        data["status"]="false"
api_changeTimeServer(convertDayTimeToMili(timeWC))
reloadLobby()
check_gold(1000000,400000)
def checkGold(init,config):
    print("init: "+str(init))
    print("config: "+str(config))
    goldSumCofg=init+config
    print("goldSumCofg: " + str(goldSumCofg))
    golShow=pow(10,muc(goldSumCofg)-2)
    print("golShow: " + str(golShow))
    realClaim = 1000
    print("realClaim: " + str(realClaim))
    sumReal=init+realClaim
    print("sumReal: " + str(sumReal))
    if config>golShow:
        if(config/golShow)%1>0:
            goldRcf = int(config)+golShow
        else:
            goldRcf=config
        print("goldRcf: " + str(goldRcf))
        sumExpect = init + goldRcf
        print("sumExpect: " + str(sumExpect))
        LenghtCF = muc(config)
        print("LenghtCF: " + str(LenghtCF))
        mucRound = pow(10, LenghtCF - 1)
        print("mucRound: " + str(mucRound))
        goldWant = goldRcf - config
        print("goldWant: " + str(goldWant))
        goldAdd = pow(10, muc(goldWant) - 1)
        print("goldAdd: " + str(goldAdd))
        loop = int(goldWant / goldAdd)
        print("loop: " + str(loop))
        for x in range(loop):
            print(x)
            sumReal += goldAdd
            if sumReal == sumExpect:
                print("c=b")
                return realClaim
            elif sumReal < sumExpect:
                continue
            else:
                print("c>b")
                print(sumReal)
                return x
        if sumReal < sumExpect:
            print(sumReal)
            print("c<b")
    else:
        goldRcf = golShow
        print("goldRcf: " + str(goldRcf))
        sumExpect = init + goldRcf
        print("sumExpect: " + str(sumExpect))
        goldWant = goldRcf - config
        print("goldWant: " + str(goldWant))
        goldAdd = pow(10, muc(goldWant) - 1)
        print("goldAdd: " + str(goldAdd))
        loop = goldWant / goldAdd
        if loop%1 >0:
            loops = int(loop)
            du=goldWant-(goldAdd*loops)
            print("du: " + str(du))
            print("loop: " + str(loops))
            loopDu=int(du/ 1000)
            for x in range(loops):
                sumReal += goldAdd
                if sumReal > sumExpect:
                    print("c>b")
                    return realClaim
            for x in range(loopDu):
                sumReal += 1000
                if sumReal > sumExpect:
                    print("c>b")
                    return realClaim
            if sumReal < sumExpect:
                print("c<b")
            if sumReal == sumExpect:
                print(sumReal)
                print("c==b")
        else:
            loops=int(loop)
            print("loop: " + str(loops))
            for x in range(loops):
                print(x)
                sumReal += goldAdd
                if sumReal > sumExpect:
                    print("c>b")
                    return realClaim
            if sumReal < sumExpect:
                print(sumReal)
                print("c<b")
            if sumReal == sumExpect:
                print(sumReal)
                print("c==b")
def muc(gold):
    lenght=len(str(gold))
    return lenght
print(checkGold(1000000,1100))
#Function VIP:--------------------->
#Function WC:---------------------->
#-------------------------------------------------------------------------------------#

/44444444