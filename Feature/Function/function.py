#--------------Tile----------------------------------------#
__author__ = "QC"
__title__ ="List Function"
__desc__="""
    Tong hop danh sach cac function test Feature
"""
#--------------End Tile------------------------------------#
#--------------Import LIB----------------------------------#
import json
import re
import sys
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.cocosjs import CocosJsPoco
#--------------End Import Lib------------------------------#
#--------------Import FILE---------------------------------#
# from Lavuavi.Config.Api import *
#link cheat:
from Laviuda.Config.Api import *
#----------------------------------------------------------#
from Laviuda.Config.config import *
from Laviuda.Report.report import *
from Laviuda.Img.img import *
from Laviuda.Poco.poco import *
from importlib import reload
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
def exists1(self):
        try:
            return self.attr('visible')
        except :
            return 0
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
#cheat
def cheatGoldEmpty(gold):
    try:
        pocoTag.btnCheat.click()
        if waitNolimitPoco(pocoTag.pnGold,2):
            pocoTag.pnGold.click([0.6045215255512122, 0.41971168518066404])
            text(str(gold))
        else:
            return False
        pocoTag.btnSendCheatPlayer.click()
        pocoTag.btnCheat.click()
        print("Cheat tien thanh cong")
        return True
    except:
        print("Khong tim thay")
        return False
def CheatCard(wildCard,cardPlay):#ex: WildCard = '2c', cardPlay="ab,2b,3b,4b,5b"
    pocoTag.btnCheat.click()
    pocoTag.btnTabCustom.click()
    pocoTag.btnResetCustom.click()
    pocoTag.pnPointEvent.click([0.7598879526638265, 0.6159336566925049])
    text(wildCard)
    pocoTag.pnCaseId_1.click([0.5944052164770731, 0.4596827030181885] )
    text(cardPlay)
    pocoTag.btnSendCustom.click()
    pocoTag.btnCheat.click() 
# Action
def back_to_lobby():
    btns = [image_vip.back, image_vip.close, image_vip.outroom]
    try:
        for btn in btns:
            if exists(btn):
                touch(btn)
                print("back lobby thanh cong")
            continue
    except:
        print("back lobby khong thanh cong")
def reloadLobby():
    try:
        poco = CocosJsPoco()
        pocoTag.btnPlay.click()
        back_to_lobby()
        sleep(1)
#         pocoTag.btnLeaveGame.click()
#         touch(image_vip.back)    
        print('reload lobby')
        return True
    except:
        print('error reload lobby')
        return False
reloadLobby()
def reloadLoby2():
    poco = CocosJsPoco()
    poco.click([0.04817596456992819, 0.9241753578186035])
    pocoTag.btnHide.click()
def closeEvent():
    try:
        if waitNolimitPoco(poco("btnClose"),2):
            poco("btnClose").click()
    except:
        print("error close ev")
def closeAllEvent():
    while waitNolimitPoco(poco("btnClose"),2):
        pocoTag.btnClose.click()
def claimAll():
    while waitNolimitPoco(poco("btnClaim"),2):
        pocoTag.btnClaim.click()
        continue
def out():
    try:
        poco = CocosJsPoco()
        pocoTag.btnSetting.click()
        wait(imageInOutAcc.imgBtnOut)
        touch(imageInOutAcc.imgBtnOut)
        touch(imageInOutAcc.imgOutOk)
        print("out")
    except:
        print("error out")
def changeAcc(userN,passW):
    try:
        poco = CocosJsPoco()
        out()
        pocoTag.btnSwitch.click()
        pocoTag.inputUser.click()
        sleep(1)
        text("")
        pocoTag.inputUser.click()
        sleep(1)
        User=str(userN)
        text(User)
        pocoTag.logo.click()
        pocoTag.inputPass.click()
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
#         pocoTag.btnPlay.click()
        pocoTag.btnSelectTable.click()
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
        if waitNolimitPoco(poco("btnKnock"),60):
            poco("btnKnock").click()
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
        if waitNolimitPoco(poco("btnPass"),60):
            poco("btnPass").click()
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
def CheckLobby():
    try:
        if waitNolimitPoco(pocoTag.btnPlay,60):
            print("check back lobby")
            return True
        else:
            print("back lobby fail")
            return False
    except:
        print("error back lobby")
        return False
def waitEndGame():
    try:
        poco = CocosJsPoco()
#       if waitNolimitPoco(poco("imgOtherWin"),100):  
        if waitNoLimit(imageWC.imgWin,100):
            print("end game")
            return True
        else:
            print("end time down")
            return False
    except:
        print("error")
        return False
def waitEndGame2():
    try:
        poco = CocosJsPoco()
#       if waitNolimitPoco(poco("imgOtherWin"),100):  
        if waitNoLimit(imageWC.imgWin2,100):
            print("end game")
            return True
        else:
            print("end time down")
            return False
    except:
        print("error")
        return False
def checkGold():
#     numGold = pocoTag.lbGold.attr("text")
    numGold = poco(name="lbGold").attr("text")
    return pipeSubGold(numGold)
def convertDayTimeToMili(time):
    dt = datetime(time['Y'],time['M'],time['D'],time['h'],time['m'],time['s'])
    milliseconds = int(round(dt.timestamp() * 1000))
    print(milliseconds)
    return milliseconds
#Function VIP:--------------------->
def convertDayToSecond(day):
    second = int(day*24*60*60)
    return second
def cheatTimeRemain(UserID,day):
    try:
        cheat_remain = api_postDoFunction(UserID, "CHEAT_TIME_REMAIN_VIP", [convertDayToSecond(day)])
        print("cheat time remain thanh cong")
        reloadLobby()
        print("Vao shop vip thanh cong")
        killApp()
        openApp()
        #check show pop-up gia han
        back_to_lobby()
        return True 
    except:
        print("Error")
        return False
def open_vip():
    try:
        if exists(image_vip.btn_vip):
            pocoTag.btnVip.click()
            data["Status"] = "Pass"
            print("Vao thanh cong")
    except:
        data["Status"] = "Fail"
        print("error")
        time.sleep(2)
def open_pack(pack):
    try:
        poco(pack).click()
        touch(image_vip.btn_cancel)
        data["Status"] = "Pass"
        print("Mo thanh cong")
    except:
        data["Status"] = "Fail"
        print("error")
def check_item():
    items = [image_vip.cachua, image_vip.votay, image_vip.xonuoc, image_vip.trung, image_vip.hoahong, image_vip.hoavang, image_vip.sungnuoc]
    try:
        touch(image_vip.btn_profile)
        if exists(image_vip.list_item):
            #return False
            for item in items:
                if exists(item):
                    touch(item)
                    time.sleep(2)
                    touch(image_vip.btn_profile)
                else:
                    swipe(Template(r"tpl1610432749141.png", record_pos=(0.114, 0.123), resolution=(2340, 1079)), vector=[-0.1399, -0.0097])
                    time.sleep(2)
                    touch(item)
            data["Check_item"] = "Pass"
            print("List item co ton tai")
        else:
            #return True
            data["Check_item"] = "Fail"
            print("List item khong ton tai")
        back_to_lobby()
    except:
        print("Error")
def check_item3():
    try:
        touch(image_vip.btn_profile)
        if exists(image_vip.list_item):
            swipe(Template(r"tpl1610432749141.png", record_pos=(0.114, 0.123), resolution=(2340, 1079)), vector=[-0.1399, -0.0097])
            time.sleep(2)
            touch(image_vip.boom)
        print("success")
    except:
        print("Error")
def to_table():
    try:
        pocoTag.btnPlay.click()
        pocoTag.btnCheat.click()
        pocoTag.btnAddBot.click()
        time.sleep(2)
        pocoTag.btnCheat.click()
        time.sleep(2)
        print("Vao ban, cheat bot thanh cong")
    except:
        print("Khong thanh cong")
def buy_vip_thap(pack):
    try:
        poco(pack).click()
        time.sleep(1)
        touch(image_vip.btn_ok)
        data["Check_low_vip"] = "Pass"
        print("Khong mua duoc vip thap hon")
    except:
        data["Check_low_vip"] = "Fail"
        print("Error")
def checkExists(self):
    try:
        return self.attr('visible')
    except :
        return 0
def checkTimeRemainVip():
    try:
        if checkExists(poco("lbTimeMyVip")):
            old_day = int(re.sub(r'\D', '', poco("lbTimeMyVip").get_text()))
            print(old_day)
#             return old_day
        else:
            print(0)
    except:
        print("error")
def cheatPayMentVip(idU, pack):
    try:
        cheat = api_postDoFunction(idU, "CHEAT_PAYMENT_VIP", [pack])
        touch(image_vip.btn_claim)
        time.sleep(2)
        print("success")
    except:
        print("error")
