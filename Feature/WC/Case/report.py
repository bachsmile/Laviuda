#---------------------------------------------Tile----------------------------------------#

__author__ = "pc"

#---------------------------------------------End Tile------------------------------------#
#---------------------------------------------Link------------------------------------#
# from Lavuavi.Feature.WC.Case.report import *
#---------------------------------------------End Link------------------------------------#
#---------------------------------------------Import LIB-------------------------------------------------#
import json
from datetime import datetime
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.cocosjs import CocosJsPoco

#---------------------------------------------End Import Lib---------------------------------------------#

#---------------------------------------------Import FILE------------------------------------------------#
from Lavuavi.Config.config import *

#---------------------------------------------End Import FILE--------------------------------------------#

#---------------------------------------------Connect Device---------------------------------------------#

if not cli_setup():
#------------------Android---------------------------------#
    auto_setup(__file__)

#------------------Android---------------------------------#

#------------------NOX-------------------------------------#
#     auto_setup(__file__, logdir=True, devices=[
#             "Windows:///197680",
#     ])
#------------------NOX-------------------------------------#

#------------------------------------------End Connect---------------------------------------------------#

#------------------------------------------Poco----------------------------------------------------------#

    poco = CocosJsPoco()

#------------------------------------------End Poco------------------------------------------------------#
#------------------------------------------script content-------------------------------------------------------------------#
#------------------------------------------bien----------------------------------------------------------#

