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
from Lavuida.Config.Api import *
#----------------------------------------------------------#
from Laviuda.Config.config import *
from Laviuda.Report.report import *
from Laviuda.Img.img import *
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
#highlight
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
        return True
    except:
        print('error open App')
        return False
def waitNoLimit(obj,time):
    try:
        wait(obj,time,0.5)
        return True 
    except:
        return False
def waitNolimitPoco(obj,time):
    return obj.wait(time).exists()
def pipeSubGold(strGold):
    gold=0
    lenght = len(strGold)-1
    gold= float(strGold[0:lenght])
    if strGold[lenght:len(strGold)]=='K':
        gold=gold*1000
    elif strGold[lenght:len(strGold)]=='M':
        gold=gold*1000000
        print(type(gold))
    elif strGold[lenght:len(strGold)]=='B':
        gold=gold*1000000000
    else:
        gold=float(strGold)
    return gold
def fortmartTime(time):
    timeStr= str(time['D'])+"/"+str(time['M'])+"/"+str(time['Y'])+" "+str(time['h'])+":"+str(time['m'])+":"+str(time['s'])
    print(timeStr)
    return timeStr
# Action
def reloadLobby():
    try:
        poco = CocosJsPoco()
        pocoTag.btnPlay.click()
        sleep(1)
        pocotag.btnLeaveGame.click()
        print('reload lobby')
        return True
    except:
        print('error reload lobby')
        return False
def reloadLoby2():
    poco = CocosJsPoco()
    poco.click([0.04817596456992819, 0.9241753578186035])
    pocoTag.btnHide.click()
def closeEvent():
    try:
        sleep(1)
        poco = CocosJsPoco()
        if waitNolimitPoco(pocoTag.btnClose,1):
            pocoTag.btnClose.click()
    except:
        print("error close ev")
def out():
    try:
        poco = CocosJsPoco()
        pocoTag.btnSetting.click()
        sleep(1)
        wait(imageInOutAcc.imgBtnOut)
        touch(imageInOutAcc.imgBtnOut)
        touch(imageInOutAcc.imgOutOk)
        print("out")
    except:
        print("error out")
def changeAcc(userN,passW):
    try:
        out()
        poco = CocosJsPoco()
        pocoTag.btnSwitch.click()
        pocoTag.inputUser.click()
        sleep(1)
        text("")
        pocoTag.inputUser.click()
        sleep(1)
        User=str(userN)
        text(User)
        pocoTag.logo.click()
        pocotag.inputPass.click()
        PassW=str(passW)
        text(PassW)
        pocoTag.logo.click()
        pocoTag.btnLogin.click()
        return True
    except:
        print("error login")
        return False
def joinTable():
    try:
        sleep(2)
        poco = CocosJsPoco()
        pocoTag.btnPlay.click()
        print("joinTable")
        return 1
    except:
        print("error joinTable")
        return 0
def clickOutTable():
    try:
        poco = CocosJsPoco()
        pocoTag.btnLeaveGame.click()
        print("register back")
        return True
    except:
        print("error register back")
        return False
def addBot():
    try:
        poco = CocosJsPoco()
        pocoTag.btnCheat.click()
        for i in range(2):
            sleep(1)
            pocoTag.btnAddBot.click()
        pocoTag.btnCheat.click()
        print("event addBot")
        return True
    except:
        print("error addBot")
        return False
def clickKnock():
    try:
        if waitNolimitPoco(pocoTag.btnKnock,60):
            pocoTag.btnKnock.click()
            print("event clickKnock")
            return True
        else:
            print("end countdown time")
            return False
    except:
        print("error clickKnock")
        return False
def clickPass():
    try:
        if waitNolimitPoco(pocoTag.btnPass,60):
            pocotag.btnPass.click()
            print("pass")
            return True
        else:
            print("no find btn pass")
            return False  
    except:
        print("error Pass")
        return False
def clickExchange1():
    try:
        if waitNolimitPoco(pocoTag.btnExchange1,60):
            pocoTag.btnExchange1.click()
            sleep(1)
            poco.click([0.6264933239634575, 0.8615635156631469])
            sleep(1)
            poco.click([0.6602340558843552, 0.4599999904632568])
            sleep(1)
            pocoTag.btnSwap.click()
            print("event Exchange1")
            return True
        else:
            print("end countdown time")
            return False  
    except:
        print("error Exchange1")
        return False
def clickExchange5():
    try:
        if waitNolimitPoco(pocoTag.btnExchange5,60):
            pocoTag.btnExchange5.click()
            return True
        else:
            return False
    except:
        return False
def clickClaim():
    try:
        if waitNolimitPoco(pocoTag.btnClaim,1):
            pocoTag.btnClaim.click()
            return True
        else:
            return False
    except:
        return False
# check
def tableGame():
    try:
        if waitNolimitPoco(pocoTag.bg_table,10):
            print("table play")
            return True
        else:
            print("end countdown time")
            return False
    except:
        print("error table play")
        return False
#Function DB:---------------------->
#Function VIP:--------------------->
#Function WC:---------------------->
#------------------#
def beforEvent():
    clearReport()
    #Cheat time-------------24/11/2020 7:00:00----------
    timeCheat = api_changeTimeServer(1605051600000)
#     timeCheat = api_changeTimeServer(timeC["timeD0"]["mili"])
    dayS = {
        "Y": timeWC["start"]['Y'],
        "M": timeWC["start"]['M'],
        "D": timeWC["start"]['D'],
        "h": timeWC["start"]['h'],
        "m": timeWC["start"]['m'],
        "s": timeWC["start"]['s']
    }
    dayS['D'] = dayS['D']-2
    timeCheat = api_changeTimeServer(convertDayTimeToMili(dayS))
    dataReportConfig["TimeCheat"]=fortmartTime(dayS)
    if timeCheat ==200:
        dataReportConfig['CheatTime']="Pass"
    else:
        dataReportConfig['CheatTime']="Fail"
    #End Cheatime---------------------------------------
    #changeAcc
    changeAcc(user["user0"]["user"],user["user0"]["pass"])
    sleep(5)
    closeEvent()
    #In Game--------------------------------------------
    #---------reload lobby------------------------------
    reloadLobby()
    reloadLoby2()
    #---------end reload lobby--------------------------
    #End in Game----------------------------------------
    #Check btn event -----------------------------------
    if CheckBtnEvent():
        dataReportConfig["Button"]="Fail"
    else:
        dataReportConfig["Button"]="Pass"
    #end Check btn event--------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    print(dataReportConfig)
    reportBeforEvent(dataReportConfig)
#------------------#
#-------------------------------------------------------------------------------------#