def check_buy_vip(idU, pack):
    old_gold = getGold(idU)
    cheatPayMentVip(idU, pack)
    try:
        time.sleep(2)
        new_gold = getGold(idU)
        gold_in = new_gold - old_gold
        gold_conf = vip_pack[pack]["dailyTribute"]
        if gold_in == gold_conf:
            data["Check_gold"] = "Pass"
            print("Success")
    except:
        data["Check_gold"] = "Pass"
        print("Error")
# check_buy_vip(19202812, "vip.pack_1")
# reportBuyVip(data)
def check_gold_support(idU):
    cheatGoldEmpty(1)
    reloadLobby()
    old_gold = getGold(idU)
    try:
        if exists(image_vip.btn_ok):
            image_vip.btn_ok
            new_gold = getGold(idU)
            gold_in = new_gold - old_gold
            gold_conf = gold_support
            if gold_in == gold_conf: 
                data["Status"] = "Pass"
                print("Nhan gold support thanh cong")
    except:
        data["Status"] = "Fail"
        print("Khong nhan duoc gold support")
def cheatBuyGold(idU, pack):
    try:
        cheat = api_postDoFunction(idU, "CHEAT_PAYMENT_IAP", [pack])
        pocoTag.btnClaim
        time.sleep(2)
        print("Success")
    except:
        print("Error")
def check_buy_gold(idU, pack):
    old_gold = getGold(idU)
    cheatBuyGold(idU, pack)
    try:
        new_gold = getGold(idU)
        gold_in = new_gold - old_gold
        gold_conf = pack_gold["gg_play"][pack]
        if gold_in == gold_conf:
            data["Check_gold"] = "Pass"
            data["Status"] = "Pass"
            print("Success")
    except:
        data["Status"] = "Fail"
        print("Error")
def check_gold_tribute():
    try:
        if exists(image_vip.btn_claim):
            pocoTag.btnClaim
            data["Status"] = "Pass"
            print("Success")
    except:
        data["Status"] = "Fail"
        print("Error")
def checkMoGUIVipGD():
    try:
        if exists(image_vip.btn_giahan):
            data["Show_PopUp_GH"] = "Pass"
            touch(image_vip.btn_giahan)
            data["Mo_GUI_Vip"] = "Pass"
            print("Success")
        else:
            data["Show_PopUp_GH"] = "Fail"
            data["Mo_GUI_Vip"] = "Fail"
            print("error")
    except:
        print("error")
def checkLevelVip():
    try:
        touch(image_vip.btn_profile)  
        if exists(image_vip.vip_dy):
            print("user dang co vip kim cuong")
        if exists(image_vip.vip_gold):
            print("user dang co vip vang")
        if exists(image_vip.vip_silver):
            print("user dang co vip bac")
        if exists(image_vip.no_vip):
            print("user dang non vip")
    except:
        print("error")
def checkExists(self):
    try:
        return self.attr('visible')
    except :
        return 0
#Function WC:---------------------->
    #------------------#
def beforEvent():
    clearReport()
    timeCheat = api_changeTimeServer(1605051600000)
    dayS = {
        "Y": timeWC["start"]['Y'],
        "M": timeWC["start"]['M'],
        "D": timeWC["start"]['D'],
        "h": timeWC["start"]['h'],
        "m": timeWC["start"]['m'],
        "s": timeWC["start"]['s']
    }
    timeNow=convertDayTimeToMili(dayS) - datetoMili(1) + housToMili(10)
    timeCheat = api_changeTimeServer(timeNow)
    dataReportConfig["TimeCheat"]=convertSecondstoDateTime(timeNow)
    if timeCheat ==200:
        dataReportConfig['CheatTime']="Pass"
    else:
        dataReportConfig['CheatTime']="Fail"
    #End Cheatime---------------------------------------
    #changeAcc
    changeAcc(user["user0"]["user"],user["user0"]["pass"])
    sleep(5)
    #closeEvent()
    claimAll()
    closeAllEvent()
    #reloadLobby()
    reloadLoby2()
    claimAll()
    closeAllEvent()
    #Check btn event -----------------------------------
    if CheckBtnEvent():
        dataReportConfig["Button"]="Fail"
    else:
        dataReportConfig["Button"]="Pass"
    #end Check btn event--------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportBeforEvent(dataReportConfig)
def afterEvent():
    resetDataReportConfig()
    sleep(2)
#-------------In Game-------------------------------------------------#
    #-------------Cheat time-----------------------------------#
    #26/11/2020 06:59:00
    timeCheat = api_changeTimeServer(1605051600000)
    dayS = {
        "Y": timeWC["start"]['Y'],
        "M": timeWC["start"]['M'],
        "D": timeWC["start"]['D'],
        "h": timeWC["start"]['h'],
        "m": timeWC["start"]['m'],
        "s": timeWC["start"]['s']
    }
    timeNow=convertDayTimeToMili(dayS) -housToMili(1)+ minutetoMili(59)+secToMili(30)
    timeCheat = api_changeTimeServer(timeNow)
    dataReportConfig["TimeCheat"]=convertSecondstoDateTime(timeNow)
    if timeCheat ==200:
        dataReportConfig['CheatTime']="Pass"
    else:
        dataReportConfig['CheatTime']="Fail"
    #-------------End Cheatime---------------------------------#
    #reload lobby------------------------------
    reloadLobby()
    claimAll()
    closeAllEvent()
#     clickClaim()
    reloadLoby2()
 #Check event--------------------------------------------------#
    #Check btn event -----------------------------------
    if CheckBtnEvent():
        try:
            eventWCOpen()
            if CheckNotiEvent():
                print(1)
                dataReportConfig['Befor']="Pass"
                if coutDownTime()==1:
                    dataReportConfig["Coutdown"]="Pass"
                else:
                    dataReportConfig["Coutdown"]="Fail"
                if eventWCOpen():
                    dataReportConfig["After"]="Pass"
                else:
                    dataReportConfig["After"]="Fail"
                if waitNolimitPoco(pocoTag.btnJoin,2):
                    dataReportConfig['ShowBtnJoin']="Pass"
                else:
                    dataReportConfig['ShowBtnJoin']="Fail"
                closeEvent()
                #cheat time back 1p
                #26/11/2020 06:59:20
                timeCheat = api_changeTimeServer(1605051600000)
                dayS1 = {
                    "Y": timeWC["start"]['Y'],
                    "M": timeWC["start"]['M'],
                    "D": timeWC["start"]['D'],
                    "h": timeWC["start"]['h'],
                    "m": timeWC["start"]['m'],
                    "s": timeWC["start"]['s']
                }
                timeNow=convertDayTimeToMili(dayS1) -housToMili(1)+ minutetoMili(59)
                timeCheat = api_changeTimeServer(timeNow)
                dataReportConfig["TimeCheat"]=convertSecondstoDateTime(timeNow)
                if timeCheat ==200:
                    dataReportConfig['CheatTime1']="Pass"
                else:
                    dataReportConfig['CheatTime1']="Fail"
                sleep(1)
#                 killApp()
#                 sleep(2)
#                 openApp()
#                 sleep(20)
#                 claimAll()
                #changeAcc
                if changeAcc(user["user1"]["user"],user["user1"]["pass"]):
                    claimAll()
                    closeAllEvent()
                    CheckLobby()
                    joinTable()
                    if coutDownTimeIntable():
                        dataReportConfig['ShowProg']="Pass"
                    else:
                        dataReportConfig['ShowProg']="Fail"
                    clickOutTable()
#                     closeEvent()
            else:
                print(2)
                dataReportConfig['Befor']="Fail"
                sleep(20)
                dataReportConfig["Coutdown"]="Fail"
#                 if coutDownTime()==1:
#                     sleep(1)
#                     dataReportConfig["Coutdown"]="Pass"
#                 else:
#                     dataReportConfig["Coutdown"]="Fail"
#          
                #Join event
                if eventWCOpen():
                    dataReportConfig["After"]="Pass"
                else:
                    dataReportConfig["After"]="Fail"
                if waitNolimitPoco(pocoTag.btnJoin,2):
                    dataReportConfig['ShowBtnJoin']="Pass"
                else:
                    dataReportConfig['ShowBtnJoin']="Fail"
                closeEvent()
                #cheat time back 1p
                #26/11/2020 06:59:20
                timeCheat = api_changeTimeServer(1605051600000)
                dayS1 = {
                    "Y": timeWC["start"]['Y'],
                    "M": timeWC["start"]['M'],
                    "D": timeWC["start"]['D'],
                    "h": timeWC["start"]['h'],
                    "m": timeWC["start"]['m'],
                    "s": timeWC["start"]['s']
                }
                timeNow=convertDayTimeToMili(dayS1) -housToMili(1)+ minutetoMili(59)
                timeCheat = api_changeTimeServer(timeNow)
                dataReportConfig["TimeCheat1"]=convertSecondstoDateTime(timeNow)
                if timeCheat ==200:
                    dataReportConfig['CheatTime1']="Pass"
                else:
                    dataReportConfig['CheatTime1']="Fail"
                sleep(1)
