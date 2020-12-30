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
#-------------------------------------------------------------------------------------#

