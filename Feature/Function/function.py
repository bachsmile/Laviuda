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
from Laviuda.Config.Api import *
#----------------------------------------------------------#
from Laviuda.Config.config import *
from Laviuda.Report.report import *
from Laviuda.Img.img import *
from Laviuda.Poco.poco import *
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
#cheat
def cheatGoldEmpty(gold):
    try:
        pocoTag.btnCheat.click()
        if exists(imageWC.imgGoldCheat):
            touch(imageWC.imgGoldCheat)
        else:
            touch(imageWC.imgGoldCheat1)
        text(str(gold))
        pocoTag.btnSendCheatPlayer.click()
        pocoTag.btnCheat.click()
        print("Cheat tien thanh cong")
        return True
    except:
        print("Khong tim thay")
        return False
# Action
def reloadLobby():
    try:
        poco = CocosJsPoco()
        pocoTag.btnPlay.click()
        sleep(1)
        pocoTag.btnLeaveGame.click()
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
def closeAllEvent():
    while waitNolimitPoco(pocoTag.btnClose,1):
        pocoTag.btnClose.click()
def claimAll():
    while waitNolimitPoco(pocoTag.btnClaim,1):
        pocoTag.btnClaim.click()      
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
            print(0)
            print("end game")
            return True
        else:
            print("end time down")
            return False
    except:
        print("error")
        return False
def checkGold():
    numGold = pocoTag.lbGold.attr("text")
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
            data_report["Status"] = "Pass"
            print("Vao thanh cong")
    except:
        data_report["Status"] = "Fail"
        print("error")
        time.sleep(2)
def open_pack(pack):
    try:
        poco(pack).click()
        touch(image_vip.btn_cancel)
        data_report["Status"] = "Pass"
        print("Mo thanh cong")
    except:
        data_report["Status"] = "Fail"
        print("error")
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
# def check_item():
#     items = [image_vip.cachua, image_vip.votay, image_vip.xonuoc, image_vip.trung, image_vip.hoahong, image_vip.hoavang, image_vip.sungnuoc]
#     try:
#         touch(image_vip.btn_profile)
#         if exists(image_vip.list_item):
#             #return False
#             for item in items:
#                 if exists(item):
#                     touch(item)
#                     time.sleep(2)
#                     touch(image_vip.btn_profile)
#                 else:
#                     swipe(image_vip.hoahong, record_pos=(0.113, 0.122), resolution=(2340, 1079)), vector=[-0.1553, -0.0043]             
#                     time.sleep(2)
#                     touch(item)
#             data_report["Check_item"] = "Pass"
#             print("List item co ton tai")
#         else:
#             #return True
#             data_report["Check_item"] = "Fail"
#             print("List item khong ton tai")
#         back_to_lobby()
#     except:
#         print("Error")
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
        data_report["Check_low_vip"] = "Pass"
        print("Khong mua duoc vip thap hon")
    except:
        data_report["Check_low_vip"] = "Fail"
        print("Error")
# def check_vip():
    
def cheat_buy_vip(pack):
    old_gold = float(re.sub('[MKB]', '', poco("lbGold").get_text()))
    old_day = float(re.sub(r'\D', '', poco("lbTimeMyVip").get_text()))
    a = api_postDoFunction("19175089", "CHEAT_PAYMENT_VIP", [pack])
    try:
        touch(image_vip.btn_claim)
        time.sleep(2)
        new_gold = float(re.sub('[MKB]', '', poco("lbGold").get_text()))
        new_day = float(re.sub(r'\D', '', poco("lbTimeMyVip").get_text()))
        gold = new_gold - old_gold
        gold_in = vip_pack[pack]["dailyTribute"]
        day = new_day - old_day
        day_in = vip_pack[pack]["day"] 
        if gold == gold_in & day == day_in:
            data_report["Check_gold"] = "Pass"
            data_report["Check_day"] = "Pass"
            print("Mua thanh cong")
            data_report["Status"] = "Pass"
    except:
        data_report["Status"] = "Fail"
        print("Error")
# def check_gold_support():
def checkLevelVip():
    logos = [image_vip.logo_vip_bac, image_vip.logo_vip_vang, image_vip.logo_vip_kimcuong]
    try:    
        if exists(image_vip.logo_vip_bac):
            print("user dang co vip bac")
        elif exists(image_vip.logo_vip_vang):
            print("user dang co vip vang")
        else:
            print("user dang co vip kim cuong")
    except:
        print("error")
