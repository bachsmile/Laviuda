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
from poco.agent import PocoAgent
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
#tắt app
def killApp():
    try:
        clear_app("com.zingplay.laviuda")
        print('kill App')
        return True
    except:
        print('error kill App')
        return False
#mở lại app
def openApp():
    try:
        start_app("com.zingplay.laviuda")
        print('open App')
        return True
    except:
        print('error open App')
        return False
#kiểm tra đối tượng 
def exists1(self):
        try:
            return self.attr('visible')
        except :
            return 0
#check đối tượng hình ảnh
def waitNoLimit(obj,time):
    try:
        wait(obj,time,0.5)
        return True 
    except:
        return False
#check đối tượng poco
def waitNolimitPoco(obj,time):
    return obj.wait(time).exists()
#MPK-> số
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
#Chuyển json time -> chuỗi time
def fortmartTime(time):
    timeStr= str(time['D'])+"/"+str(time['M'])+"/"+str(time['Y'])+" "+str(time['h'])+":"+str(time['m'])+":"+str(time['s'])
    print(timeStr)
    return timeStr
#cheat
#cheat gold về 0
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
#cheat set card trong bàn chơi
def CheatCard(wildCard,cardPlay):#ex: WildCard = '2c', cardPlay="ab,2b,3b,4b,5b"
    pocoTag.btnCheat.click()
    pocoTag.btnTabCustom.click()
    pocoTag.btnResetCustom.click()
    pocoTag.pnPointEvent.click([0.7598879526638265, 0.6159336566925049])
    text("")
    pocoTag.pnPointEvent.click([0.7598879526638265, 0.6159336566925049])
    text(wildCard)
    pocoTag.pnCaseId_1.click([0.5944052164770731, 0.4596827030181885] )
    text(cardPlay)
    pocoTag.btnSendCustom.click()
    pocoTag.btnCheat.click()
    clear()
# Action
#reload
def back_to_lobby():
    btns = [image_vip.outroom, image_vip.icon_close, image_vip.back, image_vip.close]
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
        clear()
        pocoTag.btnSelectTable.click()
#         back_to_lobby()
        sleep(1)
        if waitNolimitPoco(pocoTag.btnLeaveGame,1):
            pocoTag.btnLeaveGame.click()
        else:
            touch(image_vip.back)  
#         touch(image_vip.back)    
        print('reload lobby')
        return True
    except:
        print('error reload lobby')
        return False
def reloadLoby2():
    try:
        poco = CocosJsPoco()
        clear()
        poco.click([0.04817596456992819, 0.9241753578186035])
        pocoTag.btnHide.click()
    except:
        clear()
#dong cac event "x"
def closeEvent():
    try:
        clear()
        if waitNolimitPoco(pocoTag.btnClose,2):
            pocoTag.btnClose.click()  
    except:
        print("error close ev")
#dong tat ca cac event co btn x xuat hien
def closeAllEvent():
    clear()
    while waitNolimitPoco(pocoTag.btnClose,2):
        pocoTag.btnClose.click()
        clear()
#claim tat ca nhung pop up claim xuat hien
def claimAll():
    clear()
    while waitNolimitPoco(poco("btnClaim"),2):
        pocoTag.btnClaim.click()
        clear()
        continue
#logout
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
#thay doi tai khoang
def changeAcc(userN,passW):
    try:
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
        clear()
        return True
    except:
        print("error login")
#vao ban choi
def joinTable():
    try:
        sleep(2)
        clear()
        poco = CocosJsPoco()
#         pocoTag.btnPlay.click()
        pocoTag.btnSelectTable.click()
        print("joinTable")
        return 1
    except:
        print("error joinTable")
        return 0
#out ban choi
def clickOutTable():
    try:
        poco = CocosJsPoco()
        pocoTag.btnLeaveGame.click()
        print("register back")
        return True
    except:
        print("error register back")
        return False
#them bot
def addBot():
    try:
        poco = CocosJsPoco()
        pocoTag.btnCheat.click()
        for i in range(2):
            sleep(1)
            pocoTag.btnAddBot.click()
        pocoTag.btnCheat.click()
        print("event addBot")
        clear()
        return True
    except:
        print("error addBot")
        return False
#click btn knock
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
#click btn pass
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
#click btn exchange1
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
#click btn exchange5
def clickExchange5():
    try:
        if waitNolimitPoco(pocoTag.btnExchange5,60):
            pocoTag.btnExchange5.click()
            return True
        else:
            return False
    except:
        return False
#claim qua 1 lan
def clickClaim():
    try:
        if waitNolimitPoco(pocoTag.btnClaim,1):
            pocoTag.btnClaim.click()
            clear()
            return True
        else:
            return False
    except:
        return False
