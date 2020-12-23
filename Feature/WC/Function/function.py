# -*- encoding=utf8 -*-
#--------------Tile----------------------------------------#

__author__ = "pc"

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
from Lavuavi.Feature.WC.Case.report import *
from Lavuavi.Img.img import *
#--------------End Import FILE-----------------------------#
#--------------Connect Device------------------------------#

if not cli_setup():
    auto_setup(__file__)
    
#--------------End Connect---------------------------------#
#--------------Poco----------------------------------------#

# poco = CocosJsPoco()

#--------------End Poco------------------------------------#
# script content
#--------------bien----------------------------------------#

#-------------end bien-------------------------------------#
#-----------------------------------------------------------------#
def beforEvent():
#     Data1={
#       "Time": timeC["timeD0"]["data"],
#       "Status": "Fail",
#       "Button": "Fail"
#     }
    print(dataReportConfig)
    clearReport()
    #Cheat time-------------24/11/2020 6:00:00----------
    timeCheat = api_changeTimeServer(1605051600000)
    timeCheat = api_changeTimeServer(timeC["timeD0"]["mili"])
    dataReportConfig["TimeCheat"]=timeC["timeD0"]["data"]
    if timeCheat ==200:
        dataReportConfig['CheatTime']="Pass"
    else:
        dataReportConfig['CheatTime']="Fail"
    #End Cheatime---------------------------------------
    #changeAcc
#     changeAcc(user["user0"]["user"],user["user0"]["pass"])
#     sleep(5)
#     poco("btnClose").click()
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
#-----------------------------------------------------------------#
def afterEvent():
    Data1 = {
      "Time": "01/01/2020 00:00:00",
      "Status": "Fail",
      "Button": "Fail",
      "Befor": "Fail",
      "Coutdown": "Fail",
      "ShowBtnJoin": "Fail",
      "After": "Fail",
      "Time1": "01/01/2020 00:00:00",
      "Status1": "Fail",
      "KillApp": "Fail",
      "Login": "Fail",
      "Progess": "Fail"
    }
    poco = CocosJsPoco()
    sleep(2)
#-------------In Game-------------------------------------------------#
    #-------------Cheat time-----------------------------------#
    #26/11/2020 06:59:00
    timeCheat = api_changeTimeServer(1605051600000)
    timeCheat = api_changeTimeServer(timeC["timeD02"]["mili"])
    Data1["Time"]=timeC["timeD02"]["data"]
    if timeCheat:
        Data1['Status']="Pass"
    else:
        Data1['Status']="Fail"
    #-------------End Cheatime---------------------------------#
    #reload lobby------------------------------
    sleep(2)
    reloadLobby()
    if waitNolimitPoco(poco("btnClose"),1):
          poco("btnClose").click()
#     clickClaim()
    reloadLoby2()
    # poco("btnClaim").click()
 #Check event--------------------------------------------------#
    #Check btn event -----------------------------------
    if CheckBtnEvent():
        Data1["Button"]="Pass"
        try:
            poco = CocosJsPoco()
            #Join event
            eventWCOpen()
            #Check noti event befor event---------------
            if CheckNotiEvent():
                Data1['Befor']="Pass"
                #Open pop-up wait event
                if coutDownTime()==1:
                    sleep(1)
                    Data1["Coutdown"]="Pass"
                else:
                    Data1["Coutdown"]="Fail"
                #Join event
                if eventWCOpen():
                    sleep(1)
                    Data1["After"]="Pass"
                else:
                    Data1["After"]="Fail"
                sleep(1)
                closeEvent()
                #cheat time back 1p
                #26/11/2020 06:59:20
                timeCheat = api_changeTimeServer(1605051600000)
                timeCheat = api_changeTimeServer(timeC["timeD01"]["mili"])
                Data1["Time1"]=timeC["timeD01"]["data"]
                if timeCheat:
                    Data1['Status1']="Pass"
                else:
                    Data1['Status1']="Fail"
                sleep(1)
                #kill app
                if killApp():
                    Data1['KillApp']="Pass"
                else:
                    Data1['KillApp']="Fail"
                #open app
                sleep(2)
                openApp()
                #wait
                sleep(20)
                CheckLobby()
                #changeAcc
                if  changeAcc(user["user1"]["user"],user["user1"]["pass"]):
                    Data1['Login']="Pass"
                    CheckLobby()
                    #join table wait
                    joinTable()
                    #wait event
                    coutDownTimeIntable()
                    #back to lobby
                    backToLobby()
                    poco("btnClose").click()
                    #join event
                    eventWCOpen()
                else:
                    Data1['Login']="Fail"
        except:
            print('btnMain no find')
    else:
        Data1["Button"]="Fail"
    #end Check btn event--------------------------------
  #end check event---------------------------------------------#
