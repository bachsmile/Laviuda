
#---------------------------------------------Tile-------------------------------------------------------#
__author__ = "QC"
__title__ ="List Poco"
__desc__="""
    Tong hop danh sach cac poco in game
"""
#---------------------------------------------End Tile---------------------------------------------------#
#---------------------------------------------Import LIB-------------------------------------------------#
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.cocosjs import CocosJsPoco
#---------------------------------------------End Import Lib---------------------------------------------#
#---------------------------------------------Link-------------------------------------------------------#
from Lavuavi.Poco.poco import *
#---------------------------------------------Link-------------------------------------------------------#

#---------------------------------------------Import FILE------------------------------------------------#

#---------------------------------------------End Import FILE--------------------------------------------#

#---------------------------------------------Connect Device---------------------------------------------#
if not cli_setup():
    auto_setup(__file__)
#------------------------------------------End Connect---------------------------------------------------#

#------------------------------------------Poco----------------------------------------------------------#
poco = CocosJsPoco() 
#------------------------------------------End Poco------------------------------------------------------#
#------------------------------------------script content------------------------------------------------#
#------------------------------------------bien----------------------------------------------#
x=0
#------------------------------------------end bien------------------------------------------#
#------------------------------------------WC------------------------------------------------#

#------------------------------------------WC------------------------------------------------#
#------------------------------------------VIP-----------------------------------------------#

#------------------------------------------VIP-----------------------------------------------#
#------------------------------------------DB------------------------------------------------#
class poco:
    btn_google= poco("btnGooglePlus")
    btn_switch= poco("btnSwitch")
    btn_claim= poco("btnClaim")
    btn_play= poco("btnPlay")
    btn_facebooknormal= poco("btnFacebookNormal")
    image_4= poco("Image_4") #input user name
    image_4_0= poco("Image_4_0")  #input pass
    btn_register= poco("btnRegister")
    btn_tomorrow= poco("btnTomorrow")
    btn_leavegame= poco("btnLeaveGame")
    btn_daily= poco("btnDaily")
    icon_setting= poco("iconSetting")
    lobby_layer2= poco("bgLobbyLayer2") 
    btn_guest= poco("btnGuest")
#------------------------------------------DB------------------------------------------------#
#---------------------------------------------End script--------------------------------------------------------------------#
#---------------------------------------------Report-----------------------------------------------------#
#File report
#---------------------------------------------End Report-------------------------------------------------#