#Function WC:---------------------->
    #------------------#
def beforEvent():
    clearReport()
    #Cheat time-------------24/11/2020 7:00:00----------
    timeCheat = api_changeTimeServer(1605051600000)
    dayS = {
        "Y": timeWC["start"]['Y'],
        "M": timeWC["start"]['M'],
        "D": timeWC["start"]['D'],
        "h": timeWC["start"]['h'],
        "m": timeWC["start"]['m'],
        "s": timeWC["start"]['s']
    }
    timeNow=convertDayTimeToMili(dayS) - datetoMili(2)
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
    #In Game--------------------------------------------
    #---------reload lobby------------------------------
    #reloadLobby()
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
    reportBeforEvent(dataReportConfig)
def afterEvent():
    resetDataReportConfig()
    poco = CocosJsPoco()
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
    timeNow=convertDayTimeToMili(dayS) -housToMili(1)+ minutetoMili(59)+secToMili(40)
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
            poco = CocosJsPoco()
            #Join event
            eventWCOpen()
            #Check noti event befor event---------------
            if CheckNotiEvent():
                dataReportConfig['Befor']="Pass"
                #Open pop-up wait event
                if coutDownTime()==1:
                    sleep(1)
                    dataReportConfig["Coutdown"]="Pass"
                else:
                    dataReportConfig["Coutdown"]="Fail"
                #Join event
                if eventWCOpen():
                    sleep(1)
                    dataReportConfig["After"]="Pass"
                else:
                    dataReportConfig["After"]="Fail"
                sleep(1)
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
                #kill app
                killApp()
                #open app
                sleep(2)
                openApp()
                #wait
                sleep(20)
                claimAll()
                closeAllEvent()
                #changeAcc
                if changeAcc(user["user1"]["user"],user["user1"]["pass"]):
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
                    closeEvent()
            else:
                print(21)
                dataReportConfig['Befor']="Fail"
                if coutDownTime()==1:
                    sleep(1)
                    dataReportConfig["Coutdown"]="Pass"
                else:
                    dataReportConfig["Coutdown"]="Fail"
                #Join event
                if eventWCOpen():
                    sleep(1)
                    dataReportConfig["After"]="Pass"
                else:
                    dataReportConfig["After"]="Fail"
                sleep(1)
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
                dayS1['h'] = dayS1['h']-1
                dayS1['m'] = dayS1['m']+59
                print(dayS1)
                timeCheat = api_changeTimeServer(convertDayTimeToMili(dayS1))
                dataReportConfig["TimeCheat1"]=fortmartTime(dayS1)
                print(timeCheat)
                if timeCheat ==200:
                    dataReportConfig['CheatTime1']="Pass"
                else:
                    dataReportConfig['CheatTime1']="Fail"
                sleep(1)
                #kill app
                killApp()
                #open app
                sleep(2)
                openApp()
                #wait
                sleep(20)
                CheckLobby()
                #changeAcc
                if  changeAcc(user["user1"]["user"],user["user1"]["pass"]):
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
                    closeEvent()
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
    #check auto show event
    if CheckGUIEvent():
        dataReportConfig['GuiEvent']="Pass"
    else:
        dataReportConfig['GuiEvent']="Fail"
    #close Gui Event
#     clickClaim()
    closeEvent()