#End in Game----------------------------------------------------------#
#-------------End script----------------------------------#
#-------------Report--------------------------------------#
    reportAfterEvent(Data1)
#-----------------------------------------------------------------#
def day1():
    #join event
    eventWCOpen()
    #Check enable ngay 1 va nhiem vu ngay 1
    if waitNoLimit(imgDay.tabDay1,5):
        dataDay1["Tab"]="Pass"
        print("ton tai day 1")
    else:
        dataDay1["Tab"]="Fail"
        print("error day1")  
    if waitNolimitPoco(challengePlay[challenge["day1"]["mission"]]["data"]["detailMission"],5):
        dataDay1["Mission"]="Pass"
        print("nv day1")
    else:
        dataDay1["Mission"]="Fail"
        print("error day1")
    print(dataDay1)
    closeEvent()
     #------------------------#
    #report
    reportDay1(dataDay1)
    checkMission("day1")
#-----------------------------------------------------------------#
def day2():
    #resetDataReport
    resetDataReportConfig()
    #cheat time pass 1 ngay-> 27/11/2020 11:11:11
    timeCheat = api_changeTimeServer(1605051600000)
    timeCheat = api_changeTimeServer(timeC["timeD2"]["mili"])
    dataReportConfig["TimeCheat"]=timeC["timeD2"]["data"]
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
    clickClaim()
    closeEvent()
    closeEvent()
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
#-----------------------------------------------------------------#
def day3():
        #resetDataReport
    resetDataReportConfig()
    #------------------------#
    #report
    reportDay3(dataReportConfig)
    #------------------------#
    checkMission("day3")
#-----------------------------------------------------------------#
def GuiDeal():
#     if  changeAcc(user["user1"]["user"],user["user1"]["pass"]):
#         dataReportConfig['Login']="Fail"
#     else:
#         dataReportConfig['Login']="Pass"
#     if  CheckGUIEvent() :
#         dataReportConfig['GuiEvent']="Fail"
#         closeEvent()
#     else:
#         dataReportConfig['GuiEvent']="Pass"
    #close Gui Event
#     if waitNolimitPoco(poco("btnClaim"),2):
#         poco("btnClaim").click()
#     if  CheckGUIDeal():
#         dataReportConfig['GuiEDeal']="Pass"
#         closeEvent()
#     else:
#         dataReportConfig['GuiEDeal']="Fail"
    gold1=checkGold()
    clickGuiDeal()
    cheatBuyDeal(user["user2"]["id"],1)
    clickClaim()
    if checkDisableBtnDeal():
        dataReportConfig['BtnBuyWC']="Fail"
    else:
        dataReportConfig['BtnBuyWC']="Pass"
    closeEvent()
    gold2=checkGold()
    if checkUpdateGold(dealWCConfig["offerWC1"]["gold"],gold1,gold2):
        dataReportConfig['GoldUpdate']="Pass"
    else:
        dataReportConfig['GoldUpdate']="Fail"
    cheatBuyDeal(user["user2"]["id"],2)
    sleep(1)
    cheatBuyDeal(user["user2"]["id"],3)
    clickClaim()
    if checkBtnDeal():
        dataReportConfig['BtnDeal']="Pass"
    else:
        dataReportConfig['BtnDeal']="Fail"
    #report
    reportDeal(dataReportConfig)
    #------------------------#
#-----------------------------------------------------------------#
    #------------------------#
#-----------------------------------------CODE FUNCTION LIB----------------------------------------------------#
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
    lenght = len(strGold)-1
    return strGold[0:lenght]
#--------------------------------------------------------------------------------------------------------#
#cheat
def cheatGoldEmpty(gold):
    try:
        poco("btnCheat").click()
        if exists(Template(r"tpl1608102257956.png", record_pos=(0.186, 0.083), resolution=(2400, 1080))):
            touch(Template(r"tpl1608102257956.png", record_pos=(0.186, 0.083), resolution=(2400, 1080)))
        else:
            touch(Template(r"tpl1608102303058.png", record_pos=(0.184, 0.083), resolution=(2400, 1080)))
        text(gold)
        poco("btnSendCheatPlayer").click()
        poco("btnCheat").click()
        print("cheat gold success")
        return True
    except:
        print("Error cheat gold")
        return False
def cheatNumMision(num,idU):
        try:
            a = api_postDoFunction(idU, "CHEAT_NUM_OBTAIN_MISSION", [num])
            print(a)
            print("cheat cheatFinishedMision success")
            return True
        except:
            print("Error cheatFinishedMision")
            return False
#reload lobby
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
def reloadLoby2():
    poco = CocosJsPoco()
    poco.click([0.04817596456992819, 0.9241753578186035])
    poco("btnHide").click()
