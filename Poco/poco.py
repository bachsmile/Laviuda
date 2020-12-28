
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
class poco:
    # changeacc
    poco("btnSwitch")
    poco("Image_4")
    poco("logo")
    poco("Image_4_0")
    poco("logo")
    poco("btnLogin")
    poco("btnSetting")
    #buttn X close
    poco("btnClose")
    #reload
    poco("btnPlay")
    poco("btnLeaveGame")
    #hide trong close avatar
    poco("btnHide") 
    #btn event
    poco("btnMain")
    #noti event
    poco("<no-name>").offspring("layer_7")[0].child("<no-name>")[0]
    poco(text="NOTIFICACIONES")
    #btn cheat
    poco(name="lbTime")
    poco("btnCheat")
    poco("btnAddBot")
    poco("lbTimeServer")
    poco("btnSendCheatPlayer")
    #btn join in event
    poco("btnJoin")
    poco("btnClaim")
    #WC lable
    poco(text="Hoy")
    poco(text="Día 1")
    poco(text="Día 2")
    poco(text="Día 3")
    poco(text="Día 4")
    poco(text="Día 5")
    poco(text="Día 6")
    poco(text="Día 7")
    poco("lbNumTacos")
    poco("lbProgress")
    #gold
    poco(name="lbGold")
    #deal WC
    poco("btnOfferEventTB")
    poco("imgTruck")
    #action game
    poco("btnPass")
    poco("btnKnock")
    poco("btnExchange1")
    poco("btnSwap")
    poco("btnExchange5")
    #game
    poco("bg_table")
#------------------------------------------VIP-----------------------------------------------#
class poco:
    btn_vip = poco("btnVip")
    btn_play = poco("btnPlay")
    btn_cheat = poco("btnCheat")
    btn_add_bot = poco("btnAddBot")
    btn_send = poco("btnSendCheatPlayer")
    btn_setting = poco("btnSetting")
    bg_logout = poco("bgLobbyLayer2")
    btn_switch = poco("btnSwitch")
    input_name = poco("Image_4")
    input_pass = poco("Image_4_0")
    btn_login = poco("btnLogin")
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