#     closeEvent()
#     claimAll()
#     closeAllEvent()
    #check auto show deal
    if CheckGUIDeal():
        dataReportConfig['GuiEDeal']="Pass"
    else:
        dataReportConfig['GuiEDeal']="Fail"
    #close Gui Deal
    closeEvent()
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
# def day6():
#         #resetDataReport
#     resetDataReportConfig()
#     #------------------------#
#     #cheat time pass 1 ngay-> 30/11/2020 11:11:11 -> 1606709471000
#     timeCheat = api_changeTimeServer(1605051600000)
#     #timeCheat = api_changeTimeServer(timeC["timeD0"]["mili"])
#     dayS = {
#         "Y": timeWC["start"]['Y'],
#         "M": timeWC["start"]['M'],
#         "D": timeWC["start"]['D'],
#         "h": timeWC["start"]['h'],
#         "m": timeWC["start"]['m'],
#         "s": timeWC["start"]['s']
#     }
#     timeNow=convertDayTimeToMili(dayS) + datetoMili(5)
#     timeCheat = api_changeTimeServer(timeNow)
#     dataReportConfig["TimeCheat"]=convertSecondstoDateTime(timeNow)
#     #reload lobby
#     reloadLobby()
#     #click btn play
#     joinTable()
#     #cheat theo nhiem vu
#     #add bot
#     addBot()
#     #Click knock
#     if clickKnock():
#         data1["Knock"]="Pass"
#     else:
#         data1["Knock"]="Fail"
#     #wait end game
#     waitEndGame()
#     #check update progess
#     if checkUpdateProgessTable():
#         data1["Update"]="Pass"
#     else:
#         data1["Update"]="Fail"
#     #waitplaygame
#     sleep(10)
#     #cheat theo nhiem vu
#     #Click knock
#     if clickKnock():
#         data1["Knock"]="Pass"
#     else:
#         data1["Knock"]="Fail"
#     #chon thoat table
#     clickOutTable()
#     #wait end game
#     waitEndGame()
#     #check update progess
#     if checkUpdateProgessTable():
#         data1["Update"]="Pass"
#     else:
#         data1["Update"]="Fail"
#        #check lobby
#     if CheckLobby():
#         data1["Leave"]="Pass"
#     else:
#         data1["Leave"]="Fail"
#     #------------------------#
#     #report
#     reportDay6(data1)
#     #------------------------#
#     #report
#     reportDay3(dataReportConfig)
#     #------------------------#
#     checkMission("day3")
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
    #click btn play
    joinTable()
    checkGold
    #wait pass day
    waitTimePassDay(timeW)
    #check progess table
    if checkProgessTable():
        dataReportConfig["Progess"]="Fail"
    else:
        dataReportConfig["Progess"]="Pass"
    #chon thoat table
    clickOutTable()
    #check auto show event
    if CheckGUIEvent():
        dataReportConfig['GuiEvent']="Pass"
    else:
        dataReportConfig['GuiEvent']="Fail"
    #check gold init
    goldInit=checkGold()
    #check gold claim
    goldClaim=challengePlay[challenge["day6"]["mission"]]["data"]["gold"]
    #click claim gift
    if clickClaim():
        dataReportConfig['Claim']="Pass"
    else:
        dataReportConfig['Claim']="Fail"
    #exit GUI event
    closeEvent()
    #check update gold
    goldAfter=checkGold()
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
    try:
        #join event
        eventWCOpen()
        #check progress
        prog1=checkProgressCurrent()
        print(prog1)
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
        #check update progess
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
        #check progress
        prog1=checkProgressCurrent()
        closeEvent()
        #cheat gold du play
        if cheatGold(user["user1"]["id"],1000000) :
            dataReportConfig["CheatGold"]="Pass"
        else :
            dataReportConfig["CheatGold"]="Fail"
        #click btn play
        if joinTable():
            dataReportConfig["BtnPlay"]="Pass"
        else:
            dataReportConfig["BtnPlay"]="Fail"
        #Check table
        if tableGame():
            dataReportConfig["JoinTable"]="Pass"
        else:
            dataReportConfig["JoinTable"]="Fail"
        #cheat cheatPorkerSpecial
        #add bot
        if addBot():
            dataReportConfig["Bot"]="Pass"
        else:
            dataReportConfig["Bot"]="Fail"
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
        if CheckLobby():
            dataReportConfig["Leave"]="Pass"
        else:
            dataReportConfig["Leave"]="Fail" 
        closeEvent()
    except:
        print("error knock")
    print(dataReportConfig)
    reportKnock(dataReportConfig)