#------------------------------------------end bien------------------------------------------------------#
#------------------------------------------Report------------------------------------------------------------------------#
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
      "Time": data["Time"],
      "Status": data["Status"],
      "Button": data["Button"],
      "Befor":data["Befor"],
      "Coutdown":data["Coutdown"],
      "ShowBtnJoin":data["ShowBtnJoin"],
      "After":data["After"],
      "Time1": data["Time1"],
      "Status1": data["Status1"],
      "KillApp":data["KillApp"],
      "Login":data["Login"],
      "Progess":data["Progess"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Test btn sau thoi gian show event
    
            Time :                                  {0}    Status cheat time 1p befor event:{1}
            
            Show Button event:                      {2}
            
            Click btn befor event show noti:        {3}
            
            Wait coutdown:                          {4}
            
            Show btn join event:                    {5}
            
            Click btn after event:                  {6}
            
            Time:                                   {7}    Status cheat time 1p befor event:{8}
            
            Kill App:                               {9}
            
            Login account 2:                        {10}
            
            Show Progess:                           {11}
            
            
                                                                time test: {12}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["Time"], detail["Status"], detail["Button"], detail["Befor"], detail["Coutdown"], detail["ShowBtnJoin"], detail["After"], detail["Time1"], detail["Status1"], detail["KillApp"], detail["Login"], detail["Progess"], current_time)
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
          "Lobby": data["Lobby"],
          "CheatFM": data["CheatFM"],
          "Reload": data["Reload"],
          "GuiEvent": data["GuiEvent"],
          "Claim": data["Claim"],
          "UpdateGold": data["UpdateGold"]
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Claim gift finished mission
    
            Chờ ra lobby:                           {0}    
            
            Cheat finished mission:                 {1}    
            
            Reload lobby:                           {2}    
            
            Show GUI event                          {3}
            
            Claim Gift:                             {4}
            
            Update gold :                           {5}      
            
            
            
                                                                time test: {6}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["Lobby"], detail["CheatFM"], detail["Reload"], detail["GuiEvent"], detail["Claim"], detail["UpdateGold"], current_time)
    f = open("log.txt", 'w+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#NoClaimGift
def reportNoClaimGift(data):
    detail={
          "Lobby": data["Lobby"],
          "CheatFM": data["CheatFM"],
          "Reload": data["Reload"],
          "GuiEvent": data["GuiEvent"],
          "CloseGUI": data["CloseGUI"],
          "UpdateGold": data["UpdateGold"]
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Claim gift finished mission
    
            Chờ ra lobby:                           {0}    
            
            Cheat finished mission:                 {1}    
            
            Reload lobby:                           {2}    
            
            Show GUI event                          {3}
            
            Close GUI event:                        {4}
            
            Update gold :                           {5}      
            
            
            
                                                                time test: {6}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["Lobby"], detail["CheatFM"], detail["Reload"], detail["GuiEvent"], detail["CloseGUI"], detail["UpdateGold"], current_time)
    f = open("log.txt", 'w+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#reportAutoClaim
def reportAutoClaim(data):
    detail={
          "GuiEvent": data["CheatFM"],
          "Effect": data["CheatFM"],
          "Tick": data["CheatFM"],
          "MissionNew": data["CheatFM"],
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
    f = open("log.txt", 'w+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#passClaimGift
def reportPassClaimGift(data):
    detail={
          "ChangeAcc":  data["ChangeAcc"],
          "GUIEvent":  data["GUIEvent"],
          "Auto":  data["Auto"],
          "Tick":  data["Tick"],
          "UpdateMission":  data["UpdateMission"]
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Claim gift finished mission
    
            Change acc 1                            {0}
            
            Auto show GUI event:                    {1}     
                          
            Show effect auto claim:                 {2}    
            
            Tick claim gift:                        {3}
            
            Update mission new:                     {4}
            
            
                                                                time test: {5}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["ChangeAcc"], detail["GUIEvent"], detail["Auto"], detail["Tick"], detail["UpdateMission"], current_time)
    f = open("log.txt", 'w+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#reportChangeAcc
def reportChangeAcc(data):
    detail={
          "Lobby": data["Lobby"],
          "ChangeAcc": data["ChangeAcc"],
          "GuiEvent": data["GuiEvent"],
          "MissionDay1": data["MissionDay1"],
          "CloseGUI": data["CloseGUI"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Claim gift finished mission
    
            Chờ ra lobby:                           {0}    
                          
            Change Account:                         {1}    
            
            Show GUI event                          {2}
            
            Nhiem vu Day1 acc2 khong hoan thanh:    {3}
            
            Close event :                           {4}      
            
            
            
                                                                time test: {5}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["Lobby"], detail["ChangeAcc"], detail["GuiEvent"], detail["MissionDay1"], detail["CloseGUI"], current_time)
    f = open("log.txt", 'w+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#reportUpdateMissionTable
def reportUpdateMissionTable(data):
    detail = {
      "CheatFM": data["CheatFM"],
      "CheatTime": data["CheatTime"],
      "TimeCheat": data["TimeCheat"],
      "Reload": data["Reload"],
      "CloseGUI": data["CloseGUI"],
      "BtnPlay": data["BtnPlay"],
      "Bot": data["Bot"],
      "MissionNew": data["MissionNew"],
      "Leave": data["Leave"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Claim gift finished mission
    
            Cheat finished mission:                 {0}     
                          
            Cheat time qua ngay:                    {1}    Time cheat:                          {2}   
            
            Reload lobby:                           {3}
            
            Close GUI event:                        {4}
            
            Click btn play:                         {5}    Add bot                              {6}    
            
            Update nhiem vu ngay moi                {7}
            
            Leave table:                            {8}
            
            
                                                                time test: {9}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["CheatFM"], detail["CheatTime"], detail["TimeCheat"], detail["Reload"],  detail["CloseGUI"], detail["BtnPlay"], detail["Bot"], detail["MissionNew"], detail["Leave"], current_time)
    f = open("log.txt", 'w+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#reportUpdateMissionLobby
def reportUpdateMissionLobby(data):
    detail = {
      "CheatFM": data["CheatFM"],
      "CheatTime": data["CheatTime"],
      "TimeCheat": data["TimeCheat"],
      "Reload": data["Reload"],
      "TimeW": data["TimeW"],
      "MissionNew": data["MissionNew"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Claim gift finished mission
    
            Cheat finished mission:                 {0}     
                          
            Cheat time qua ngay:                    {1}    Time cheat:                          {2}   
            
            Reload lobby:                           {3}
            
            Wait time pass day:                     {4}               
            
            Update nhiem vu ngay moi                {5}
            
            
            
                                                                time test: {6}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["CheatFM"], detail["CheatTime"], detail["TimeCheat"], detail["Reload"],  detail["TimeW"], detail["MissionNew"],  current_time)
    f = open("log.txt", 'w+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#reportUpdateProgressMissionFull
def reportUpdateProgressMissionFull(data):
    detail = {
      "CheatFOM": data["CheatFOM"],
      "CheatCard": data["CheatCard"],
      "Bot": data["Bot"],
      "UpdateFull": data["UpdateFull"],
      "UpdateAgain": data["UpdateAgain"],
    }
    report = """
    -----------------------------------------------------------------------------------------------------------
    
    CASE: Claim gift finished mission
    
            Cheat gan hoan thanh nhiem vu:          {0}     
                          
            Cheat bộ 4 lá WC:                       {1}    
                
            Add bot:                                {2}   
            
            Update progress full:                   {3}
            
            Again no update progress:               {4}                           
            
            
            
                                                                time test: {5}
                                                                Reporter: BachTX
    ----------------------------------------------------------------------------------------------------------
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format( detail["CheatFOM"], detail["CheatCard"], detail["Bot"], detail["UpdateFull"],  detail["UpdateAgain"],  current_time)
    f = open("log.txt", 'w+')
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
def reportDeal(data):
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
    
    CASE: Test mission Exchange1
            
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
    log=report.format( detail["Login"],detail["GuiEvent"], detail["GuiEDeal"], detail["BtnBuyWC"], detail["Update"], detail["GoldUpdate"], detail["BtnDeal"], current_time)
    f = open("log.txt", 'a+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#Report init
def reportInit(detail,report):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log=report.format(detail["Time"], detail["Status"], detail["Button"],current_time)
    f = open("log.txt", 'w+')
    f.write(log)
    print(type(log))
    f.close()
#--------------------------------------------------------------------------------------------------------#
#Clear report
def clearReport():
    report=""
    f = open("log.txt", 'w+')
    f.write(report)
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
          "Reload": "Fail",
          "GuiEvent": "Fail",
          "GuiEDeal": "Fail",
          "CheatFOM": "Fail",
          "Bot": "Fail",
          "Knock": "Fail",
          "Exchange1":"Fail",
          "BtnBuyWC":"Fail",
          "GoldUpdate":"Fail",
          "BtnDeal":"Fail",
          "Login":"Fail"
        }
#--------------------------------------------------------------------------------------------------------#
#---------------------------------------------End script--------------------------------------------------------------------#
#---------------------------------------------Report-----------------------------------------------------#
#File report
#---------------------------------------------End Report-------------------------------------------------#