#                 closeEvent()
#                 killApp()
# #                 sleep(2)
#                 openApp()
#                 sleep(20)
                CheckLobby()
                sleep(1)
                #changeAcc
                if changeAcc(user["user1"]["user"],user["user1"]["pass"]):
                    claimAll()
                    closeAllEvent()
                    CheckLobby()
                    #join table wait
                    joinTable()
                    #wait event
                    if coutDownTimeIntable():
                        dataReportConfig['ShowProg']="Pass"
                    else:
                        dataReportConfig['ShowProg']="Fail"
                    #back to lobby
                    clickOutTable()
#                     closeEvent()
        except:
            print('btnMain no find')
    else:
        try:
            print(3)
            dataReportConfig['Befor']="Fail"
            sleep(20)
            dataReportConfig["Coutdown"]="Fail"
#                 if coutDownTime()==1:
#                     sleep(1)
#                     dataReportConfig["Coutdown"]="Pass"
#                 else:
#                     dataReportConfig["Coutdown"]="Fail"
            #Join event
            if eventWCOpen():
                dataReportConfig["After"]="Pass"
            else:
                dataReportConfig["After"]="Fail"
#                 eventWCOpen()
            if waitNolimitPoco(pocoTag.btnJoin,2):
                dataReportConfig['ShowBtnJoin']="Pass"
            else:
                dataReportConfig['ShowBtnJoin']="Fail"
            closeEvent()
            #cheat time back 1p
            #26/11/2020 06:59:20
            timeCheat = api_changeTimeServer(1605051600000)
            dayS1 = {
                "Y": timeWC["start"]['Y'],
                "M": timeWC["start"]['M'],
                "D": timeWC["start"]['D'],
                "h": timeWC["start"]['h'],
                "m": timeWC["start"]['m'],
                "s": timeWC["start"]['s']
            }
            timeNow=convertDayTimeToMili(dayS1) -housToMili(1)+ minutetoMili(59)
            timeCheat = api_changeTimeServer(timeNow)
            dataReportConfig["TimeCheat1"]=convertSecondstoDateTime(timeNow)
            if timeCheat ==200:
                dataReportConfig['CheatTime1']="Pass"
            else:
                dataReportConfig['CheatTime1']="Fail"
            sleep(1)
#                 closeEvent()
            #kill app
#                 killApp()
# #                 #open app
# #                 sleep(2)
#                 openApp()
# #                 #wait
#                 sleep(20)
#                 poco = CocosJsPoco()
#                 sleep(1)
            CheckLobby()
            sleep(1)
            #changeAcc
            if changeAcc(user["user1"]["user"],user["user1"]["pass"]):
                sleep(1)
                claimAll()
                closeAllEvent()
                CheckLobby()
                #join table wait
                joinTable()
                #wait event
                if coutDownTimeIntable():
                    dataReportConfig['ShowProg']="Pass"
                else:
                    dataReportConfig['ShowProg']="Fail"
                #back to lobby
                clickOutTable()
#                 closeEvent()
        except:
            print('btnMain no find')
    #end Check btn event--------------------------------
  #end check event---------------------------------------------#
#End in Game----------------------------------------------------------#
#-------------End script----------------------------------#
#-------------Report--------------------------------------#
    reportAfterEvent(dataReportConfig)
def day1():
    resetDataReportConfig()
    #join event
    claimAll()
    closeAllEvent()
    eventWCOpen()
    #Check enable ngay 1 va nhiem vu ngay 1
    if CheckLableDay()==1:
        dataReportConfig["Tab"]="Pass"
        print("ton tai day 1")
    else:
        dataReportConfig["Tab"]="Fail"
        print("error day1")  
    if waitNolimitPoco(challengePlay[challenge["day1"]["mission"]]["data"]["detailMission"],5):
        dataReportConfig["Mission"]="Pass"
        print("nv day1")
    else:
        dataReportConfig["Mission"]="Fail"
        print("error day1")
    print(dataReportConfig)
    closeEvent()
     #------------------------#
    #report
    reportDay1(dataReportConfig)
    checkMission("day1")
def day2():
    #resetDataReport
    resetDataReportConfig()
    claimAll()
    closeAllEvent()
    #cheat time pass 1 ngay-> 27/11/2020 07:00:00
    timeCheat = api_changeTimeServer(1605051600000)
    dayS = {
        "Y": timeWC["start"]['Y'],
        "M": timeWC["start"]['M'],
        "D": timeWC["start"]['D'],
        "h": timeWC["start"]['h'],
        "m": timeWC["start"]['m'],
        "s": timeWC["start"]['s']
    }
    timeNow= convertDayTimeToMili(dayS) + datetoMili(1)
    timeCheat = api_changeTimeServer(timeNow)
    dataReportConfig["TimeCheat"]=convertSecondstoDateTime(timeNow)
    if timeCheat ==200:
        dataReportConfig['CheatTime']="Pass"
    else:
        dataReportConfig['CheatTime']="Fail"
    #reload lobby
    if reloadLobby():
        dataReportConfig['Reload']="Pass"
    else:
        dataReportConfig['Reload']="Fail"
    claimAll()
    closeNotiVip()
    claimAll()
    closeDealSpec1()
    #check auto show event
    if CheckGUIEvent():
        dataReportConfig['GuiEvent']="Pass"
        closeEvent()
    else:
        dataReportConfig['GuiEvent']="Fail"
    #close Gui Event
#     clickClaim()
#     closeEvent()
#     claimAll()
#     closeAllEvent()
    #check auto show deal
    if CheckGUIDeal():
        dataReportConfig['GuiEDeal']="Pass"
            #close Gui Deal
        closeEvent()
    else:
        dataReportConfig['GuiEDeal']="Fail"
    #check mission
     #join event
    eventWCOpen()
    #Check enable ngay 2 va nhiem vu ngay 2
    if CheckLableDay()==2:
        dataReportConfig["Tab"]="Pass"
        print("ton tai day2")
    else:
        dataReportConfig["Tab"]="Fail"
        print("error day2")   
#     if waitNolimitPoco(challenge["day2"]["data"]["detailMission"],5):
    if waitNolimitPoco(challengePlay[challenge["day2"]["mission"]]["data"]["detailMission"],5):
        dataReportConfig["Mission"]="Pass"
        print("nv day2")
    else:
        dataReportConfig["Mission"]="Fail"
        print("error day2")
    closeEvent()
        #------------------------#
    print(dataReportConfig)
    #report
    reportDay2(dataReportConfig)
    #------------------------#
    checkMission("day2")
def day3():
        #resetDataReport
    resetDataReportConfig()
    #------------------------#
    #report
    reportDay3(dataReportConfig)
    #------------------------#
    checkMission("day3")
def day4():
        #resetDataReport
    resetDataReportConfig()
    #------------------------#
    #join event
    eventWCOpen()
    #Check enable ngay 1 va nhiem vu ngay 1
    if CheckLableDay()==4:
        dataReportConfig["Tab"]="Pass"
    else:
        dataReportConfig["Tab"]="Fail"
    if waitNolimitPoco(challengePlay[challenge["day4"]["mission"]]["data"]["detailMission"],5):
        dataReportConfig["Mission"]="Pass"
    else:
        dataReportConfig["Mission"]="Fail"
    print(dataReportConfig)
    closeEvent()
    #report
    reportDay4(dataReportConfig)
    #------------------------#
    checkMission("day4")
def day5():
        #resetDataReport
    resetDataReportConfig()
    #------------------------#
    #cheat time pass 1 ngay-> 30/11/2020 11:11:11 -> 1606709471000
    timeCheat = api_changeTimeServer(1605051600000)
    #timeCheat = api_changeTimeServer(timeC["timeD0"]["mili"])
    dayS = {
        "Y": timeWC["start"]['Y'],
        "M": timeWC["start"]['M'],
        "D": timeWC["start"]['D'],
        "h": timeWC["start"]['h'],
        "m": timeWC["start"]['m'],
        "s": timeWC["start"]['s']
    }
    timeNow=convertDayTimeToMili(dayS) + datetoMili(4)
    timeCheat = api_changeTimeServer(timeNow)
    dataReportConfig["TimeCheat"]=convertSecondstoDateTime(timeNow)
    #End Cheatime--------------------------------------
    reloadLoby()
    #join event
    eventWCOpen()
     #check progress
    prog1=checkProgressCurrent()
    closeEvent()
    #cheat gold du play
    cheatGold(user["user1"]["id"],1000000)
    checkMission2("day5")
    sleep(2)
    eventWCOpen()
    prog2=checkProgressCurrent()
    closeEvent()
    #check update progess
    if checkUpdateProgessTable(prog1,prog2):
        dataReportConfig["Update"]="Pass"
    else:
        dataReportConfig["Update"]="Fail"
    #waitplaygame
    sleep(10)
    eventWCOpen()
     #check progress
    prog3=checkProgressCurrent()
    lose1()
    eventWCOpen()
     #check progress
    prog4=checkProgressCurrent()
    #check update progess
    if checkUpdateProgessTable(prog3,prog4):
        dataReportConfig["NoUpdate"]="Pass"
    else:
        dataReportConfig["NoUpdate"]="Fail"
    #report
    reportDay5(dataReportConfig)