# check
#check ban choi
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
#check lobby
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
#check end game khi thua
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
#check end game khi thang
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
#format gold ve dang hien thi trong game
def fortmatGold(gold):
    if gold/pow(10,9)>=1:
        if (gold % pow(10, 9))//pow(10,8)>0:
            return (str(gold // pow(10, 9)) + "." + str((gold % pow(10, 9))//pow(10,8)) + "B")
        else:
            return(str(gold // pow(10, 9)) + "B")
    elif gold/pow(10,6)>=1:
        if (gold % pow(10, 6))//pow(10,5)>0:
            return (str(gold // pow(10, 6)) + "." + str((gold % pow(10, 6))//pow(10,5)) + "M")
        else:
            return (str(gold // pow(10, 6)) + "M")
    elif gold/pow(10,3)>10:
        if ((gold % pow(10, 3))//pow(10,2))>0:
            return (str(gold // pow(10, 3)) + "." + str((gold % pow(10, 3))//pow(10,2)) + "K")
        else:
            return (str(gold // pow(10, 3)) + "K")
    else:
        return (str(gold))
#lay text gold trong ther gold nguoi choi
def checkGold():
#     numGold = pocoTag.lbGold.attr("text")
    numGold = poco(name="lbGold").attr("text")
#     return pipeSubGold(numGold)
    return numGold
#chuyen time sang miliseconds
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
        cheat_remain = api_postDoFunction(UserID, "CHEAT_TIME_REMAIN_VIP", [str(convertDayToSecond(day))])
        print("cheat time remain thanh cong")
        reloadLobby()
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
        else:
            data["Status"] = "Fail"
            print("Vao khong thanh cong")
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
                    swipe(image_vip.hoahong1, vector=[-0.1399, -0.0097])
                    time.sleep(2)
                    touch(item)
            data["Check_item"] = "Pass"
            print("List item co ton tai")   
        else:
            data["Check_item"] = "Fail"
            print("List item khong ton tai")
    except:
        print("Error")
def check_item3():
    try:
        touch(image_vip.btn_profile)
        if exists(image_vip.list_item):
            swipe(image_vip.hoahong1, vector=[-0.1399, -0.0097])
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
        pocoTag.btnVip.click()
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
        time.sleep(1)
        touch(image_vip.btn_claim)
        time.sleep(1)
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
        if checkUpdateGold(gold_conf,old_gold,new_gold):
            data["Check_gold"] = "Pass"
            print("Success")
    except:
        data["Check_gold"] = "Fail"
        print("Error")
def check_gold_support(idU):
    cheatGoldEmpty(1)
    time.sleep(2)
    reloadLobby()
    old_gold = getGold(idU)
    try:
        if exists(image_vip.pop_up_gold_support):
            touch(image_vip.btn_ok_sp)
            time.sleep(1)
            new_gold = getGold(idU)
            gold_in = new_gold - old_gold
            gold_conf = gold_support
            if checkUpdateGold(gold_conf,old_gold,new_gold):
                data["Gold_support"] = "Pass"
                data["Status"] = "Pass"
                print("Nhan gold support thanh cong")
        else:
            data["Gold_support"] = "Fail"
            data["Status"] = "Fail"
            print("khong nhan duoc gold support")
    except:
        print("Error")
def cheatBuyGold(idU, pack):
    try:
        cheat = api_postDoFunction(idU, "CHEAT_PAYMENT_IAP", [pack])
        time.sleep(2)
        pocoTag.btnClaim.click()
        print("Success")
    except:
        print("Error")
def check_buy_gold(idU, pack):
    old_gold = getGold(idU)
    cheatBuyGold(idU, pack)
    try:
        time.sleep(1)
        new_gold = getGold(idU)
        gold_in = new_gold - old_gold
        gold_defaul = pack_gold["gg_play"][pack]
        if getLevelVip(idU) == 1:
            gold_conf = gold_defaul + gold_defaul*30/100
        elif getLevelVip(idU) == 2:
            gold_conf = gold_defaul + gold_defaul*50/100
        elif getLevelVip(idU) == 3:
            gold_conf = gold_defaul*2
        else:
            gold_conf = gold_defaul
        if checkUpdateGold(gold_conf,old_gold,new_gold):
            data["Check_gold"] = "Pass"
            data["Status"] = "Pass"
            print("Success")
    except:
        data["Check_gold"] = "Fail"
        data["Status"] = "Fail"
        print("Error")
def check_gold_tribute(idU):
    old_gold = getGold(idU)
    try:
        if exists(image_vip.btn_claim):
            pocoTag.btnClaim.click()
            time.sleep(1)
            new_gold = getGold(idU)
            gold_in = new_gold - old_gold
            if getLevelVip(idU) == 1:
                gold_conf = vip_pack["vip.pack_1"]["dailyTribute"]
            elif getLevelVip(idU) == 2:
                gold_conf = vip_pack["vip.pack_2"]["dailyTribute"]
            elif getLevelVip(idU) == 3:
                gold_conf = vip_pack["vip.pack_3"]["dailyTribute"]
            else:
                gold_conf = 0
            if checkUpdateGold(gold_conf,old_gold,new_gold):
                data["Gold_tribute"] = "Pass"
                data["Status"] = "Pass"
                print("Nhan duoc gold tribute")
        else:
            data["Gold_tribute"] = "Fail"
            data["Status"] = "Fail"
            print("Ko nhan duoc gold tribute")
    except:
        print("Error")
def back_lobby_from_table():
    try:
        if exists(image_vip.outroom):
            touch(image_vip.outroom)
            time.sleep(1)
            print("Out ban thanh cong")
        else:
            print("Out ban khong thanh cong")
    except:
        print("error")
def checkMoGUIGH():
    try:
        if exists(image_vip.btn_giahan):  
            touch(image_vip.btn_giahan)
            data["Show_PopUp_GH"] = "Pass"
            data["Mo_GUI_Vip"] = "Pass"
            data["Status"] = "Pass"
            print("Success")
        else:
            data["Show_PopUp_GH"] = "Fail"
            data["Mo_GUI_Vip"] = "Fail"
            data["Status"] = "Fail"
            print("error")
    except:
        print("error")
def checkMoGUIVip():
    try:
        if exists(image_vip.btn_hethan):
            touch(image_vip.btn_hethan)
            print("vao GUI vip thanh cong")
        else:
            print("Vao GUI vip ko thanh cong")
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
        back_to_lobby()
    except:
        print("error")
#Function WC:---------------------->
    #------------------#
#case1
def beforEvent(users):
    clearReport()
    claimAll()
    closeAllEvent()
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
    changeAcc(user[users]["user"],user[users]["pass"])
    sleep(5)
    #closeEvent()
    claimAll()
    closeAllEvent()
    #reloadLobby()
    reloadLoby2()
#     claimAll()
#     closeAllEvent()
    #Check btn event -----------------------------------
    if CheckBtnEvent():
        dataReportConfig["Button"]="Fail"
    else:
        dataReportConfig["Button"]="Pass"
    #end Check btn event--------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportBeforEvent(dataReportConfig)
#case2
def afterEvent(users):
    resetDataReportConfig()
    claimAll()
    closeAllEvent()
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
                timeNow=convertDayTimeToMili(dayS1) -housToMili(1)+ minutetoMili(59)+secToMili(20)
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
                if changeAcc(user[users]["user"],user[users]["pass"]):
                    claimAll()
                    closeAllEvent()
                    CheckLobby()
                    joinTable()
                    sleep(20)
                    if checkProgress():
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
                timeNow=convertDayTimeToMili(dayS1) -housToMili(1)+ minutetoMili(59)+secToMili(20)
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
                if changeAcc(user[users]["user"],user[users]["pass"]):
                    claimAll()
                    closeAllEvent()
                    CheckLobby()
                    #join table wait
                    joinTable()
                    #wait event
                    sleep(20)
                    if checkProgress():
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
            timeNow=convertDayTimeToMili(dayS1) -housToMili(1)+ minutetoMili(59)+secToMili(20)
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
            if changeAcc(user[users]["user"],user[users]["pass"]):
                sleep(1)
                claimAll()
                closeAllEvent()
                CheckLobby()
                #join table wait
                joinTable()
                #wait event
                sleep(20)
                if checkProgress():
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
#case3
def day1(user):
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
    checkMission("day1",user)
#case4
def day2(user):
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
    checkMission("day2",user)
#case5
def day3(user):
        #resetDataReport
    resetDataReportConfig()
    claimAll()
    closeAllEvent()
    #------------------------#
    #report
    reportDay3(dataReportConfig)
    #------------------------#
    checkMission("day3",user)
#case6
def day4(user):
        #resetDataReport
    resetDataReportConfig()
    claimAll()
    closeAllEvent()
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
    checkMission("day4",user)
#case7
def day5(users):
        #resetDataReport
    resetDataReportConfig()
    claimAll() 
    closeAllEvent()
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
    claimAll()
    closeAllEvent()
    #join event
    eventWCOpen()
     #check progress
    prog1=checkProgressCurrent()
    closeEvent()
    #cheat gold du play
    cheatGold(user[users]["id"],1000000)
    checkMission2("day5")
    sleep(2)
    claimAll()
    closeAllEvent()
    eventWCOpen()
    prog2=checkProgressCurrent()
    closeEvent()
    #check update progess
    if checkUpdateProgessTable(prog1,prog2):
        dataReportConfig["Update"]="Pass"
    else:
        dataReportConfig["Update"]="Fail"
    #report
    reportDay5(dataReportConfig)
#case8
def day6(users):
        #resetDataReport
    resetDataReportConfig()
    sleep(2)
    claimAll() 
    closeAllEvent()
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
    cheatGold(user[users]["id"],1000000)
    reloadLobby()
    claimAll() 
    closeAllEvent()
    #click btn play
    joinTable()
    prog1=checkProgressCurrent()
    #cheat theo nhiem vu
    #add bot
    addBot()
    #Click knock
    clickKnock()
    #wait end game
    waitEndGame()
    prog2=checkProgressCurrent()
    #check update progess
    if checkUpdateProgessTable(prog1,prog2):
        dataReportConfig["Update"]="Pass"
    else:
        dataReportConfig["Update"]="Fail"
    #chon thoat table
    clickOutTable()
    #wait end game
    waitEndGame()
    #------------------------#
    #report
    reportDay6(dataReportConfig)
    #------------------------#
#case9
def day7(users,user1):
    resetDataReportConfig()
    sleep(2)
    claimAll()
    closeAllEvent()
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
    timeNow=convertDayTimeToMili(dayS) + datetoMili(6)-secToMili(40)
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
    sleep(30)
    #check progess table
    if checkProgessTable():
        dataReportConfig["HideProgress"]="Fail"
    else:
        dataReportConfig["HideProgress"]="Pass"
    #chon thoat table
    clickOutTable()
    sleep(1)
    claimAll()
    closeDealSpec1()
    #check auto show event
    #check gold init
    goldInit=getGold(user[users]["id"])
    if CheckGUIEvent():
        dataReportConfig['GuiEvent']="Pass"
    else:
        dataReportConfig['GuiEvent']="Fail"
        eventWCOpen()
    #check gold claim
    to=checkTocos()
    goldClaim=to*challengePlay[challenge["day7"]["mission"]]["data"]["gold"]
    #click claim gift
    clickClaimMission()
    #exit GUI event
#     closeEvent()
    clickClaim()
    #check update gold
    goldAfter=getGold(user[users]["id"])
    if checkUpdateGold(goldClaim,goldInit,goldAfter):
        dataReportConfig['UpdateGold']="Pass"
    else:
        dataReportConfig['UpdateGold']="Fail"
    #close Gui Event
#     closeEvent()
    #change acc3
    changeAcc(user[user1]["user"],user[user1]["pass"])
    claimAll()
    closeAllEvent()
    eventWCOpen()
    #check gift
    gift=checkTocos()
    if gift==0:
        dataReportConfig['CheckGift']="Pass"
    else:
        dataReportConfig['CheckGift']="Fail"
    #------------------------#
    #report
    reportDay7(dataReportConfig)
#case10
def exchange1(day,users):
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
        cheatGold(user[users]["id"],1000000) 
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
#case11
def knock(day,users):
    try:
        resetDataReportConfig()
        claimAll()
        closeAllEvent()
        #join event
        eventWCOpen()
        #check progress
        prog1=checkProgressCurrent()
        closeEvent()
        cheatGold(user[users]["id"],1000000)
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
#case12
def collect(day,users):
    try:
        resetDataReportConfig()
        claimAll()
        closeAllEvent()
        #join event
        eventWCOpen()
        #check progress
        prog1=checkProgressCurrent()
        closeEvent()
        #cheat gold du play
        cheatGold(user[users]["id"],1000000)
        #click btn play
        joinTable()
        #cheat cheatPorkerSpecial
        if challengePlay[challenge[day]["mission"]]["data"]["type"] == 'wc':
            CheatCard(cardCheat["wc"]["card"],cardCheat["wc"]["set"])
#         if challengePlay[challenge["day"+str(day)]["mission"]]["data"]["type"] == 'wc':
#             CheatCard(cardCheat["wc"]["card"],cardCheat["wc"]["set"])
        #add bot
        addBot()
        #Click knock
        clickKnock()
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
#case13
def claimGift(day,users):
    # script content
    resetDataReportConfig()
    claimAll()
    closeAllEvent()
    #back to loby
    CheckLobby()
    #check gold init
    goldInit=getGold(user[users]["id"])
    #Cheat finished mission-----------------------
    if cheatFinishedMision(user[users]["id"],1):
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
    goldClaim=challengePlay[challenge[day]["mission"]]["data"]["gold"]
    tocosConf=challengePlay[challenge[day]["mission"]]["data"]["tacos"]
    #click claim gift
    clickClaimMission()
    sleep(2)
    to2=checkTocos()
    #exit GUI event
    closeEvent()
    #check update gold
    goldAfter=getGold(user[users]["id"])
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
#case14
def noClaimGift(day,users):
   #back to loby
    resetDataReportConfig()
    claimAll()
    closeAllEvent()
    CheckLobby()
#     poco("btnJoin")
    #check gold init
    goldInit=getGold(user[users]["id"])
    #Cheat finished mission-----------------------
    cheatFinishedMision(user[users]["id"],2)
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
    goldClaim=challengePlay[challenge[day]["mission"]]["data"]["gold"]
    #check update gold
    goldAfter=getGold(user[users]["id"])
    if checkUpdateGold(goldClaim,goldInit,goldAfter):
        dataReportConfig['GoldUpdate']="Fail"
    else:
        dataReportConfig['GoldUpdate']="Pass"
    #End in Game----------------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportNoClaimGift(dataReportConfig)
#case15
def passClaimGift(day,users):
    resetDataReportConfig()
    claimAll()
    closeAllEvent()
    # script content
    #Change acc 1
    changeAcc(user[users]["user"],user[users]["pass"])
    claimAll()
    closeNotiVip()
    claimAll()
    closeDealSpec1()
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
    tocosConf=challengePlay[challenge["day"+str(day)]["mission"]]["data"]["tacos"]
    if checkTocosUpdate(tocosConf,to1,to2):
        dataReportConfig['UpdateTocos']="Pass"
    else:
        dataReportConfig['UpdateTocos']="Fail"
    #check tick claim day2
    if checkFinishMission(day):
        dataReportConfig['Tick']="Pass"
    else:
        dataReportConfig['Tick']="Fail"
    #checkUpdate mission
    if CheckMissionProgress(day+2):
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
#case16
def autoClaimGift(day):
    resetDataReportConfig()
    claimAll()
    closeNotiVip()
    claimAll()
    closeDealSpec()
    closeDealSpec1()
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
    tocosConf=challengePlay[challenge[day]["mission"]]["data"]["tacos"]
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
    closeEvent()
    #End in Game----------------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportAutoClaim(dataReportConfig)
#case17
def CheckChangeAcc(day,users):
     # script content
    #change acc
    resetDataReportConfig()
    claimAll()
    closeAllEvent()
    changeAcc(user[users]["user"],user[users]["pass"])
    claimAll()
    closeAllEvent()
    #open Gui
    eventWCOpen()
    #check nv day 1
    if checkMissedMission(day):
        dataReportConfig['MissionDay1']="Pass"
    else:
        dataReportConfig['MissionDay1']="Fail"
    #exit GUI event
    closeEvent()
    #End in Game----------------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportChangeAcc(dataReportConfig)
#case18
def missionPassDayInTable(day,users):
    resetDataReportConfig()
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
    closeAllEvent()
    cheatFinishedMision(user[users]["id"],day)
    reloadLobby()
    sleep(1)
    claimAll()
    closeAllEvent()
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
#case19
def missionPassDayOpenGui(day,users):
    resetDataReportConfig()
    to1=0
    to2=0
    #Cheat finished mission
    cheatFinishedMision(user[users]["id"],day)
    reloadLobby()
    claimAll()
    closeAllEvent()
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
    timeNow= convertDayTimeToMili(dayS) + datetoMili(day) - housToMili(1) + minutetoMili(59)+secToMili(30) 
    timeCheat = api_changeTimeServer(timeNow)
    #reload lobby
    reloadLobby()
    claimAll()
    closeAllEvent()
    claimAll()
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
    closeEvent()
    #------------------------#
    #report
    print(dataReportConfig)
    reportUpdateMissionLobby(dataReportConfig)
#case20
def UpdateProgressMissionFull(day,users):
    resetDataReportConfig()
    claimAll()
    closeAllEvent()
    data1 = {
      "UpdateFull": "Fail",
      "UpdateAgain": "Fail",
    }
    #cheat gan hoan thanh nhiem vu
    cheatNumMision(user[users]["id"],challengePlay[challenge[day]["mission"]]["data"]["totalX"]-1)
    reloadLobby()
    claimAll()
    closeAllEvent()
    eventWCOpen()
    prog1=checkProgressCurrent()
    closeEvent()
    print(prog1)
    checkMission2(day)
    #check update progess
    touch(imageWC.imgCar)
    prog2=checkProgressCurrent()
    if checkUpdateProgessTable(prog1,prog2):
        dataReportConfig["UpdateFull"]="Pass"
    else:
        dataReportConfig["UpdateFull"]="Fail"
#     clickOutTable()
    sleep(5)
    eventWCOpen()
    prog3=checkProgressCurrent()
    closeEvent()
    checkMission2(day)
    #check update progess
    touch(imageWC.imgCar)
    prog4=checkProgressCurrent()
    if checkUpdateProgessTable(prog3,prog4):
        dataReportConfig["UpdateAgain"]="Fail"
    else:
        dataReportConfig["UpdateAgain"]="Pass"
    #------------------------#
    #report
    reportUpdateProgressMissionFull(dataReportConfig)
#case21
def checkDisconect():
    try:
        killApp()
        openApp()
        sleep(20)
        poco = CocosJsPoco()  
        clear()
        poco = CocosJsPoco()
        claimAll()
        closeAllEvent()
        joinTable()
        checkProgress()
        clickOutTable()
    except:
        print("fail")
#case22
def GuiDeal(users):
    resetDataReportConfig()
    sleep(5)
    claimAll()
    closeAllEvent()
    changeAcc(user[users]["user"],user[users]["pass"])
    claimAll()
    closeDealSpec()
    if  CheckGUIEvent() :
        dataReportConfig['GuiEvent']="Fail"
        closeEvent()
    else:
        dataReportConfig['GuiEvent']="Pass"
    if  CheckGUIDeal():
        dataReportConfig['GuiEDeal']="Fail"
        closeEvent()
    else:
        dataReportConfig['GuiEDeal']="Pass"
    gold1=getGold(user[users]["id"])
    clickGuiDeal()
    cheatBuyDeal(user[users]["id"],1)
    clickClaim()
    sleep(1)
    if checkDisableBtnBuy(1):
        dataReportConfig['BtnBuyWC']="Pass"
    else:
        dataReportConfig['BtnBuyWC']="Fail"
    closeEvent()
    gold2=getGold(user[users]["id"])
    clickGuiDeal()
    goldConf=0
    if waitNoLimit(imageWC.imageOfferDeal,2):
        goldConf=dealWCConfig["offerWC1"]["gold"]
    else:
        goldConf=dealWCConfig["offerWC1"]["gold1"]
    closeEvent()
    if checkUpdateGold(goldConf,gold1,gold2):
        dataReportConfig['GoldUpdate']="Pass"
    else:
        dataReportConfig['GoldUpdate']="Fail"
    clickGuiDeal()
    cheatBuyDeal(user[users]["id"],2)
    sleep(1)
    clickClaim()
    cheatBuyDeal(user[users]["id"],2)
    sleep(1)
    clickClaim()
    sleep(1)
    cheatBuyDeal(user[users]["id"],3)
    sleep(1)
    clickClaim()
    cheatBuyDeal(user[users]["id"],3)
    sleep(1)
    clickClaim()
    if checkBtnDeal():
        dataReportConfig['BtnDeal']="Fail"
    else:
        dataReportConfig['BtnDeal']="Pass"
    #report
    reportDeal(dataReportConfig)
#case23
def endEvent(day,users):
    #change Accout 1
    resetDataReportConfig()
    claimAll()
    closeAllEvent()
    changeAcc(user[users]["user"],user[users]["pass"])
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
    sleep(2)
    claimAll()
    closeAllEvent()
    #---------end reload lobby--------------------------
    #check gold init
    goldInit=getGold(user[users]["id"])
    sleep(1)
    #opent GUI event
    eventWCOpen()
    #check gold claim
    to=checkTocos()
    goldClaim=to*challengePlay[challenge[day]["mission"]]["data"]["gold"]
    #wait pass day
    sleep(30)
    #check close GUI
    if CheckGUIEvent():
        dataReportConfig['GUIEvent']="Fail"
        closeEvent()
    else:
        dataReportConfig['GUIEvent']="Pass"
    #check gold
    goldAfter=getGold(user[users]["id"])
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
def win(day,users):
    try:
        resetDataReportConfig()
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
        cheatGold(user[users]["id"],1000000)
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
            dataReportConfig["Update1"]="Fail"
        else:
            dataReportConfig["Update1"]="Pass"
#         clickOutTable()
        #check lobby
        CheckLobby()
        print("fc win")
    except:
        print("error win")
    print(dataReportConfig)
    reportWin(dataReportConfig)
def win1(day):
    try:
        claimAll()
        closeAllEvent()
        clear()
        cheatGold(user["user1"]["id"],1000000)
        reloadLoby2()
        claimAll()
        closeAllEvent()
        #click btn play
        joinTable()
        #cheat cheatPorkerSpecial
        CheatCard(cardCheat[challengePlay[challenge[day]["mission"]]["data"]["type"]]["card"], cardCheat[challengePlay[challenge[day]["mission"]]["data"]["type"]]["set"])
        #add bot
        addBot()
        #Click knock
        clickKnock()
        clickOutTable()
        #wait end game
        waitEndGame2()
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
#full house
def full1(day):
    try:
            claimAll()
            closeAllEvent()
            clear()
            cheatGold(user["user1"]["id"],1000000)
            reloadLoby2()
            claimAll()
            closeAllEvent()
            #click btn play
            joinTable()
            #cheat cheatPorkerSpecial
            CheatCard(cardCheat[challengePlay[challenge[day]["mission"]]["data"]["type"]]["card"], cardCheat[challengePlay[challenge[day]["mission"]]["data"]["type"]]["set"])
            #add bot
            addBot()
            #Click knock
            clickKnock()
            clickOutTable()
            #wait end game
            waitEndGame2()
    except:
            print("error win")
    #-- ----------------#
#check
#check button event
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
#check noti cho event
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
#dem time
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
#dem tiem trong ban
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
#check nhiem vu tung ngay la nhiem vu gi
def checkMission(day,user):
    if challenge[day]["mission"]=="win":
        return win(day,user)
#     if challenge[day]["mission"]=="play":
#         return play(day)
    if challenge[day]["mission"]=="knock":
        return knock(day,user)
    if challenge[day]["mission"]=="exchange1":
        return exchange1(day,user)
    if challenge[day]["mission"]=="collect":
        return collect(day,user)
#check va thuc hien nhiem vu rut gon
def checkMission2(day):
    if challenge[day]["mission"]=="win":
        return win1(day)
    if challenge[day]["mission"]=="play":
        return "play"
    if challenge[day]["mission"]=="knock":
        return "knock"
    if challenge[day]["mission"]=="exchange1":
        return "exchange1"
    if challenge[day]["mission"]=="full":
        return full1(day)
#check an btn deal khi mua het deal
def checkDisableBtnDeal():
    try:
        if waitNolimitPoco(pocoTag.btnOfferEventTB,1):
            print("check CheckGUIDeal")
            clear()
            return False
        else:
            return True
    except:
        print("check CheckGUIDeal no exists")
        return True 
#check an btn buy sau khi mua het goi
def checkDisableBtnBuy(offer):
    try:
        if waitNolimitPoco(poco("lbPrice"+str(offer)),1):
            print("check purchased")
            clear()
            return False
        else:
            clear()
            return True
    except:
        print("check check purchased no exists")
        return False 
#check thong bao khong du tien
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
#check nhiem vu ngay
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
#check tien do hien tai
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
#check thanh progess
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
#check thanh progess trong ban choi
def checkProgessTable():
    try:
        if waitNolimitPoco(pocoTag.btnMain,5):
            print("Progess table")
            return 1 
        else:
            print("Progess no show table")
            return 0
        clear()
    except:
        return 0 
        print("error Progess table")
#check show thanh progess trong ban choi
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
#check update tien trinh
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
#check gui event WC
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
#check gui deal
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
#check btn deal
def checkBtnDeal():
    try:
        if waitNolimitPoco(poco("btnOfferEventTB"),1):
            print("check CheckGUIDeal")
            return True
        else:
            return False
    except:
        print("check CheckGUIDeal no exists")
        return False
#check show nhiem vu ngay nao
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
        clear()
    except:
        return False
#check tocos hien co
def checkTocos():
    try:
        if waitNolimitPoco(pocoTag.lbNumTacos,2):
#             tocos=int(pocoTag.lbNumTacos.get_text())
            tocos=int(poco("lbNumTacos").get_text())
            return tocos
    except:
        return False
#check update tocos
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
#check update gold
def checkUpdateGold(gold1, gold2, gold3):
    try:
        print(gold1)
        print(gold2)
        print(gold3)
        claim= float(gold1)
        update= gold3 - gold2
        print(update)
        if update == claim :
            if fortmatGold(gold3)==checkGold():
                print("Gold update")
                return True
            else:
                return False
        else:
            print("gold update false")
            return False
    except:
        print("Gold update error")
        return False 
#check nhiem vu khong hoan thanh
def checkMissedMission(day):
    try:
        mission="TBNodeDay"+str(day)
        if waitNolimitPoco(poco(mission),2):
            return poco(mission).offspring("imgMissed").attr("visible")
        else:
            return False
    except:
        return False
#check nhiem vu hoan thanh
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
#mo event
def eventWCOpen():
    try:
        poco = CocosJsPoco()
        clear()
        if waitNolimitPoco(pocoTag.btnMain,5):
            pocoTag.btnMain.click()
            pocoTag.btnMain.invalidate()
            print("event WC")
            return True
    except:
        print("error event WC")
        return False
#nhan qua hoan thanh nhiem vu
def clickClaimMission():
    try:
        if waitNolimitPoco(pocoTag.btnJoin,1):
            pocoTag.btnJoin.click()
            pocoTag.btnJoin.invalidate()
            return True
        else:
            return False
    except:
        return False
#chon thuc hien nhiem vu trong GUI
def joinMission():
    try:
        poco = CocosJsPoco()
        pocoTag.btnJoin.click()
        return True
    except:
        return False
#mo GUI deal
def clickGuiDeal():
    try:
        if waitNolimitPoco(pocoTag.btnOfferEventTB,10):
            pocoTag.btnOfferEventTB.click()
            clear()
            return True
        else:
            return False
    except:
        return False
#dong pop-up deal dac biet
def closeDealSpec():
    try:
        if waitNoLimit(imageWC.imgEventSpec,2):
            pocoTag.btnClose.click()
            clear()
            return True
        else:
            return False
    except:
        return False
#dong pop-up deal dac biet2
def closeDealSpec1():
    try:
        if waitNoLimit(imageWC.imgDealSpec,2):
            poco("btnClose").click()
            return True
        else:
            return False
    except:
        return False
#dong pop-up show thuong vip
def closeNotiVip():
    try:
        if waitNoLimit(imageWC.imgVipBag,1):
            pocoTag.btnClose.click()
            return True
        else:
            return False
    except:
        return False
#18/12/2020: 00:00:00 /1608224400000
#19/12/20210 00:00:00 /1608310800000
#20/12/2020 00:00:00 /1608397200000
#20/12/2020 23:00:00 /1608480000000
#21/12/2020 00:00:00 /1608483600000
#21/12/2020 23:00:00 /1608566400000
#21/12/2020 23:59:50 /1608569990000
#23/12/2020 00:00:00 /1608656400000
#24/12/2020 00:00:00 /1608742800000
#25/12/2020 00:00:00 /1608829200000
#26/12/2020 00:00:00 /1608915600000
#27/12/2020 00:00:00 /1609002000000

time_db=[
{"Y":2020,"M":11,"D":4,"h":17,"m":50,"s":0}, 
{"Y":2020,"M":11,"D":6,"h":0,"m":0,"s":0},
{"Y":2020,"M":11,"D":6,"h":23,"m":59,"s":50},  
{"Y":2020,"M":11,"D":7,"h":23,"m":0,"s":0},    
{"Y":2020,"M":11,"D":8,"h":0,"m":0,"s":0},     
{"Y":2020,"M":11,"D":8,"h":23,"m":0,"s":0},   
{"Y":2020,"M":11,"D":8,"h":23,"m":59,"s":50}, 
{"Y":2020,"M":11,"D":10,"h":0,"m":0,"s":0},    
{"Y":2020,"M":11,"D":11,"h":0,"m":0,"s":0},   
{"Y":2020,"M":11,"D":12,"h":0,"m":0,"s":0},
{"Y":2020,"M":11,"D":13,"h":0,"m":0,"s":0},
{"Y":2020,"M":11,"D":14,"h":0,"m":0,"s":0}
]
def convertDayTime(time):
    dt = datetime(time['Y'],time['M'],time['D'],time['h'],time['m'],time['s'])
    milliseconds = int(round(dt.timestamp() * 1000))
    print(milliseconds)
    return milliseconds  
#convertDayTime(time_db1)
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
def get_user_id():
    touch(image_vip.btn_profile)
    time.sleep(4)
    return pocoTag.ibID.get_text()
def close_info():
    time.sleep(1)
    pocoTag.btn_closeInfo.click()
    time.sleep(1)
def log_in():
    pocoTag.btnSwitch.click()
    pocoTag.inputUser.click()
    text("ngoctu92")
    pocoTag.inputPass.click()
    text("12345678")
    pocoTag.btnLogin.click()
    time.sleep(3)
def log_out():
    try:
        poco("btnPlay").exists
    except:
        print("Please back to lobby page!")
    else:
        print("Success!")
    poco("iconSetting").click()
    poco("bgLobbyLayer2").click()
    touch(imageInOutAcc.imgOutOk)
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
    text("ngoctu92")
    pocoTag.inputPass.click()
    text("12345678")
    pocoTag.btnRegister.click()  
    time.sleep(3)
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
s=0
def bonus_day_1(s):
    dataDaily= {
        "status": "False",
        "detail": ""
    }
    if btn_claim_exit(pocoTag.btnClaim)==True:
        dataDaily["status"]="True"
        dataDaily["detail"]="Show GUI daily bonus day 1 success!"
        time.sleep(3)
        pocoTag.btnClaim.click()  
        pocoTag.btnClaim.click()
        goldNewbie=gold_number()
        s+=1
        if goldNewbie ==40000:
            print("Update gold day 1 true")
            dataDaily["status"]="True"
            dataDaily["detail"]="Update gold day 1 true"
        else:
            print("Update gold false!")
            dataDaily["status"]="False"
            dataDaily["detail"]="Update gold day 1 false"
        report_Gold_dailybonus(dataDaily)
    else: 
        print("khong auto show Gui daily bonus sau play tutorial")
        dataDaily["status"]="False"
        dataDaily["detail"]="Dont show GUI dayly bonus day 1"
    report_GUI_dailybonus(dataDaily)
    return s 
def claim_bonus_true(config,s,user):
    dataDaily= {
        "status": "False",
        "detail": ""
    }
    time.sleep(3)
    if btn_claim_exit(pocoTag.btnClaim)==True:
        print("Nhan bonus day success!")
        gold_befor= getGold(userID)
        pocoTag.btnClaim.click()
        gold_after= getGold(user)
        dataDaily["status"]="True"
        dataDaily["detail"]="Show GUI daily bonus True!"
        s+=1
        if config ==gold_after - gold_befor:
            print("Update gold true")
            dataDaily["status"]="True"
            dataDaily["detail"]="Update gold true"
        else:
            print("Update gold false!")
            dataDaily["status"]="False"
            dataDaily["detail"]="Wrong config gold update"
        report_Gold_dailybonus(dataDaily)
    else:
        print("Dont show GUI bonus day")
        dataDaily["status"]="False" 
        dataDaily["detail"]="Dont show GUI daily bonus when enough 24h"
    report_GUI_dailybonus(dataDaily)
    return s
def claim_bonus_false(config,s,user):
    dataDaily= {
        "status": "False",
        "detail": ""
    }
    time.sleep(3)
    if btn_claim_exit(pocoTag.btnClaim)==True:
        print("Nhan bonus day success!")
        gold_befor= getGold(user)
        pocoTag.btnClaim.click()
        gold_after= getGold(user)
        dataDaily["status"]="False"
        dataDaily["detail"]="Show GUI daily bonus when not enough 24h!"
        s+=1
        if config ==gold_after - gold_befor:
            print("Update gold true")
            dataDaily["status"]="True"
            dataDaily["detail"]="Update gold true"
        else:
            print("Update gold false!")
            dataDaily["status"]="False"
            dataDaily["detail"]="Wrong config gold update"
        report_Gold_dailybonus(dataDaily)
    else:
        dataDaily["status"]="True" 
        dataDaily["detail"]="Dont show GUI daily bonus when not enough 24h!"
    report_GUI_dailybonus(dataDaily)
    return s  
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
    if pocoTag.btnSwitch.exists():
        data["status"]="true"
        print("check in lobby!")
    else:
        print ("Please go to Login page")

#9. Kiểm tra có show GUI daily bonus khi dung o lobby cho nhan bonus
def check_show_GUI():
    api_changeTimeServer(1608397200000)
    reloadLobby()
#12. Vào playing game-> Chờ qua 24h rồi ra lại lobby( Ngày 4)
def playing_24h():
    time.sleep(3)
    pocoTag.btnPlay.click()
    api_changeTimeServer(convertDayTime(time_db[4]))
    time.sleep(3)
    pocoTag.btnLeaveGame.click()
    time.sleep(3)   
#14. Đứng chờ ở GUI daily bonus 23h
def GUI_bonus_23h(s):
    api_changeTimeServer(convertDayTime(time_db[5]))
    reloadLobby()
    s=claim_bonus_false(DailyBonus["day5"],s,userID) 
    pocoTag.btnDaily.click()
def close_Gui_daily():
    if pocoTag.btnTomorrow.exists():
        pocoTag.btnTomorrow.click()
def GUI_bonus_24h():
    api_changeTimeServer(convertDayTime(time_db[6]))
    reloadLobby()
    time.sleep(10)
#16 Nhận bonus 5 lần-> Log out-> Login sau 24h nhưng không nhận bonus->Login lại sau 24h tiếp theo

#kill app vào lại sau 24h
# kill_app()
# start_app()
#check an btn Daily bonus ở lobby khi đã nhận đủ 7 lần
def checkCompleteBonus(s):
    i=9
    while s<7:
        api_changeTimeServer(convertDayTime(time_db[i]))
        clear()
        time.sleep(4)
        if btn_claim_exit(pocoTag.btnClaim)==True:
            pocoTag.btnClaim.click()
            s+=1
        else:
            print("Dont show")
        if i<11:
            i+=1
        else:
            break
        print(s)
    else:
        print("da nhan du 7 ngay")
def checkIconDaily():
    if btn_claim_exit(pocoTag.btnDaily)==True:
        print("Dont auto hide daily bonus icon when hasclaimed 7 day enough on lobby screen ")
    else:
        print("Auto hide daily bonus icon success!")
#19. Ra lại lobby-> đứng ở lobby chờ sau 24
def complete_lobby_24h():
    dataDaily= {
        "status": "False",
        "detail": "",
    }
    api_changeTimeServer(convertDayTime(time_db[11]))
    reloadLobby()
    clear()
    sleep(3)
    if btn_claim_exit(pocoTag.btnClaim)==True:
        pocoTag.btnClaim.click()
        print("Show daily bonus GUI when has claimed 7 day")
        dataDaily["status"]="False"
        dataDaily["detail"]="Lobby: Still show GUI dayly bonus over day 7"
    else:
        print("Dont shoe daily bonus GUI when has claimed 7 day!")
        dataDaily["status"]="True"
        dataDaily["detail"]="Lobby: Dont show GUI dayly bonus over day 7"
    report_GUI_dailybonus(dataDaily)
#20. Log out-> Login lại sau 24h
def complete_logout_login_24h():
    dataDaily= {
        "status": "False",
        "detail": "",
    }
    clear()
    log_out()
    log_in() 
    time.sleep(3)
    if btn_claim_exit(pocoTag.btnClaim)==True:
        pocoTag.btnClaim.click()
        print("Show daily bonus GUI when has claimed 7 day")
        dataDaily["status"]="False"
        dataDaily["detail"]="Login: Still show GUI dayly bonus over day 7"
    else:
        print("Dont shoe daily bonus GUI when has claimed 7 day!")
        dataDaily["status"]="True"
        dataDaily["detail"]="Login: Dont show GUI dayly bonus over day 7"
    report_GUI_dailybonus(dataDaily)
# changeAcc(user["user2"]["user"],user["user2"]["pass"])
def afterBT():
    try:
        timeBT={
            "start":{"Y":2020,"M":11,"D":18,"h":13,"m":0,"s":0},
            "end":{"Y":2021,"M":1,"D":5,"h":7,"m":0,"s":0}
        }
         #Cheat time-------------#02/12/2020 23:59:00 -> 1606928340000
        timeCheat = api_changeTimeServer(1605051600000)
    #     timeCheat = api_changeTimeServer(timeC["timeD0"]["mili"])
        dayS = {
            "Y": timeBT["start"]['Y'],
            "M": timeBT["start"]['M'],
            "D": timeBT["start"]['D'],
            "h": timeBT["start"]['h'],
            "m": timeBT["start"]['m'],
            "s": timeBT["start"]['s']
        }
        timeNow=convertDayTimeToMili(dayS) -housToMili(1)+ minutetoMili(59)+secToMili(30)
        timeCheat = api_changeTimeServer(timeNow)
        reloadLobby()
        sleep(2)
        claimAll()
        closeAllEvent()
        eventWCOpen()                  
        if waitNoLimit(BT.noti,10):
            print("check noti event")
        sleep(25)
        eventWCOpen()
        if waitNolimitPoco(poco("rewardContainer"),3):
            print("Home BT")
        else:
            print("No home BT")
    except:
        print("no check noti event")
def tut():
#     eventWCOpen()
    sleep(5)
    for x in range(2):
        poco.click([0.94378074490513, 0.875])
        sleep(10)
    sleep(2)
    poco.click([0.9508081517919887, 0.109375])
    if waitNoLimit(BT.dealBT,2):
        print("Tut fail")
    poco.click([0, 1])
    if waitNolimitPoco(poco("sprChap1"),2):
        print("Tut fail")
    poco("btnTut5").click()
    claimAll()
    closeAllEvent()        