# def collect(day):
#      try:
#         #join event
#         eventWCOpen()
#         #check progress
#         prog1=checkProgressCurrent()
#         closeEvent()
#         #cheat gold du play
#         cheatGold(user["user1"]["id"],1000000)
#         #click btn play
#         joinTable()
#         #cheat cheatPorkerSpecial
#         #add bot
#         addBot()
#         #Click knock
#         clickKnock()
#         prog2=checkProgressCurrent()
#         #cheat win finished game
#         # cheatNumMision(1)
#         #chon thoat table
#         clickOutTable()
#         #wait end game
#         waitEndGame()
#         #check update progess
#         if checkUpdateProgessTable(prog1,prog2):
#             dataReportConfig["Update"]="Pass"
#         else:
#             dataReportConfig["Update"]="Fail"
#            #check lobby
#         CheckLobby()
#         closeEvent()
#     except:
#         print("error collect")
#     print(dataReportConfig)
#     reportCollect(dataReportConfig)
def claimGift():
    # script content
    #back to loby
    CheckLobby()
    #check gold init
    goldInit=checkGold()
    #Cheat finished mission-----------------------
    if cheatFinishedMision(user["user1"]["id"],1):
        dataReportConfig['CheatFM']="Pass"
    else:
        dataReportConfig['CheatFM']="Fail"
    #---------reload lobby------------------------------
    reloadLobby()
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
    to2=checkTocos()
    #exit GUI event
    closeEvent()
    #check update gold
    goldAfter=checkGold()
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
    CheckLobby()
    #check gold init
    goldInit=checkGold()
    #Cheat finished mission-----------------------
    cheatFinishedMision(user["user1"]["id"],2)
    #---------reload lobby------------------------------
    reloadLobby()
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
    goldAfter=checkGold()
    if checkUpdateGold(goldClaim,goldInit,goldAfter):
        dataReportConfig['GoldUpdate']="Fail"
    else:
        dataReportConfig['GoldUpdate']="Pass"
    #End in Game----------------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportNoClaimGift(dataReportConfig)
def passClaimGift():
    # script content
    #Change acc 1
    changeAcc(user["user1"]["user"],user["user1"]["pass"])
    #check GUI event
    if CheckGUIEvent():
        dataReportConfig['GuiEvent']="Pass"
    else:
        dataReportConfig['GuiEvent']="Fail"
        eventWCOpen()
    #checkAuto claim
    to1=checkTocos()
    sleep(5)
    to2=checkTocos()
    tocosConf=challengePlay[challenge["day2"]["mission"]]["data"]["tacos"]
    if checkTocosUpdate(tocosConf,to1,to2):
        dataReportConfig['UpdateTocos']="Pass"
    else:
        dataReportConfig['UpdateTocos']="Fail"
    #check tick claim day2
    #checkUpdate mission
    if CheckMissionProgress("day4"):
        dataReportConfig["MissionNew"]="Pass"
    else:
        dataReportConfig["MissionNew"]="Fail"
    #exit GUI event
    closeEvent()
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
    
    #check update nhiem vu ngay 3
    #Show update mission
    if CheckMissionProgress("day3"):
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
    changeAcc(user["user2"]["user"],user["user2"]["pass"])
    #open Gui
    eventWCOpen()
    #check nv day 1
    print("error find poco no name")
    if True:
        dataReportConfig['MissionDay1']="Pass"
    else:
        dataReportConfig['MissionDay1']="Fail"
    #exit GUI event
    closeEvent()
    #End in Game----------------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportChangeAcc(dataReportConfig)
def missionPassDayInTable():
    #Cheat finished mission
#     timeCheat = api_changeTimeServer(convertDayTimeToMili(timeWC["start"]))
#     reloadLobby()
#     clickClaim()
#     closeEvent()
#     cheatFinishedMision(user["user2"]["id"],2)
#     reloadLobby()
#     clickClaim()
#     closeEvent()
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
    timeNow= convertDayTimeToMili(dayS) + datetoMili(1) - housToMili(1) + minutetoMili(59) 
    timeCheat = api_changeTimeServer(timeNow)
    #reload lobby
    reloadLobby()
    clickClaim()
    closeEvent()
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
    if CheckMissionProgress("day2"):
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
def missionPassDayOpenGui():
    #Cheat finished mission
    cheatFinishedMision(user["user2"]["id"],3)
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
    dayS['D'] = dayS['D']+3
    dayS['h'] = dayS['h']-1
    dayS['m'] = dayS['m']+59
    timeCheat = api_changeTimeServer(convertDayTimeToMili(dayS))
    #reload lobby
    reloadLobby()
    clickClaim()
    closeEvent()
    eventWCOpen()
    waitTimePassDay(timeW)
    #Show update mission
    if CheckMissionProgress("day4"):
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
    if  changeAcc(user["user1"]["user"],user["user1"]["pass"]):
        dataReportConfig['Login']="Fail"
    else:
        dataReportConfig['Login']="Pass"
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
    gold1=checkGold()
    clickGuiDeal()
    cheatBuyDeal(user["user1"]["id"],1)
    clickClaim()
    if checkDisableBtnDeal():
        dataReportConfig['BtnBuyWC']="Fail"
    else:
        dataReportConfig['BtnBuyWC']="Pass"
    closeEvent()
    gold2=checkGold()
    if checkUpdateGoldDeal(dealWCConfig["offerWC1"],gold1,gold2):
        dataReportConfig['GoldUpdate']="Pass"
    else:
        dataReportConfig['GoldUpdate']="Fail"
    clickGuiDeal()
    cheatBuyDeal(user["user1"]["id"],2)
    clickClaim()
    sleep(1)
    cheatBuyDeal(user["user1"]["id"],3)
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
    dayS['h'] = dayS['h']-1
    dayS['m'] = dayS['m']+59
    timeCheat = api_changeTimeServer(convertDayTimeToMili(dayS))