def day6():
        #resetDataReport
    resetDataReportConfig()
    #------------------------#
    #cheat time pass 1 ngay-> 30/11/2020 11:11:11 -> 1606709471000
    timeCheat = api_changeTimeServer(1605051600000)
    #timeCheat = api_changeTimeServer(timeC["timeD0"]["mili"])
    dayS = {
        "Y": timeWC["start"]['Y'],
        "M": timeWC["start"]['M'],
        "D": timeWC["start"]['D'],
        "h": timeWC["start"]['h'],
        "m": timeWC["start"]['m'],
        "s": timeWC["start"]['s']
    }
    timeNow=convertDayTimeToMili(dayS) + datetoMili(5)
    timeCheat = api_changeTimeServer(timeNow)
    dataReportConfig["TimeCheat"]=convertSecondstoDateTime(timeNow)
    #reload lobby
    reloadLobby()
    #click btn play
    joinTable()
    #cheat theo nhiem vu
    #add bot
    addBot()
    #Click knock
    if clickKnock():
        data1["Knock"]="Pass"
    else:
        data1["Knock"]="Fail"
    #wait end game
    waitEndGame()
    #check update progess
    if checkUpdateProgessTable():
        data1["Update"]="Pass"
    else:
        data1["Update"]="Fail"
    #waitplaygame
    sleep(10)
    #cheat theo nhiem vu
    #Click knock
    if clickKnock():
        data1["Knock"]="Pass"
    else:
        data1["Knock"]="Fail"
    #chon thoat table
    clickOutTable()
    #wait end game
    waitEndGame()
    #check update progess
    if checkUpdateProgessTable():
        data1["Update"]="Pass"
    else:
        data1["Update"]="Fail"
       #check lobby
    if CheckLobby():
        data1["Leave"]="Pass"
    else:
        data1["Leave"]="Fail"
    #------------------------#
    #report
    reportDay6(data1)
    #------------------------#
    #report
    reportDay3(dataReportConfig)
    #------------------------#
    checkMission("day3")
def day7():
    #cheat time pass 1 ngay-> #01/12/2020 23:59:00 -> 1606841940000
    #cheat time pass 1 ngay-> 30/11/2020 11:11:11 -> 1606709471000
    timeCheat = api_changeTimeServer(1605051600000)
    #timeCheat = api_changeTimeServer(timeC["timeD0"]["mili"])
    dayS = {
        "Y": timeWC["start"]['Y'],
        "M": timeWC["start"]['M'],
        "D": timeWC["start"]['D'],
        "h": timeWC["start"]['h'],
        "m": timeWC["start"]['m'],
        "s": timeWC["start"]['s']
    }
    timeNow=convertDayTimeToMili(dayS) + datetoMili(6)-minutetoMili(1)
    timeCheat = api_changeTimeServer(timeNow)
    dataReportConfig["TimeCheat"]=convertSecondstoDateTime(timeNow)
    #reload lobby
    reloadLobby()
    claimAll()
    closeAllEvent()
    #click btn play
    joinTable()
    #wait pass day
#     waitTimePassDay(timeW)
    sleep(50)
    #check progess table
    if checkProgessTable():
        dataReportConfig["Progess"]="Fail"
    else:
        dataReportConfig["Progess"]="Pass"
    #chon thoat table
    clickOutTable()
    claimAll()
    #check auto show event
    if CheckGUIEvent():
        dataReportConfig['GuiEvent']="Pass"
    else:
        dataReportConfig['GuiEvent']="Fail"
    #check gold init
    goldInit=getGold(user["user1"]["id"])
    #check gold claim
    goldClaim=challengePlay[challenge["day7"]["mission"]]["data"]["gold"]
    #click claim gift
    if clickClaim():
        dataReportConfig['Claim']="Pass"
    else:
        dataReportConfig['Claim']="Fail"
    #exit GUI event
    closeEvent()
    #check update gold
    goldAfter=getGold(user["user1"]["id"])
    if checkUpdateGold(goldClaim,goldInit,goldAfter):
        dataReportConfig['UpdateGold']="Pass"
    else:
        dataReportConfig['UpdateGold']="Fail"
    #close Gui Event
    closeEvent()
    #change acc3
    changeAcc(user["user3"]["user"],user["user3"]["pass"])
    #check gift
    #------------------------#
    #report
    reportDay7(dataReportConfig)
def exchange1(day):
    print(day)
    try:
        prog1=0
        prog2=0
        prog3=0
        #join event
#         eventWCOpen()
        sleep(1)
        eventWCOpen()
        #check progress
        prog1=checkProgressCurrent()
#         return 1
        closeEvent()
        cheatGold(user["user1"]["id"],1000000) 
        #click btn play
        if joinTable():
            dataReportConfig["BtnPlay"]="Pass"
        else:
            dataReportConfig["BtnPlay"]="Fail"
        #cheat cheatPorkerSpecial
        #add bot
        if addBot():
            dataReportConfig["Bot"]="Pass"
        else:
            dataReportConfig["Bot"]="Fail"
        #Click exchange5
        clickExchange5()
        #Click Exchange1
        if clickExchange1():
            dataReportConfig["Exchange1"]="Pass"
        else:
            dataReportConfig["Exchange1"]="Fail"
        sleep(3)
        #check update progess
        touch(imageWC.imgCar)
        prog2=checkProgressCurrent()
        if checkUpdateProgessTable(prog1,prog2):
            dataReportConfig["Update"]="Pass"
        else:
            dataReportConfig["Update"]="Fail"
        #click knock
        clickKnock()
        #chon thoat table
        if clickOutTable():
            dataReportConfig["ChooseLeave"]="Pass"
        else:
            dataReportConfig["ChooseLeave"]="Fail"
        #wait end game
        waitEndGame()
        #check update progess
        prog3=checkProgressCurrent()
        if checkUpdateProgessTable(prog2,prog3):
            dataReportConfig["NoUpdate"]="Fail"
        else:
            dataReportConfig["NoUpdate"]="Pass"
        #check lobby
        if CheckLobby():
            dataReportConfig["Leave"]="Pass"
        else:
            dataReportConfig["Leave"]="Fail"
    except:
        print("error exchange1")
    print(dataReportConfig)
    reportExchange1(dataReportConfig)
def knock(day):
    try:
        #join event
        eventWCOpen()
        eventWCOpen()
        #check progress
        prog1=checkProgressCurrent()
        closeEvent()
        #cheat gold du play
        cheatGold(user["user1"]["id"],1000000)
        #click btn play
        joinTable()
        #Check table
        tableGame()
        #cheat cheatPorkerSpecial
        #add bot
        addBot()
        #Click knock
        if clickKnock():
            dataReportConfig["Knock"]="Pass"
        else:
            dataReportConfig["Knock"]="Fail"
        prog2=checkProgressCurrent()
        #cheat win finished game
        # cheatNumMision(1)
        #chon thoat table
        clickOutTable()
        #wait end game
        waitEndGame()
        #check update progess
        if checkUpdateProgessTable(prog1,prog2):
            dataReportConfig["Update"]="Pass"
        else:
            dataReportConfig["Update"]="Fail"
           #check lobby
        CheckLobby()
        closeEvent()
    except:
        print("error knock")
    print(dataReportConfig)
    reportKnock(dataReportConfig)
def collect(day):
    try:
        #join event
        eventWCOpen()
        #check progress
        prog1=checkProgressCurrent()
        closeEvent()
        #cheat gold du play
        cheatGold(user["user2"]["id"],1000000)
        #click btn play
        joinTable()
        #cheat cheatPorkerSpecial
        if challengePlay[challenge["day"+str(day)]["mission"]]["data"]["type"] == 'wc':
            CheatCard(cardCheat["wc"]["card"],cardCheat["wc"]["set"])
        #add bot
        addBot()
        #Click knock
        clickKnock()
        #cheat win finished game
        # cheatNumMision(1)
        #chon thoat table
        clickOutTable()
        #wait end game
        waitEndGame2()
        prog2=checkProgressCurrent()
        #check update progess
        if checkUpdateProgessTable(prog1,prog2):
            dataReportConfig["Update"]="Pass"
        else:
            dataReportConfig["Update"]="Fail"
           #check lobby
        CheckLobby()
    except:
        print("error collect")
    print(dataReportConfig)
    reportCollect(dataReportConfig)