def backToLobby():
    try:
        poco = CocosJsPoco()
        if waitNoLimit(imgBack,2):
            touch(imgBack)
            return True
        if waitNolimitPoco(poco("btnLeaveGame"),1):
            poco("btnLeaveGame").click()
            return True
        if waitNolimitPoco(poco("btnHide"),1):
            poco("btnHide").click()
            return True
#         if waitNolimitPoco(poco("btnClose"),1):
#             poco("btnClose").click()
#             return True
    except:
        print("error backToLobby")
def CheckLobby():
    try:
        if waitNolimitPoco(poco("btnPlay"),60):
            print("check back lobby")
            return True
        else:
            print("back lobby fail")
            return False
    except:
        print("error back lobby")
        return False
#Guievent
def CheckBtnEvent():
    try:
#         if waitNolimitPoco(poco("btnMain"),10):
        if waitNoLimit(imgDay.imgBtnEvent,5):
            return True
        else:
            return False
    except:
        print("error btn event")
        return False
def eventWCOpen():
    try:
        poco = CocosJsPoco()
        poco("btnMain").click()
        print("event WC")
        return True
    except:
        print("error event WC")
        return False
def closeEvent():
    try:
        sleep(1)
        if waitNolimitPoco(poco("btnClose"),1):
            poco("btnClose").click()
    except:
        print("error close ev")
def CheckNotiEvent():
    try:
        if poco("<no-name>").offspring("layer_7")[0].child("<no-name>")[0].attr("type")=="ImageView":
            print("check noti event")
            return True
        else:
            print("check noti event no exists")
            return False
    except:
        print("check noti event no exists")
        return False
#login
def changeAcc(userN,passW):
    try:
        out()
        poco = CocosJsPoco()
        poco("btnSwitch").click()
        poco("Image_4").click()
        sleep(1)
        text("")
        poco("Image_4").click()
        sleep(1)
        User=str(userN)
        text(User)
        poco("logo").click()
        poco("Image_4_0").click()
        PassW=str(passW)
        text(PassW)
        poco("logo").click()
        poco("btnLogin").click()
        return True
    except:
        print("error login")
        return False
def out():
    try:
        poco = CocosJsPoco()
        poco("btnSetting").click()
        sleep(1)
        wait(imgLogin.imgBtnOut)
        touch(imgLogin.imgBtnOut)
        touch(imgLogin.imgOutOk)
        print("out")
    except:
        print("error out")
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
#wait
def coutDownTime():
    cout=65
    while 1:
        sleep(1)
        cout-=1
        time=poco(name="lbTime").attr("text")
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
            return 0
            break
        if exists1(poco("btnMain")):
            print("show")
            return 1
            break
def waitEndGame():
    try:
        poco = CocosJsPoco()
#       if waitNolimitPoco(poco("imgOtherWin"),100):  
        if waitNoLimit(imgPlay.imgWin,100):
            print(0)
            print("end game")
            return True
        else:
            print("end time down")
            return False
    except:
        print("error")
        return False
#check
def checkMission(day):
    if challenge[day]["mission"]=="win":
        return win(day)
    if challenge[day]["mission"]=="play":
        return play(day)
    if challenge[day]["mission"]=="knock":
        return knock(day)
    if challenge[day]["mission"]=="exchange1":
        return exchange1(day)
def checkProgessTable():
    try:
        if waitNolimitPoco(poco("btnMain"),5):
            print("Progess table")
            return 1 
        else:
            print("Progess no show table")
            return 0
    except:
        return 0 
        print("error Progess table")
def checkNotiNoEnoughGold():
    try:
        if waitNolimitPoco(poco(text="NOTIFICACIONES"),5):
            print('Noti no enough gold')
            poco.click([0.49964862965565704, 0.6496874809265136])
            return True
        else:
            print('no show Noti no enough gold')
            return False
    except:
        print("error show enough gold")
        return False
def tableGame():
    try:
        if waitNolimitPoco(poco("bg_table"),10):
            print("table play")
            return True
        else:
            print("end countdown time")
            return False
#         print(exists1(poco("bg_table")))
    except:
        print("error table play")
        return False
def CheckGUIEvent():
    try:
        if waitNolimitPoco(poco("imgTruck"),5):
            print("check CheckGUIEvent")
            return True
        else:
            return False
    except:
        print("check CheckGUIEvent no exists")
        return False
def CheckGUIDeal():
    try:
        if waitNoLimit(imgDeals.imgDeal,5):
            print("check CheckGUIDeal")
            return True
        else:
            return False
    except:
        print("check CheckGUIDeal no exists")
        return False
def CheckLableDay():
    try:
