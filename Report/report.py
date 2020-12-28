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
from Lavuavi.Config.config import *
from Lavuavi.Report.report import *
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
#Function WC:---------------------->
#-------------------------------------------------------------------------------------#