def claimGift():
    # script content
    claimAll()
    closeAllEvent()
    #back to loby
    CheckLobby()
    #check gold init
    goldInit=getGold(user["user1"]["id"])
    #Cheat finished mission-----------------------
    if cheatFinishedMision(user["user1"]["id"],1):
        dataReportConfig['CheatFM']="Pass"
    else:
        dataReportConfig['CheatFM']="Fail"
    #---------reload lobby------------------------------
    reloadLobby()
    claimAll()
    #check GUI event
    if CheckGUIEvent():
        dataReportConfig['GuiEvent']="Pass"
    else:
        dataReportConfig['GuiEvent']="Fail"
        eventWCOpen()
    to1=checkTocos()
    #check gold claim
    goldClaim=challengePlay[challenge["day1"]["mission"]]["data"]["gold"]
    tocosConf=challengePlay[challenge["day1"]["mission"]]["data"]["tacos"]
    #click claim gift
    clickClaimMission()
    sleep(2)
    to2=checkTocos()
    #exit GUI event
    closeEvent()
    #check update gold
    goldAfter=getGold(user["user1"]["id"])
    if checkUpdateGold(goldClaim,goldInit,goldAfter):
        dataReportConfig['GoldUpdate']="Pass"
    else:
        dataReportConfig['GoldUpdate']="Fail"
    if checkTocosUpdate(tocosConf,to1,to2):
        dataReportConfig['UpdateTocos']="Pass"
    else:
        dataReportConfig['UpdateTocos']="Fail"
    #End in Game----------------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportClaimGift(dataReportConfig)
def noClaimGift():
    # script content
   #back to loby
    claimAll()
    closeAllEvent()
    CheckLobby()
#     poco("btnJoin")
    #check gold init
    goldInit=getGold(user["user1"]["id"])
    #Cheat finished mission-----------------------
    cheatFinishedMision(user["user1"]["id"],2)
    #---------reload lobby------------------------------
    reloadLobby()
    claimAll()
    closeNotiVip()
    claimAll()
    closeDealSpec1()
    #check GUI event
    if CheckGUIEvent():
        closeEvent()
    else:
        eventWCOpen()
        sleep(1)
        closeEvent()
    #check gold claim
    goldClaim=challengePlay[challenge["day2"]["mission"]]["data"]["gold"]
    #check update gold
    goldAfter=getGold(user["user1"]["id"])
    if checkUpdateGold(goldClaim,goldInit,goldAfter):
        dataReportConfig['GoldUpdate']="Fail"
    else:
        dataReportConfig['GoldUpdate']="Pass"
    #End in Game----------------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportNoClaimGift(dataReportConfig)
def passClaimGift(day):
    # script content
    #Change acc 1
    changeAcc(user["user1"]["user"],user["user1"]["pass"])
    #check GUI event
    if CheckGUIEvent():
        dataReportConfig['GUIEvent']="Pass"
    else:
        dataReportConfig['GUIEvent']="Fail"
        eventWCOpen()
    #checkAuto claim
    to1=checkTocos()
    sleep(5)
    to2=checkTocos()
    tocosConf=challengePlay[challenge["day"+str(2)]["mission"]]["data"]["tacos"]
    if checkTocosUpdate(tocosConf,to1,to2):
        dataReportConfig['UpdateTocos']="Pass"
    else:
        dataReportConfig['UpdateTocos']="Fail"
    #check tick claim day2
    if checkFinishMission(2):
        dataReportConfig['Tick']="Pass"
    else:
        dataReportConfig['Tick']="Fail"
    #checkUpdate mission
    if CheckMissionProgress(day):
        dataReportConfig["MissionNew"]="Pass"
    else:
        dataReportConfig["MissionNew"]="Fail"
    #exit GUI event
    #check update gold
    #End in Game----------------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportPassClaimGift(dataReportConfig)
def autoClaimGift():
    # script content
#     clickOutTable()
    #Check auto show GUI event
    if CheckGUIEvent():
        dataReportConfig['GuiEvent']="Pass"
    else:
        dataReportConfig['GuiEvent']="Fail"
        eventWCOpen()
    #Check effect claim gift
    to1=checkTocos()
    sleep(5)
    to2=checkTocos()
    tocosConf=challengePlay[challenge["day2"]["mission"]]["data"]["tacos"]
    if checkTocosUpdate(tocosConf,to1,to2):
        dataReportConfig['Effect']="Pass"
    else:
        dataReportConfig['Effect']="Fail"
    #check đánh dấu nhận thưởng 2
    if checkFinishMission(2):
        dataReportConfig['Tick']="Pass"
    else:
        dataReportConfig['Tick']="Fail"
    #check update nhiem vu ngay 3
    #Show update mission
    if CheckMissionProgress(3):
        dataReportConfig["MissionNew"]="Pass"
    else:
        dataReportConfig["MissionNew"]="Fail"
    #End in Game----------------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportAutoClaim(dataReportConfig)
def CheckChangeAcc():
     # script content
    #change acc
    claimAll()
    closeAllEvent()
    changeAcc(user["user2"]["user"],user["user2"]["pass"])
    claimAll()
    closeAllEvent()
    #open Gui
    eventWCOpen()
    #check nv day 1
    if checkMissedMission(1):
        dataReportConfig['MissionDay1']="Pass"
    else:
        dataReportConfig['MissionDay1']="Fail"
    #exit GUI event
    closeEvent()
    #End in Game----------------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportChangeAcc(dataReportConfig)
def missionPassDayInTable(day):
    claimAll()
    closeAllEvent()
    timeCheat = api_changeTimeServer(1605051600000)
    #cheat time pass 1 ngay-> 27/11/2020 23:59:00 -> 1606496340000
    dayS = {
        "Y": timeWC["start"]['Y'],
        "M": timeWC["start"]['M'],
        "D": timeWC["start"]['D'],
        "h": timeWC["start"]['h'],
        "m": timeWC["start"]['m'],
        "s": timeWC["start"]['s']
    }
    timeNow= convertDayTimeToMili(dayS) + datetoMili(2) - housToMili(1) + minutetoMili(59) 
    timeCheat = api_changeTimeServer(timeNow)
    #reload lobby
    reloadLobby()
    claimAll()
    closeNotiVip()
    claimAll()
    closeDealSpec1()
    #check GUI event
    if CheckGUIEvent():
        closeEvent()
    #click btn play
    joinTable()
    #add bot
    addBot()
    #play wait pass day
    for x in range(2):
        clickPass()
    #Show update mission
    if CheckMissionProgress(day+1):
        dataReportConfig["MissionNew"]="Pass"
    else:
        dataReportConfig["MissionNew"]="Fail"
    #Click out table
    clickOutTable()
    #Click knock
    clickKnock()
    #wait end game
    waitEndGame()
    #------------------------#
    #report
    reportUpdateMissionTable(dataReportConfig)
def missionPassDayOpenGui(day):
    to1=0
    to2=0
    #Cheat finished mission
#     cheatFinishedMision(user["user2"]["id"],3)
    reloadLobby()
    timeCheat = api_changeTimeServer(1605051600000)
    #cheat time pass 1 ngay-> #28/11/2020 23:59:00 -> 1606582740000
    dayS = {
        "Y": timeWC["start"]['Y'],
        "M": timeWC["start"]['M'],
        "D": timeWC["start"]['D'],
        "h": timeWC["start"]['h'],
        "m": timeWC["start"]['m'],
        "s": timeWC["start"]['s']
    }
    timeNow= convertDayTimeToMili(dayS) + datetoMili(day) - housToMili(1) + minutetoMili(59)+secToMili(40) 
    timeCheat = api_changeTimeServer(timeNow)
    #reload lobby
    reloadLobby()
#     clickClaim()
#     closeEvent()
    if CheckGUIEvent()==False:
        eventWCOpen()
    sleep(3)
    to1=checkTocos()
#     sleep(2)
#     to1=checkTocos()
#     waitTimePassDay(dayS,Y,M,D,h,m,s)
    sleep(25)
    to2=checkTocos()
    #Show update mission
    tocosConf=challengePlay[challenge["day"+str(day)]["mission"]]["data"]["tacos"]
    if checkTocosUpdate(tocosConf,to1,to2):
        dataReportConfig['Effect']="Pass"
    else:
        dataReportConfig['Effect']="Fail"
    if CheckMissionProgress(day+1):
        dataReportConfig["MissionNew"]="Pass"
    else:
        dataReportConfig["MissionNew"]="Fail"
    #------------------------#
    #report
    print(dataReportConfig)
    reportUpdateMissionLobby(dataReportConfig)
