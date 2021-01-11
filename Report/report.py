#--------------Tile----------------------------------------#
__author__ = "QC"
__title__ ="List Report"
__desc__="""
    Tong hop danh sach cac Fortmart report
"""
#--------------End Tile------------------------------------#
#--------------Import LIB----------------------------------#
import json
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.cocosjs import CocosJsPoco
#--------------End Import Lib------------------------------#
#--------------Import FILE---------------------------------#
#----------------------------------------------------------#
from Laviuda.Config.config import *
from Laviuda.Report.report import *
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
    #Report init
def reportInit(detail,report):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format(detail["Time"], detail["Status"], detail["Button"],current_time)
    f = open("log.txt", 'w+')
    f.write(log)
    print(type(log))
    f.close()
#Clear report
def clearReport():
    report=""
    f = open("log.txt", 'w+')
    f.write(report)
    f.close()
#Function DB:---------------------->
#Function VIP:--------------------->
#Case1: Open vip
def reportCheckOpenVip(data):
    detail = {
        "Status" : data["Status"]
    }
    report = """
    -----------------------------------------------------------------------------
    Case1: Open Vip
            Status check: {0}
                                    
                                    
                                    Time test: {2}
    -----------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format(detail["Status"], current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()

data_report = {
    "Status" : "Fail"
}
#Case2: Open Vip nhưng không mua
def reportCheckPackVip(data):
    detail = {
        "Status" : data["Status"]
    }
    report = """
    -----------------------------------------------------------------------------
    Case1: Check Pack Vip
            Status check: {0}
                                    
                                    
                                    Time test: {2}
    -----------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format(detail["Status"], current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()

#Function WC:---------------------->
#BeforEvent
def reportBeforEvent(data):
    detail = {
      "TimeCheat": data["TimeCheat"],
      "CheatTime": data["CheatTime"],
      "Button": data["Button"]
    }
    report = """
    -----------------------------------------------------------------------------
    
    CASE: Test btn truoc thoi gian show event
    
            Time :{0}       Status cheat:{1}
            
            Khong show Button event:{2}
                                                                time test: {3}
    
    -----------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format(detail["TimeCheat"], detail["CheatTime"], detail["Button"],current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#AfterEvent
def reportAfterEvent(data):
    detail = {
      "TimeCheat": data["TimeCheat"],
      "CheatTime": data["CheatTime"],
      "Befor":data["Befor"],
      "Coutdown":data["Coutdown"],
      "ShowBtnJoin":data["ShowBtnJoin"],
      "After":data["After"],
      "TimeCheat1": data["TimeCheat1"],
      "CheatTime1": data["CheatTime1"],
      "ShowProg":data["ShowProg"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Test btn sau thoi gian show event
    
            Time :                                  {0}    Status cheat time 1p befor event: {1}
            
            Click btn befor event show noti:        {2}
            
            Wait coutdown:                          {3}
            
            Click btn after event:                  {4}
            
            Show btn join event:                    {5}
            
            Time:                                   {6}    Status cheat time 1p befor event: {7}
            
            Show Progess:                           {8}
            
            
                                                                time test: {9}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["TimeCheat"], detail["CheatTime"],detail["Befor"], detail["Coutdown"],detail["After"], detail["ShowBtnJoin"],  detail["TimeCheat1"], detail["CheatTime1"], detail["ShowProg"], current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#Day1
def reportDay1(data):
    detail = {
      "Tab": data["Tab"],
      "Mission": data["Mission"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Test mission Day 1
    
            Tab Day1 enable:                        {0}    Nhiem vu Day 1 show:                 {1}
            
                                                                 time test: {2}
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["Tab"], detail["Mission"],current_time)
    f = open("log.txt", 'w+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#Day2
def reportDay2(data):
    detail = {
      "CheatTime": data["CheatTime"],
      "TimeCheat": data["TimeCheat"],
      "Reload": data["Reload"],
      "GuiEvent": data["GuiEvent"],
      "GuiEDeal": data["GuiEDeal"],
      "Tab": data["Tab"],
      "Mission": data["Mission"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Test mission Day 2
    
            Cheat time qua ngay:                    {0}    Time cheat:                          {1}
            
            Reload lobby:                           {2}    
            
            Auto show GUI event:                    {3}    Auto show GUI deal:                  {4}
            
            Tab Day 2 enable:                       {5}    Nhiem vu Day 2 show:                 {6}
                     
                                                                    time test: {7}

    """
#                                                                 Reporter: BachTX
#     ----------------------------------------------------------------------------------------------------------
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["CheatTime"], detail["TimeCheat"], detail["Reload"], detail["GuiEvent"], detail["GuiEDeal"], detail["Tab"], detail["Mission"],current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#Day3
def reportDay3(data):
    detail = {
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Test mission Day 3                           
                                                                time test: {0}
                ------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format(current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#Day4
def reportDay4(data):
    detail = {
      "BtnPlay": data["BtnPlay"],
      "CheatCard": data["CheatCard"],
      "Bot": data["Bot"],
      "Knock":data["Knock"],
      "ChooseLeave":data["ChooseLeave"],
      "Update":data["Update"],
      "Leave":data["Leave"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Test mission Day 4
    
            Click btn Play:                         {0}    
            
            Cheat 4 card WC:                        {1}    
            
            Add bot:                                {2}    
            
            Knock:                                  {3}    
            
            Choose Leave table:                     {4}           
            
            Show update progess:                    {5}
            
            Leave table:                            {6}
            
            
                                                                time test: {7}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["BtnPlay"], detail["CheatCard"], detail["Bot"], detail["Knock"], detail["ChooseLeave"],detail["Update"], detail["Leave"], current_time)
    f = open("log.txt", 'w+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#Day5
def reportDay5(data):
    detail = {
      "CheatTime": data["CheatTime"],
      "TimeCheat": data["TimeCheat"],
      "Reload": data["Reload"],
      "OpenGUI":data["OpenGUI"],
      "BtnPlay":data["BtnPlay"],
      "Win":data["Win"],
      "Update":data["Update"],
      "Lose": data["Lose"],
      "NoUpdate":data["NoUpdate"],
      "Leave":data["Leave"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Test mission Day 5
    
            Cheat time qua ngay:                    {0}    Time cheat:                          {1}
            
            Reload lobby:                           {2}    
            
            Open GUI event:                         {3}    Click btn play Join table:            {4}
            
            Play win:                               {5}    Show update progess:                  {6}
            
            Play lose:                              {7}    No Show update progess:               {8}

            Leave table:                            {9}
            
            
                                                                time test: {10}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["CheatTime"], detail["TimeCheat"], detail["Reload"], detail["OpenGUI"], detail["BtnPlay"], detail["Win"], detail["Update"], detail["Lose"], detail["NoUpdate"], detail["Leave"], current_time)
    f = open("log.txt", 'w+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#Day6
def reportDay6(data):
    detail = {
      "CheatTime": data["CheatTime"],
      "TimeCheat": data["TimeCheat"],
      "Reload": data["Reload"],
      "OpenGUI":data["OpenGUI"],
      "BtnPlay":data["BtnPlay"],
      "CheatCard": data["CheatCard"],
      "Update":data["Update"],
      "Leave":data["Leave"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Test mission Day 6
    
            Cheat time qua ngay:                    {0}    Time cheat:                          {1}
            
            Reload lobby:                           {2}    
            
            Open GUI event:                         {3}    Click btn play Join table:           {4}
            
            Cheat card Mission:                     {5}   
            
            Show update progess:                    {6}
            
            Leave table:                            {7}
            
            
                                                                time test: {8}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["CheatTime"], detail["TimeCheat"], detail["Reload"], detail["OpenGUI"], detail["BtnPlay"], detail["CheatCard"], detail["Update"], detail["Leave"], current_time)
    f = open("log.txt", 'w+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#Day7
def reportDay7(data):
    detail = {
      "CheatTime": data["CheatTime"],
      "TimeCheat": data["TimeCheat"],
      "HideProgress": data["HideProgress"],
      "Leave":data["Leave"],
      "GuiEvent":data["GuiEvent"],
      "Claim":data["Claim"],
      "UpdateGold":data["UpdateGold"],
      "ChangeAccout ": data["ChangeAccout"],
      "CheckGift": data["CheckGift"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Test mission Day 7
    
            Cheat time qua ngay:                    {0}    Time cheat:                          {1}
            
            Hide progress bar:                      {2}    
            
            Leave table:                            {3}
            
            Auto show GUI event:                    {4}    Claim Gift:                          {5}
            
            Update gold :                           {5}    
            
            Change accout miss all day mission:     {6}    Check gift:                          {7}    
            
            
            
                                                                time test: {8}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["CheatTime"], detail["TimeCheat"], detail["HideProgress"], detail["Leave"], detail["GuiEvent"], detail["Claim"], detail["UpdateGold"], detail["ChangeAccout"], detail["CheckGift"], current_time)
    f = open("log.txt", 'w+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#ClaimGift
def reportClaimGift(data):
    detail={
          "CheatFM": data["CheatFM"],
          "GuiEvent": data["GuiEvent"],
          "GoldUpdate": data["GoldUpdate"],
          "UpdateTocos": data["UpdateTocos"]
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Claim gift finished mission   
            
            Cheat finished mission:                 {0}     
            
            Show GUI event                          {1}
                    
            Update gold :                           {2}   
            
            Update Tocos:                           {3}
            
            
                                                                time test: {4}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["CheatFM"], detail["GuiEvent"], detail["GoldUpdate"], detail["UpdateTocos"], current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#NoClaimGift
def reportNoClaimGift(data):
    detail={
          "GoldUpdate": data["GoldUpdate"]
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Hoan thanh mission dong GUI khong nhan
    
            Khong nhan qua :                           {0}      
            
            
            
                                                                time test: {1}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format(detail["GoldUpdate"], current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#reportAutoClaim
def reportAutoClaim(data):
    detail={
          "GuiEvent": data["GuiEvent"],
          "Effect": data["Effect"],
          "Tick": data["Tick"],
          "MissionNew": data["MissionNew"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Claim gift finished mission
    
            Auto show GUI event:                    {0}     
                          
            Show effect:                            {1}    
            
            Tick claim gift:                        {2}
            
            Update mission new:                     {3}
            
            
                                                                time test: {4}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["GuiEvent"], detail["Effect"], detail["Tick"], detail["MissionNew"], current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#passClaimGift
def reportPassClaimGift(data):
    detail={
          "GUIEvent":  data["GUIEvent"],
          "UpdateTocos":  data["UpdateTocos"],
          "Tick":  data["Tick"],
          "MissionNew":  data["MissionNew"]
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Claim gift finished mission
            
            Auto show GUI event:                    {0}     
                          
            Auto claim :                            {1}    
            
            Tick claim gift:                        {2}
            
            Update mission new:                     {3}
            
            
                                                                time test: {4}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["ChangeAcc"], detail["GUIEvent"], detail["UpdateTocos"], detail["Tick"], detail["MissionNew"], current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#reportChangeAcc
def reportChangeAcc(data):
    detail={
          "MissionDay1": data["MissionDay1"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Claim gift finished mission
            
            Nhiem vu Day1 acc2 khong hoan thanh:    {0}
            
            
            
                                                                time test: {1}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["MissionDay1"],current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#reportUpdateMissionTable
def reportUpdateMissionTable(data):
    detail = {
      "MissionNew": data["MissionNew"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Qua ngay khi dang trong ban
            
            Update nhiem vu ngay moi                {0}

            
            
                                                                time test: {1}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format(detail["MissionNew"], current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#reportUpdateMissionLobby
def reportUpdateMissionLobby(data):
    detail = {
      "MissionNew": data["MissionNew"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Qua ngay khi dang mo gui event
            
            Update nhiem vu ngay moi                {0}

            
            
                                                                time test: {1}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format(detail["MissionNew"], current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#reportUpdateProgressMissionFull
def reportUpdateProgressMissionFull(data):
    detail = {
      "UpdateFull": data["UpdateFull"],
      "UpdateAgain": data["UpdateAgain"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Claim gift finished mission 
            
            Update progress full:                                           {0}
            
            Again no update progress after full progress bar:               {1}                           
            
            
            
                                                                time test: {2}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format(detail["UpdateFull"],  detail["UpdateAgain"],  current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#Knock
def reportKnock(data):
    detail = {
      "Mission": data["Mission"],
      "BtnPlay": data["BtnPlay"],
      "JoinTable":data["JoinTable"],
      "CheatFOM": data["CheatFOM"],
      "Bot": data["Bot"],
      "Knock": data["Knock"],
      "Update":data["Update"],
      "Leave":data["Leave"],
    }
    report = """
            ---------------------------------------------------------------------------------------
    
    CASE: Test mission Knock
            
            Click btn play:                         {0}    Vao table:                           {1}
            
            Cheat finished obtain mission:          {2}    Add bot                              {3}
            
            Wait den luot thi click knock           {4}
            
            Show update progess:                    {5}
            
            Leave table:                            {6}
            
            
                                                                time test: {7}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format(detail["BtnPlay"], detail["JoinTable"], detail["CheatFOM"],detail["Bot"],detail["Knock"], detail["Update"], detail["Leave"], current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#Win
def reportWin(data):
    detail = {
      "CheatGold0": data["CheatGold0"],
      "OpenGUI":data["OpenGUI"],
      "BtnPlay0":data["BtnPlay0"],
      "CheatGold1":data["CheatGold1"],
      "BtnPlay1":data["BtnPlay1"],
      "Progess": data["Progess"],
      "CheatFOM": data["CheatFOM"],
      "Update":data["Update"],
      "Leave":data["Leave"],
    }
    report = """
            -------------------------------------------------------------------------------------------
    
    CASE: Test mission Win
            
            Cheat gold = 0:                         {0}    
            
            Open GUI event:                         {1}    Click btn play show noti:            {2}
            
            Cheat gold = 1M:                        {3}    Click btn play Join table:           {4}
            
            Show progess bar:                       {5}    
            
            Cheat finished obtain mission:          {6}
            
            Show update progess:                    {7}
            
            Leave table:                            {8}
            
            
                                                                time test: {9}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format(detail["CheatGold0"], detail["OpenGUI"], detail["BtnPlay0"], detail["CheatGold1"], detail["BtnPlay1"], detail["Progess"], detail["CheatFOM"], detail["Update"], detail["Leave"], current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#Exchange1
def reportExchange1(data):
    detail = {
      "BtnPlay": data["BtnPlay"],
      "Bot": data["Bot"],
      "Exchange1": data["Exchange1"],
      "Update":data["Update"],
      "ChooseLeave":data["ChooseLeave"],
      "NoUpdate":data["NoUpdate"],
      "Leave":data["Leave"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Test mission Exchange1
    
            Click btn Play:                         {0}    
            
            Add bot:                                {1}
            
            Exchange1:                              {2}    
            
            Show update progess:                    {3}    
            
            Choose Leave table:                     {4}    
            
            No update progess bar at end game:      {5}    
            
            Leave table:                            {6}
            
            
                                                                time test: {7}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["BtnPlay"], detail["Bot"], detail["Exchange1"], detail["Update"], detail["ChooseLeave"], detail["NoUpdate"], detail["Leave"], current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#Exchange1
def reportEndEvent(data):
    detail = {
      "GUIEvent": data["GUIEvent"],
      "UpdateGold": data["UpdateGold"],
      "Button": data["Button"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Test mission end event
    
            Auto đóng event:                        {0}    
            
            No claim gift:                          {1}
            
            Ẩn event:                               {2} 
            
                                                                time test: {3}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["GUIEvent"],detail["UpdateGold"], detail["Button"], current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#Exchange1
def reportDeal(data):
    print(data)
    detail = {
      "Login":data["Login"],
      "GuiEvent": data["GuiEvent"],
      "GuiEDeal": data["GuiEDeal"],
      "BtnBuyWC": data["BtnBuyWC"],
      "GoldUpdate":data["GoldUpdate"],
      "BtnDeal":data["BtnDeal"]
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Test mission Deal
            
            Login again                             {0}
            
            Khong show Gui event:                   {1}    
            
            Khong show Gui Deal:                    {2}
            
            Button buy disiable:                    {3}    
            
            Gold update:                            {4}    
            
            Button Deal hide:                       {5}    
            
           
                                                                time test: {6}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["Login"],detail["GuiEvent"], detail["GuiEDeal"], detail["BtnBuyWC"],detail["GoldUpdate"], detail["BtnDeal"], current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
def resetDataReportConfig():
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
        "ShowBtnJoin":"Fail"
        }
def reportdailybonus(data):
    detail = {
        "Time": data["Time"],
        "status": data["status"],
        "button": data["button"]
    }   # các chi tiết cần in ra ở file log
    report = """ 
    -----------------------------------------------------------------------------
    
    CASE: TESR DAILY BOMUS
    
            Time :{0}       Status:{1}
            
            Show Button:{2}
                                                                time test: {3}
    
    -----------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") #log ra ngày hien tại
    log=report.format(detail["Time"], detail["status"], detail["button"],current_time)
    f = open("logDailyBonus.txt", 'w') #tạo mới file log
    f.write(log) #viết file log 
    print(type(log)) #in ra kiểu dữ liệu của type
    f.close()      #kết thúc
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------#


