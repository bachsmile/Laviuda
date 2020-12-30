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
def afterEvent():
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
    dayS['h'] = dayS['h']-1
    dayS['m'] = dayS['m']+59
    dayS['s'] = dayS['s']+40
    timeCheat = api_changeTimeServer(convertDayTimeToMili(dayS))
    dataReportConfig["TimeCheat"]=fortmartTime(dayS)
    print(dayS)
    print(timeWC["start"])
    if timeCheat ==200:
        dataReportConfig['CheatTime']="Pass"
    else:
        dataReportConfig['CheatTime']="Fail"
    #-------------End Cheatime---------------------------------#
    #reload lobby------------------------------
    sleep(2)
    reloadLobby()
    if waitNolimitPoco(pocoTag.btnClose,1):
          closeEvent()
#     clickClaim()
    reloadLoby2()
    # poco("btnClaim").click()
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
    #join event
    eventWCOpen()
    #Check enable ngay 1 va nhiem vu ngay 1
    if waitNoLimit(imgDay.tabDay1,5):
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
    dayS['D'] = dayS['D']+1
    timeCheat = api_changeTimeServer(convertDayTimeToMili(dayS))
    dataReportConfig["TimeCheat"]=fortmartTime(dayS)
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
def day3():
        #resetDataReport
    resetDataReportConfig()
    #------------------------#
    #report
    reportDay3(dataReportConfig)
    #------------------------#
    checkMission("day3")
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
    goldClaim=0
    #check update gold
    goldAfter=checkGold()
    if checkUpdateGold(goldClaim,goldInit,goldAfter):
        dataReportConfig['GoldUpdate']="Pass"
    else:
        dataReportConfig['GoldUpdate']="Fail"
    #End in Game----------------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportNoClaimGift(dataReportConfig)
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

