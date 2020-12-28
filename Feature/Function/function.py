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
from Lavuavi.Config.Api import *
#----------------------------------------------------------#
from Lavuavi.Config.config import *
from Lavuavi.Report.report import *
from Lavuavi.Img.img import *
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
    #KillApp
def killApp():
try:
    clear_app("com.zingplay.laviuda")
    print('kill App')
    return True
except:
    print('error kill App')
    return False
    #openApp
def openApp():
    try:
        start_app("com.zingplay.laviuda")
        print('open App')
        return True
    except:
        print('error open App')
        return False
#Function DB:---------------------->
#Function VIP:--------------------->
#Function WC:---------------------->
#-------------------------------------------------------------------------------------#