#         poco(text="Tocar ")poco(text=" 4  veces  ")poco(text="Hoy")poco(text="Día 1")
        if waitNolimitPoco(poco(text="Día 1"),1):
               print("Día 1")
        else:
            if waitNolimitPoco(poco(text="Hoy"),1):
                return 1
            else:
                return False
        if waitNolimitPoco(poco(text="Día 2"),1):
            print("Día 2")
        else:
            if waitNolimitPoco(poco(text="Hoy"),1):
                return 2
            else:
                return False
        if waitNolimitPoco(poco(text="Día 3"),1):
            print("Día 3")
        else:
            if waitNolimitPoco(poco(text="Hoy"),1):
                return 3
            else:
                return False
        if waitNolimitPoco(poco(text="Día 4"),1):
            print("Día 4")
        else:
            if waitNolimitPoco(poco(text="Hoy"),1):
                return 4
            else:
                return False
        if waitNolimitPoco(poco(text="Día 5"),1):
            print("Día 5")
        else:
            if waitNolimitPoco(poco(text="Hoy"),1):
                return 5
            else:
                return False
        if waitNolimitPoco(poco(text="Día 6"),1):
            print("Día 6")
        else:
            if waitNolimitPoco(poco(text="Hoy"),1):
                return 6
            else:
                return False   
        if waitNolimitPoco(poco(text="Día 7"),1):
            print("Día 7")
        else:
            if waitNolimitPoco(poco(text="Hoy"),1):
                return 7
            else:
                return False
    except:
        return False
def checkProgressCurrent():
    try:
        if waitNolimitPoco(poco("lbProgress"),5):
            progress=poco("lbProgress").get_text()
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
def checkShowProgessTable():
    try:
        if waitNoLimit(imgPlay.imgProgessBarON,10):
            print("Progess show on table")
            return True 
        else:
            print("Progess no show on table")
            return False
    except:
        return False 
        print("error Progess table")
def checkGold():
    numGold = poco(name="lbGold").attr("text")
    return pipeSubGold(numGold)
def checkUpdateGold(gold1, gold2, gold3):
    try:
        claim= float(gold1)
        update= float(gold3) - float(gold2)
        if update == claim :
            print("Gold update")
            return True
        else:
            print("gold update false")
            return False
    except:
        print("Gold update error")
        return False
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
def checkDisableBtnDeal():
    try:
        if waitNolimitPoco(poco("btnOfferEventTB"),1):
            
            print("check CheckGUIDeal")
            return False
        else:
            return True
    except:
        print("check CheckGUIDeal no exists")
        return True    
#action
def joinTable():
    try:
        sleep(2)
        poco = CocosJsPoco()
        poco("btnPlay").click()
        print("joinTable")
        return 1
    except:
        print("error joinTable")
        return 0
def clickOutTable():
    try:
        poco("btnLeaveGame").click()
        print("register back")
        return True
    except:
        print("error register back")
        return False
def joinMission():
    try:
        poco = CocosJsPoco()
        poco("btnJoin").click()
        return True
    except:
        return False
def addBot():
    try:
        poco = CocosJsPoco()
        poco("btnCheat").click()
        for i in range(2):
            sleep(1)
            poco("btnAddBot").click()
        poco("btnCheat").click()
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
def clickExchange1():
    try:
        if waitNolimitPoco(poco("btnExchange1"),60):
            poco("btnExchange1").click()
            sleep(1)
            poco.click([0.6264933239634575, 0.8615635156631469])
            sleep(1)
            poco.click([0.6602340558843552, 0.4599999904632568])
            sleep(1)
            poco("btnSwap").click()
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
        if waitNolimitPoco(poco("btnExchange5"),60):
            poco("btnExchange5").click()
            return True
        else:
            return False
    except:
        return False
def clickGuiDeal():
    try:
        if waitNolimitPoco(poco("btnOfferEventTB"),10):
            poco("btnOfferEventTB").click()
            return True
        else:
            return False
    except:
        return False
def clickClaim():
    try:
        if waitNolimitPoco(poco("btnClaim"),1):
            poco("btnClaim").click()
            return True
        else:
            return False
    except:
        return False
#mission
def win(day):
    try:
        print("wwwwin")
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
        if checkUpdateProgessTable():
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
def play():
    print("fc play")
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
    except:
        print("error knock")
    print(dataReportConfig)
    reportKnock(dataReportConfig)
def exchange1(day):
    try:
        #join event
        eventWCOpen()
        #check progress
        prog1=checkProgressCurrent()
        print(prog1)
        closeEvent()
        cheatGold(user["user2"]["id"],1000000) 
        #click btn play
        if joinTable():
            dataReportConfig["BtnPlay"]="Pass"
        else:
            data1["BtnPlay"]="Fail"
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
#-----------------------------------------------------------------#
    #-------------End Report--------------------------------------#
day2()
# checkBtnDeal()
# print(waitNolimitPoco(poco("btnBuyOffer2"),1))

# checkUpdateProgessTable(1,3)
# waitNolimitPoco(poco("progressToday"),100)
# a = api_postDoFunction("19130214", "CHEAT_PAYMENT_VIP", ["vip.pack_1"]);