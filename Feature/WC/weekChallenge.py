
#--------------Tile----------------------------------------#

__author__ = "pc"

#--------------End Tile------------------------------------#
#--------------Import LIB----------------------------------#
import json
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.cocosjs import CocosJsPoco
#--------------End Import Lib------------------------------#
#--------------Import FILE---------------------------------#

# from test.Autotest.Lavuavi.Image.imgWC.ImgWC import *
#link cheat:
from test.Autotest.Lavuavi.Function.Cheat.Cheat.Api import *
from test.Autotest.Lavuavi.Function.Cheat.Cheat.FinishedMision import *
#----------------------------------------------------------#
from test.Autotest.Lavuavi.Feature.WC.Function.function import *
#--------------End Import FILE-----------------------------#
#--------------Connect Device------------------------------#

if not cli_setup():
    auto_setup(__file__)
    
#--------------End Connect---------------------------------#
#--------------Poco----------------------------------------#

poco = CocosJsPoco()

#--------------End Poco------------------------------------#
#--------------FT1----------------------------------------------------------#
beforEvent()
#--------------FT1----------------------------------------------------------#
    #End in Game----------------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportPassClaimGift(Data1)
    #-------------End Report--------------------------------------#
#--------------End-FT3----------------------------------------------------------#