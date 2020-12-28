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
def reportdailybonus():
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
    log=report.format(detail["Time"], detail["Status"], detail["Button"],current_time)
    f = open("logDailyBonus.txt", 'w') #tạo mới file log
    f.write(log) #viết file log 
    print(type(log)) #in ra kiểu dữ liệu của type
    f.close()      #kết thúc
#Function DB:---------------------->
#Function VIP:--------------------->
#Function WC:---------------------->
#-------------------------------------------------------------------------------------#