def UpdateProgressMissionFull():
    data1 = {
      "UpdateFull": "Fail",
      "UpdateAgain": "Fail",
    }
    #cheat gan hoan thanh nhiem vu
    cheatNumMision(challengePlay[challenge["day4"]["mission"]]["data"]["totalX"]-1,user["user1"]["id"])
    reloadLobby()
    eventWCOpen()
    prog1=checkProgressCurrent()
    closeEvent()
    checkMission2("day4")
    #check update progess
    if waitNolimitPoco(pocoTag.btnMain,1):
        pocoTag.btnMain.click()
    prog2=checkProgressCurrent()
    if checkUpdateProgessTable(prog1,prog2):
        dataReportConfig["UpdateFull"]="Pass"
    else:
        dataReportConfig["UpdateFull"]="Fail"
    clickOutTable()
    eventWCOpen()
    prog3=checkProgressCurrent()
    closeEvent()
    checkMission2("day4")
    #check update progess
    if waitNolimitPoco(pocoTag.btnMain,1):
        pocoTag.btnMain.click()
    prog4=checkProgressCurrent()
    if checkUpdateProgessTable(prog3,prog4):
        dataReportConfig["UpdateAgain"]="Pass"
    else:
        dataReportConfig["UpdateAgain"]="Fail"
    #------------------------#
    #report
    reportUpdateProgressMissionFull(dataReportConfig)
def checkDisconect():
    killApp()
    openApp()
    sleep(15)
    checkProgress()
    clickOutTable()
def GuiDeal():
    dataReportConfig['Login']="Fail"
#     if  changeAcc(user["user1"]["user"],user["user1"]["pass"]):
#         dataReportConfig['Login']="Fail"
#     else:
#         dataReportConfig['Login']="Pass"
    if  CheckGUIEvent() :
        dataReportConfig['GuiEvent']="Fail"
        closeEvent()
    else:
        dataReportConfig['GuiEvent']="Pass"
#     close Gui Event
#     if waitNolimitPoco(poco("btnClaim"),2):
#         poco("btnClaim").click()
    if  CheckGUIDeal():
        dataReportConfig['GuiEDeal']="Pass"
        closeEvent()
    else:
        dataReportConfig['GuiEDeal']="Fail"
    gold1=getGold(user["user"]["id"])
    clickGuiDeal()
    cheatBuyDeal(user["user"]["id"],1)
    clickClaim()
    if checkDisableBtnDeal():
        dataReportConfig['BtnBuyWC']="Fail"
    else:
        dataReportConfig['BtnBuyWC']="Pass"
    closeEvent()
    gold2=getGold(user["user"]["id"])
    if checkUpdateGoldDeal(dealWCConfig["offerWC1"],gold1,gold2):
        dataReportConfig['GoldUpdate']="Pass"
    else:
        dataReportConfig['GoldUpdate']="Fail"
    clickGuiDeal()
    cheatBuyDeal(user["user"]["id"],2)
    clickClaim()
    sleep(1)
    cheatBuyDeal(user["user"]["id"],3)
    clickClaim()
    if checkBtnDeal():
        dataReportConfig['BtnDeal']="Fail"
    else:
        dataReportConfig['BtnDeal']="Pass"
    #report
    reportDeal(dataReportConfig)
def endEvent():
    #change Accout 1
    changeAcc(user["user1"]["user"],user["user1"]["pass"])
    claimAll()
    closeAllEvent()
    #Cheat time-------------#02/12/2020 23:59:00 -> 1606928340000
    timeCheat = api_changeTimeServer(1605051600000)
#     timeCheat = api_changeTimeServer(timeC["timeD0"]["mili"])
    dayS = {
        "Y": timeWC["end"]['Y'],
        "M": timeWC["end"]['M'],
        "D": timeWC["end"]['D'],
        "h": timeWC["end"]['h'],
        "m": timeWC["end"]['m'],
        "s": timeWC["end"]['s']
    }
    timeNow=convertDayTimeToMili(dayS) -housToMili(1)+ minutetoMili(59)+secToMili(30)
    timeCheat = api_changeTimeServer(timeNow)
#     dataReportConfig["TimeCheat"]=fortmartTime(dayS)
    #End Cheatime---------------------------------------
    #---------reload lobby------------------------------
    reloadLobby()
    claimAll()
    closeAllEvent()
    #---------end reload lobby--------------------------
    #check gold init
    goldInit=getGold(user["user1"]["id"])
    sleep(1)
    #opent GUI event
    eventWCOpen()
    #check gold claim
    goldClaim=challengePlay[challenge["day7"]["mission"]]["data"]["gold"]
    #wait pass day
    sleep(30)
    #check close GUI
    if CheckGUIEvent():
        dataReportConfig['GUIEvent']="Fail"
    else:
        dataReportConfig['GUIEvent']="Pass"
    #check gold
    goldAfter=getGold(user["user1"]["id"])
    if checkUpdateGold(goldClaim,goldInit,goldAfter):
        dataReportConfig['UpdateGold']="Fail"
    else:
        dataReportConfig['UpdateGold']="Pass"
    #End in Game----------------------------------------
    #Check btn event -----------------------------------
    if CheckBtnEvent():
        dataReportConfig["Button"]="Fail"
    else:
        dataReportConfig["Button"]="Pass"
    #end Check btn event--------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportEndEvent(dataReportConfig)
#mission
def win(day):
    try:
#         closeEvent()
         #cheat gold khong du play
        cheatGoldEmpty(1) 
        sleep(2)
        #open event
        eventWCOpen()
        prog1=checkProgressCurrent()
        sleep(2)
        #click btn play
        joinMission()
        #check noti
        if checkNotiNoEnoughGold():
            dataReportConfig["noPlay"]="Pass"
        else:
            dataReportConfig["noPlay"]="Fail"
        closeEvent()
        #cheat gold du play
        cheatGold(user["user"]["id"],1000000)
        reloadLoby2()
        #open event
        eventWCOpen()
        #click btn play
        sleep(2)
        joinMission()
        #check progess table
        if checkShowProgessTable():
            dataReportConfig["Progess"]="Pass"
        else:
            dataReportConfig["Progess"]="Fail"
        #Check table
        if tableGame():
            dataReportConfig["onPlay"]="Pass"
        else:
            dataReportConfig["onPlay"]="Fail"
        #cheat cheatPorkerSpecial
        CheatCard(cardCheat[challengePlay[challenge[day]["mission"]]["data"]["type"]]["card"], cardCheat[challengePlay[challenge[day]["mission"]]["data"]["type"]]["set"])
        #add bot
        addBot()
        #wait luot ban than
        #Click knock
        clickKnock()
        #chon thoat table
#         clickOutTable()
        #wait end game
        waitEndGame2()
        prog2=checkProgressCurrent()
        #check update progess
        if checkUpdateProgessTable(prog1,prog2):
            dataReportConfig["Update"]="Pass"
        else:
            dataReportConfig["Update"]="Fail"
        CheatCard(cardCheat["lose"]["card"], cardCheat["lose"]["set"])
        sleep(10)
        clickKnock()
        #chon thoat table
        clickOutTable()
        #wait end game
        waitEndGame()
        prog3=checkProgressCurrent()
        #check update progess
        if checkUpdateProgessTable(prog2,prog3):
            dataReportConfig["Update1"]="Pass"
        else:
            dataReportConfig["Update1"]="Fail"
#         clickOutTable()
        #check lobby
        CheckLobby()
        print("fc win")
    except:
        print("error win")
    print(dataReportConfig)
    reportWin(dataReportConfig)
def win1():
    try:
        reloadLoby2()
        #click btn play
        sleep(2)
        joinTable()
        #cheat cheatPorkerSpecial
        #add bot
        addBot()
        #Click knock
        clickKnock()
        clickOutTable()
        #wait end game
        waitEndGame()
    except:
        print("error win")
def lose1():
    try:
        reloadLoby2()
        #click btn play
        sleep(2)
        joinTable()
        #add bot
        addBot()
        #Click knock
        clickKnock()
        #wait end game
        waitEndGame()
    except:
        print("error win")
    #------------------#
    #check
def CheckBtnEvent():
    try:
#         if waitNolimitPoco(poco("btnMain"),10):
        if waitNoLimit(imageWC.imgBtnEvent,5):
            return True
        else:
            return False
    except:
        print("error btn event")
        return False
def CheckNotiEvent():
    try:
        if notiShow.attr("type")=="ImageView":
            print("check noti event")
            return True
        else:
            print("check noti event no exists")
            return False
    except:
        print("check noti event no exists")
        return False
def coutDownTime():
    cout=65
    while 1:
        sleep(1)
        cout-=1
        time=pocoTag.lbTime.attr("text")
        print(time)
        if time=="Abierto en: 00:00:-01":
            print("Error coutdown time")
            return 0
            break
        if time=="6 días":
            print("Pass coutdown time")
            return 1
            break
        if cout==0:
            if time!="6 días":
                print("Error coutdown time")
                return 0
                break
def coutDownTimeIntable():
    cout=20
    while 1:
        sleep(1)
        cout-=1
        if cout==0 or cout<0:
            print("Error coutdown time")
            return False
            break
        if exists1(pocoTag.btnMain):
            print("show")
            return True
            break
def checkMission(day):
    if challenge[day]["mission"]=="win":
        return win(day)
    if challenge[day]["mission"]=="play":
        return play(day)
    if challenge[day]["mission"]=="knock":
        return knock(day)
    if challenge[day]["mission"]=="exchange1":
        return exchange1(day)
    if challenge[day]["mission"]=="collect":
        return collect(day)