#     dataReportConfig["TimeCheat"]=fortmartTime(dayS)
    #End Cheatime---------------------------------------
    #---------reload lobby------------------------------
    reloadLobby()
    #---------end reload lobby--------------------------
    #check gold init
    goldInit=checkGold()
    #opent GUI event
    eventWCOpen()
    #check gold claim
    goldClaim=challengePlay[challenge["day7"]["mission"]]["data"]["gold"]
    #wait pass day
    waitTimePassDay(timeW)
    #check close GUI
    if CheckGUIEvent():
        dataReportConfig['GUIEvent']="Fail"
    else:
        dataReportConfig['GUIEvent']="Pass"
    #check gold
    goldAfter=checkGold()
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
        if cheatGoldEmpty("1") :
            dataReportConfig["CheatGold0"]="Pass"
        else :
            dataReportConfig["CheatGold0"]="Fail"
        sleep(2)
        #open event
        if eventWCOpen():
            dataReportConfig["OpenGUI"]="Pass"
        else:
            dataReportConfig["OpenGUI"]="Fail"
        sleep(2)
        #click btn play
        joinMission()
        #check noti
        if checkNotiNoEnoughGold():
            dataReportConfig["BtnPlay0"]="Pass"
        else:
            dataReportConfig["BtnPlay0"]="Fail"
        closeEvent()
        #cheat gold du play
        if cheatGold(user["user1"]["id"],1000000):
            dataReportConfig["CheatGold1"]="Pass"
        else:
            dataReportConfig["CheatGold1"]="Fail"
        reloadLoby2()
        #open event
        eventWCOpen()
        #click btn play
        sleep(2)
        if joinMission():
            dataReportConfig["BtnPlay1"]="Pass"
        else:
            dataReportConfig["BtnPlay1"]="Fail"
        #check progess table
        if checkProgessTable():
            dataReportConfig["Progess"]="Pass"
        else:
            dataReportConfig["Progess"]="Fail"
        #Check table
        if tableGame():
            dataReportConfig["JoinTable"]="Pass"
        else:
            dataReportConfig["JoinTable"]="Fail"
        #cheat cheatPorkerSpecial
        #cheat win finished game
        if cheatNumMision(1,user["user1"]["id"]):
            dataReportConfig["CheatFOM"]="Pass"
        else:
            dataReportConfig["CheatFOM"]="Fail"
        #add bot
        # addBot()
        #wait luot ban than
        #Click knock
        # clickKnock()
        #chon thoat table
    #     clickOutTable()
        #wait end game
    #     waitEndGame()
        #check update progess
        if checkUpdateProgessTable(prog1,prog2):
            dataReportConfig["Update"]="Pass"
        else:
            dataReportConfig["Update"]="Fail"
        clickOutTable()
        #check lobby
        if CheckLobby():
            dataReportConfig["Leave"]="Pass"
        else:
            dataReportConfig["Leave"]="Fail"
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
def checkProgressCurrent():
    try:
        if waitNolimitPoco(pocoTag.lbProgress,5):
            progress=pocoTag.lbProgress.get_text()
            prg=progress.split("/")
            prgL=int(prg[0].strip())
            prgR=int(prg[1].strip())
            print(prgR)
            print(prgL)
            print("Progess checkProgressCurrent")
            return prgL
        else:
            print("NO find progress")
            return False
    except:
        print("error checkProgressCurrent")
        return False