def checkMission2(day):
    if challenge[day]["mission"]=="win":
        return win1()
    if challenge[day]["mission"]=="play":
        return "play"
    if challenge[day]["mission"]=="knock":
        return "knock"
    if challenge[day]["mission"]=="exchange1":
        return "exchange1"
def checkDisableBtnDeal():
    try:
        if waitNolimitPoco(pocoTag.btnOfferEventTB,1):
            print("check CheckGUIDeal")
            return False
        else:
            return True
    except:
        print("check CheckGUIDeal no exists")
        return True 
def checkNotiNoEnoughGold():
    try:
        if waitNolimitPoco(pocoTag.NOTIFICACIONES,5):
            print('Noti no enough gold')
            poco.click([0.49964862965565704, 0.6496874809265136])
            return True
        else:
            print('no show Noti no enough gold')
            return False
    except:
        print("error show enough gold")
        return False
def CheckMissionProgress(day):
    try:
        if CheckGUIEvent()==False:
            pocoTag.btnMain.click()
        elif waitNolimitPoco(challengePlay[challenge["day"+ str(day)]["mission"]]["data"]["detailMission"],5):
            print(challengePlay[challenge["day"+ str(day)]["mission"]]["data"]["detailMission"])
            print("Progess update")
            return True
        else:
            print("Progess no update")
            return False
    except:
        print("error checkUpdateProgess")
        return False
def checkProgressCurrent():
    try:
        poco = CocosJsPoco()
        progress=""
        if waitNolimitPoco(pocoTag.lbProgress,2):
#             progress=pocoTag.lbProgress.get_text()
            progress=poco("lbProgress").get_text()    
            prg=progress.split("/")
            prgL=int(prg[0].strip())
            prgR=int(prg[1].strip())
            print("Progess checkProgressCurrent"+progress)
            return prgL
        else:
            print("NO find progress")
            return False
    except:
        print("error checkProgressCurrent")
        return False
def checkProgress():
    try:
        if waitNolimitPoco(pocoTag.lbProgress,5):
            print("Progess checkProgressCurrent")
            return True
        else:
            print("NO find progress")
            return False
    except:
        print("error checkProgressCurrent")
        return False
def checkProgessTable():
    try:
        if waitNolimitPoco(pocoTag.btnMain,5):
            print("Progess table")
            return 1 
        else:
            print("Progess no show table")
            return 0
    except:
        return 0 
        print("error Progess table")
def checkShowProgessTable():
    try:
        if waitNoLimit(imageWC.imgProgessBarON,10):
            print("Progess show on table")
            return True 
        else:
            print("Progess no show on table")
            return False
    except:
        return False 
        print("error Progess table")
def checkUpdateProgessTable(prg1,prg2):
    try:
        print(prg1)
        print(prg2)
        if (prg2-prg1) > 0 :
            print("Progess update")
            return True
        else:
            print("Progess no update")
            return False
    except:
        print("error checkUpdateProgessTable")
        return False
def CheckGUIEvent():
    try:
        if waitNolimitPoco(pocoTag.imgTruck,5):
            print("check CheckGUIEvent")
            return True
        else:
            return False
    except:
        print("check CheckGUIEvent no exists")
        return False
def CheckGUIDeal():
    try:
        if waitNoLimit(imageWC.imgDeal,5):
            print("check CheckGUIDeal")
            return True
        else:
            return False
    except:
        print("check CheckGUIDeal no exists")
        return False
def CheckLableDay():
    try:
        if waitNolimitPoco(pocoTag.lbDay1,1):
               print("Día 1")
        else:
            if waitNolimitPoco(pocoTag.lbDayCurrent,1):
                return 1
            else:
                return False
        if waitNolimitPoco(pocoTag.lbDay2,1):
            print("Día 2")
        else:
            if waitNolimitPoco(pocoTag.lbDayCurrent,1):
                return 2
            else:
                return False
        if waitNolimitPoco(pocoTag.lbDay3,1):
            print("Día 3")
        else:
            if waitNolimitPoco(pocoTag.lbDayCurrent,1):
                return 3
            else:
                return False
        if waitNolimitPoco(pocoTag.lbDay4,1):
            print("Día 4")
        else:
            if waitNolimitPoco(pocoTag.lbDayCurrent,1):
                return 4
            else:
                return False
        if waitNolimitPoco(pocoTag.lbDay5,1):
            print("Día 5")
        else:
            if waitNolimitPoco(pocoTag.lbDayCurrent,1):
                return 5
            else:
                return False
        if waitNolimitPoco(pocoTag.lbDay6,1):
            print("Día 6")
        else:
            if waitNolimitPoco(pocoTag.lbDayCurrent,1):
                return 6
            else:
                return False   
        if waitNolimitPoco(pocoTag.lbDay7,1):
            print("Día 7")
        else:
            if waitNolimitPoco(pocoTag.lbDayCurrent,1):
                return 7
            else:
                return False
    except:
        return False
def checkTocos():
    try:
        if waitNolimitPoco(pocoTag.lbNumTacos,2):
#             tocos=int(pocoTag.lbNumTacos.get_text())
            tocos=int(poco("lbNumTacos").get_text())
            return tocos
    except:
        return False
def checkTocosUpdate(to1,to2,to3):
    try:
        print(to1)
        print(to2)
        print(to3)
        to=to3-to2
        if to1==to:
            print("check checkTocosUpdate")
            return True
        else:
            return False
    except:
        print("check checkTocosUpdate error" )
        return False 
def checkUpdateGold(gold1, gold2, gold3):
    try:
        print(gold1)
        print(gold2)
        print(gold3)
        claim= float(gold1)
        update= gold3 - gold2
        print(claim)
        print(update)
        if update == claim :
            print("Gold update")
            return True
        else:
            print("gold update false")
            return False
    except:
        print("Gold update error")
        return False
def checkMissedMission(day):
    try:
        mission="TBNodeDay"+str(day)
        if waitNolimitPoco(poco(mission),2):
            return poco(mission).offspring("imgMissed").attr("visible")
        else:
            return False
    except:
        return False
def checkFinishMission(day):
    try:
        mission="TBNodeDay"+str(day)
        if waitNolimitPoco(poco(mission),5):
            return poco(mission).offspring("imgClaimed").attr("visible")
        else:
            return False
    except:
        return False
#action
def eventWCOpen():
    try:
        poco = CocosJsPoco()
        if waitNolimitPoco(pocoTag.btnMain,5):
            pocoTag.btnMain.click()
            print("event WC")
            return True
    except:
        print("error event WC")
        return False
def clickClaimMission():
    try:
        if waitNolimitPoco(pocoTag.btnJoin,1):
            pocoTag.btnJoin.click()
            return True
        else:
            return False
    except:
        return False
def joinMission():
    try:
        poco = CocosJsPoco()
        pocoTag.btnJoin.click()
        return True
    except:
        return False
def clickGuiDeal():
    try:
        if waitNolimitPoco(pocoTag.btnOfferEventTB,10):
            pocoTag.btnOfferEventTB.click()
            return True
        else:
            return False
    except:
        return False
def closeDealSpec():
    try:
        if waitNoLimit(imageWC.imgEventSpec,2):
            pocoTag.btnClose.click()
            return True
        else:
            return False
    except:
        return False
def closeDealSpec1():
    try:
        if waitNoLimit(imageWC.imgDealSpec,2):
            poco("btnClose").click()
            return True
        else:
            return False
    except:
        return False
def closeNotiVip():
    try:
        if waitNoLimit(imageWC.imgVipBag,1):
            pocoTag.btnClose.click()
            return True
        else:
            return False
    except:
        return False
#-------------------------------------------------------------------------------------#
def gold_number():
    gold=pocoTag.lbGold.get_text()
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
def log_in():
    poco = CocosJsPoco()
    poco("btnSwitch").exists()
    poco("btnGuest").click()
def log_out():
    data= {
        "status": "False"
    }
    try:
        poco("btnPlay").exists
    except:
        print("Please back to lobby page!")
    else:
        print("Success!")
    poco("iconSetting").click()
    poco("bgLobbyLayer2").click()
    touch(imageInOutAcc.imgOutOk)
    data["status"]="True"
    reportdailybonus(data)
def log_in_gg():
    poco = CocosJsPoco()
    pocoTag.btnGooglePlus.exists()
    pocoTag.btnGooglePlus.click()  
def log_in_FB():
    time.sleep(3)
    pocoTag.btnFacebookNormal.click()
    time.sleep(5)
#2.2 Register_thường
def register():
    data= {
        "status": "False"
    }
    pocoTag.btnSwitch.click()
    pocoTag.inputUser.click()
    text("ngocnn75")
    pocoTag.inputPass.click()
    text("12345678")
    pocoTag.btnRegister.click()  
#play tutorial
def play_tutorial():
    if pocoTag.btnCallBack.exists():
        pocoTag.btnCallBack.click()
        pocoTag.btnSkip.click()
        time.sleep(2)
        Daily_bonus.btn_out_tutorial.click()
    else:
        print("Dont show tutorial after register")
        time.sleep(3)
# Nhận dailybonus của ngày đầu tiên
#def close_even():
def btn_claim_exit(btn):
    try:
        return btn.attr('visible')
    except:
        return 0
    else:
        print("12345")
def bonus_day_1():
    data= {
        "status": "False"
    }
    try: 
        btn_claim_exit(pocoTag.btnClaim)==True
    except:    
        print("khong auto show Gui daily bonus sau play tutorial")
    else:
        data["status"]="true"
        time.sleep(5)
        pocoTag.btnClaim.click()  
        pocoTag.btnClaim.click()
        print("nhan gold day 1 success!")
    reportdailybonus(data)
#kiểm tra có auto về lobby sau khi click claim nhận bonus
def check_lobby():
    try:
        pocoTag.btnPlay.exists()
    except:
        print("dont auto back lobby sau khi claim bonus")
    else:
        print("Auto show back to lobby page after claim bonus")
# 1. check có đang ở log_in screen hay ko
def check_login():
    data= {
        "status": "False"
    }
    
    if pocoTag.btnSwitch.exists():
        data["status"]="true"
        print("check in lobby!")
    else:
        print ("Please go to Login page")
    reportdailybonus(data)
#7. Kiểm tra có show GUI daily bonus ko, Nhận bonus
def claim_bonus():
    data= {
        "status": "False"
    }
    time.sleep(3)
    try:
        btn_claim_exit(pocoTag.btnClaim)==True
    except:
        print("Dont show GUI bonus day2")
        data["status"]="False"
    else:
        data["status"]="True"
        pocoTag.btnClaim.click()
        print("Nhan bonus day2 success!")
    reportdailybonus(data)
#9. Kiểm tra có show GUI daily bonus khi dung o lobby cho nhan bonus
def check_show_GUI():
    api_changeTimeServer(1608796800000)
    if btn_claim_exit(pocoTag.btnClaim)==True:
        print("Auto show GUi daily bonus khi o lobby sau24h!")
    else:
        print("Khong auto show GUI daily bonus o lobby sau 24h")
#Vao lại Gui daily bonus
def into_gui_bonus():
    time.sleep(3)
    pocoTag.btnDaily.click()
    pocoTag.btnTomorrow.exists()
    pocoTag.btnTomorrow.click()
    pocoTag.btnPlay.exists()
#10. Log out-> vào lại sau 23h
def Logout_login_23h():
    log_out()
    api_changeTimeServer(1608879600000)
    time.sleep(3)
    log_in_FB()
    data= {
        "status": "False"
    }
    time.sleep(5)
    try:
        return pocoTag.btnClaim.attr('visible')
    except:
        data["status"]="True"
        print("Ko Show GUI khi chuwa ddur 24h!")
    else:
        pocoTag.btnClaim.click()
        time.sleep(3)
        data["status"]="False"
        print("Show daily GUI daily bonus khi chua du 24h")
    reportdailybonus(data)
    time.sleep(3)
#11. Vao playinggame-> ra lại lobby
def playing_23h():
    data= {
        "status": "False",
    }
    pocoTag.btnPlay.click()
    api_changeTimeServer(1608882000000)
    pocoTag.btnLeaveGame.click()       #leave khi chưa đủ 24h
    time.sleep(1)
    if btn_claim_exit(pocoTag.btnClaim)==True:
        pocoTag.btnClaim.click()
        data["status"]="False"
        print("Show GUI bonus khi leave tuwf playing chuwa ddur 24h")
    else:
        print("playing->lobby: Khong show GUI daily bonus khi chua du 24h")
        time.sleep(3)
        data["status"]="True"
    reportdailybonus(data)
#12. Vào playing game-> Chờ qua 24h rồi ra lại lobby( Ngày 4)
def playing_24h():
    data= {
        "status": "False",
    }
    time.sleep(3)
    pocoTag.btnPlay.click()
    api_changeTimeServer(1608883200000)
    time.sleep(3)
    pocoTag.btnLeaveGame.click()
    time.sleep(4)
    if pocoTag.btnClaim.exists():
        print("show GUI daily bonus day 4 Success!")
        data["status"]="True"
    else:
        print("Khong show GUI daily BONUS khi playing ra lobby sau 24h")
        data["status"]="False"
    reportdailybonus(data) 
#14. Đứng chờ ở GUI daily bonus 23h
def GUI_bonus_23h():
    data= {
        "status": "False",
    }
    reloadLobby()
    pocoTag.btnDaily.click()
    api_changeTimeServer(1608966000000)
    if pocoTag.btnClaim.exists():
        print("Show daily bonus khi o GUI daily bonus sau 23h")
        data["status"]="False"
    else:
        print("Khong show GUI daily bonus khi o gui daily bonus chua du 24h")
        data["status"]="True"
#16 Nhận bonus 5 lần-> Log out-> Login sau 24h nhưng không nhận bonus->Login lại sau 24h tiếp theo
def claim_kill_login_24h():
    data= {
        "status": "False"
    }
    time.sleep(3)
    if pocoTag.btnClaim.exists():
        print("Show daily bonus day 5 Success!")
        pocoTag.btnClaim.click()
    else:
        time.sleep(3)
        pocoTag.btnTomorrow.click()
        print("Koo auto show daily bonus khi o GUI daily bonus sau 24h")
    reportdailybonus(data)
    time.sleep(2)
    log_out()
    api_changeTimeServer(1609056000000)
    time.sleep(2)
    log_in_FB()
#kill app vào lại sau 24h
# kill_app()
# start_app()
    if pocoTag.btnClaim.exists():
        print("Show GUI khi kill app ko nhaan cuar ngay trc!")
    else:
        print("Không auto show daily bonus khi khong nhan bonus cua ngay truoc") 
    api_changeTimeServer(1609142400000)
#check an btn Daily bonus ở lobby khi đã nhận đủ 7 lần
def complete_icon_bonus_lobby():
    if pocoTag.btnDaily.exists():
        print("Van show icon Daily bonus o lobby khi da nhan du 7 lan")
    else:
        print("hide Daily bonus btn khi nhan dur 7 lan success")
#19. Ra lại lobby-> đứng ở lobby chờ sau 24
def complete_lobby_24h():
    api_changeTimeServer(1609315200000)
    if pocoTag.btnClaim.exists():
        print("Show daily bonus khi da nhan du 7 lan")
    else:
        print("Khong show daily bonus khi nhan du 7 lan o lobby!")
#20. Log out-> Login lại sau 24h
def complete_logout_login_24h():
    log_out()
    api_changeTimeServer(1609401600000)
    log_in_FB()  
    if pocoTag.btnClaim.exists():
        print("Show daily bonus khi da nhan 7 lan")
    else:
        print(" khong show GUI daily bonus khi da nhan du 7 lan!")
    print(" khong show GUI daily bonus khi da nhan du 7 lan!")
    # check_login()
    #2. đăng kí thường
    register()     
                     #Play tutorial---------------------------------------
    time.sleep(3)
    bonus_day_1()
    check_lobby()
    #3. Log out-> Log in sau 24h
    log_out()
    time.sleep(3)
    api_changeTimeServer(1608624000000)
    time.sleep(3)
    log_in_FB()
    time.sleep(3)
    #5. Nhận bonus lần 2
    claim_bonus()
    #6. Check có đang ở lobby hay không
    check_lobby()
    #7.Kiểm tra có show GUI daily bonus khi dung o lobby cho nhan bonus,nhân bonus 
    claim_bonus()
    #9. Vao lại Gui daily bonus
    into_gui_bonus()
    #10. Log out-> vào lại sau 23h
    Logout_login_23h()
    #11. Vao playinggame-> ra lại lobby
    playing_23h()
    #12. Vào playing game-> Chờ qua 24h rồi ra lại lobby( Ngày 4)
    playing_24h()
    #13. Click nhận bonus của ngày 4
    claim_bonus()
    #14. Đứng chờ ở GUI daily bonus 23h
    GUI_bonus_23h()
    #15. Tiếp tục đứng ở GUI daily bonus chờ thêm 1h( ngày 5)
    api_changeTimeServer(1608969600000)
    #16 Nhận bonus 5 lần-> Log out-> Login sau 24h nhưng không nhận bonus->Login lại sau 24h tiếp theo
    claim_kill_login_24h()
    #17 Click nhận bonus của ngày 6
    claim_bonus()
    #18 Nhận bonus lần thứ 7
    api_changeTimeServer(1609228800000)
    claim_bonus()
    #check an btn Daily bonus ở lobby khi đã nhận đủ 7 lần
    complete_icon_bonus_lobby()
    #19. Ra lại lobby-> đứng ở lobby chờ sau 24
    complete_lobby_24h()
    #20. Log out-> Login lại sau 24h
    complete_logout_login_24h()