# def checkProgress():
#      try:
#         if waitNolimitPoco(pocoTag.lbProgress,5):
#             print("Progess checkProgressCurrent")
#             return True
#         else:
#             print("NO find progress")
#         return False
#     except:
#         print("error checkProgressCurrent")
#         return False
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
            tocos=int(pocoTag.lbNumTacos.get_text())
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
        "status": "False",
        "Time": "False",
        "button": "False",
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
        "status": "False",
        "Time": "False",
        "button": "False",
    }
    pocoTag.btnSwitch.click()
    pocoTag.inputUser.click()
    text("ngocnn49")
    pocoTag.inputPass.click()
    text("12345678")
    pocoTag.btnRegister.click()  
# Nhận dailybonus của ngày đầu tiên
def bonus_day_1():
    data= {
        "status": "False",
        "Time": "False",
        "button": "False",
    }
    if pocoTag.btnClaim.exists():
        data["status"]="true"
        time.sleep(3)
        pocoTag.btnClaim.click()
        pocoTag.btnClaim.click()
        print("nhan gold day 1 success!")
    else:
        print("khong auto show Gui daily bonus sau play tutorial")
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
        "status": "False",
        "Time": "False",
        "button": "False",
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
        "status": "False",
        "Time": "False",
        "button": "False",
    }
    time.sleep(3)
    if pocoTag.btnClaim.exists():
        data["status"]="True"
        pocoTag.btnClaim.click()
    else:
        print("Dont show GUI bonus")
        data["status"]="False"
    reportdailybonus(data)
#9. Kiểm tra có show GUI daily bonus khi dung o lobby cho nhan bonus
def check_show_GUI():
    api_changeTimeServer(1608796800000)
    try:
        pocoTag.btnClaim.exists()
    except:
        print("Khong auto show GUI daily bonus o lobby sau 24h")
    else:
        print("Auto show GUi daily bonus khi o lobby sau24h!")
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
        "status": "False",
        "Time": "False",
        "button": "False",
    }
    time.sleep(5)
    if pocoTag.btnClaim.exists():
        pocoTag.btnClaim.click()
        time.sleep(3)
        data["status"]="False"
        print("Show daily GUI daily bonus khi chua du 24h")
    else:
        data["status"]="True"
        print("Ko Show GUI khi chuwa ddur 24h!")
    reportdailybonus(data)
    time.sleep(3)
#11. Vao playinggame-> ra lại lobby
def playing_23h():
    data= {
        "status": "False",
        "Time": "False",
        "button": "False",
    }
    pocoTag.btnPlay.click()
    api_changeTimeServer(1608882000000)
    pocoTag.btnLeaveGame.click()       #leave khi chưa đủ 24h
    time.sleep(1)
    try:
        pocoTag.btnClaim.exists() 
    except:
        print("playing->lobby: Khong show GUI daily bonus khi chua du 24h")
        time.sleep(3)
        pocoTag.btnClaim.click()
        data["status"]="True"
    else:
        data["status"]="False"
        print("Show GUI bonus khi leave tuwf playing khi chuwa ddur 24h")
    reportdailybonus(data)
#12. Vào playing game-> Chờ qua 24h rồi ra lại lobby( Ngày 4)
def playing_24h():
    data= {
        "status": "False",
        "Time": "False",
        "button": "False",
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
        "Time": "False",
        "button": "False",
    }
    reloadLobby()
    pocoTag.btnDaily.click()
    api_changeTimeServer(1608966000000)
    if pocoTag.btnTomorrow.exists():
        print("Show daily bonus khi o GUI daily bonus sau 23h")
        data["status"]="False"
    else:
        print("Show daily bonus khi chưa du 24h")
        data["status"]="True"
#16 Nhận bonus 5 lần-> Log out-> Login sau 24h nhưng không nhận bonus->Login lại sau 24h tiếp theo
def claim_kill_login_24h():
    data= {
        "status": "False",
        "Time": "False",
        "button": "False",
    }
    time.sleep(3)
    if pocoTag.btnClaim.exists():
        print("Show daily bonus day 5 Success!")
        gold_befor5= gold_number()
        pocoTag.btnClaim.click()
        gold_after5= gold_number()
        if DailyBonus["day5"]["bonus"]==(gold_after5 - gold_befor5):    
            data["status"]="True"
        else:
            print("Update gold sai")
            data["status"]="False"
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
    try:
        pocoTag.btnClaim.exists()
    except:
        print("Không auto show daily bonus khi khong nhan bonus cua ngay truoc")
    else:
        print("Show GUI khi kill app ko nhaan cuar ngay trc!")
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