
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
#------------------------------------------end bien------------------------------------------#
#------------------------------------------WC------------------------------------------------#
#------------------------------------------WC------------------------------------------------#
class pocoTag:
    # changeacc
    btnSwitch = poco("btnSwitch")
    inputUser = poco("Image_4")
    logo = poco("logo")
    inputPass = poco("Image_4_0")
    btnLogin = poco("btnLogin")
    btnSetting = poco("btnSetting")
    #buttn X close
    btnClose = poco("btnClose")
    #reload
    btnPlay = poco("btnPlay")
    btnLeaveGame = poco("btnLeaveGame")
    #hide trong close avatar
    btnHide = poco("btnHide") 
    #btn event
    btnMain = poco("btnMain")
    #noti event
    notiShow = poco("<no-name>").offspring("layer_7")[0].child("<no-name>")[0]
    NOTIFICACIONES = poco(text="NOTIFICACIONES")
    #btn cheat
    lbTime = poco(name="lbTime")
    btnCheat = poco("btnCheat")
    btnAddBot = poco("btnAddBot")
    lbTimeServer = poco("lbTimeServer")
    btnSendCheatPlayer = poco("btnSendCheatPlayer")
    btnSendCustom = poco("btnSendCustom")
    btnTabCustom = poco("btnTabCustom")
    btnResetCustom = poco("btnResetCustom")
    pnPointEvent = poco("pnPointEvent")
    pnCaseId_1 = poco("pnCaseId_1")
    #btn join in event
    btnJoin = poco("btnJoin")
    btnClaim = poco("btnClaim")
    #WC lable
    lbDayCurrent = poco(text="Hoy")
    lbDay1 = poco(text="Día 1")
    lbDay2 = poco(text="Día 2")
    lbDay3 = poco(text="Día 3")
    lbDay4 = poco(text="Día 4")
    lbDay5 = poco(text="Día 5")
    lbDay6 = poco(text="Día 6")
    lbDay7 = poco(text="Día 7")
    lbNumTacos = poco("lbNumTacos")
    lbProgress = poco("lbProgress")
    #gold
    lbGold = poco(name="lbGold")
    #deal WC
    btnOfferEventTB = poco("btnOfferEventTB")
    imgTruck = poco("imgTruck")
    #action game
    btnPass = poco("btnPass")
    btnKnock = poco("btnKnock")
    btnExchange1 = poco("btnExchange1")
    btnSwap = poco("btnSwap")
    btnExchange5 = poco("btnExchange5")
    #game
    bg_table = poco("bg_table")
    #vip
    btnVip = poco("btnVip")
    #DB
    iconSetting = poco("iconSetting")
    lobbyLayer2 = poco("bgLobbyLayer2")
    btnGuest = poco("btnGuest")
    btnTomorrow = poco("btnTomorrow")
    btnGooglePlus = poco("btnGooglePlus")
    btnFacebookNormal = poco("btnFacebookNormal")
    btnRegister = poco("btnRegister")
    btnDaily = poco("btnDaily")
    btnCallBack=poco("btnCallBack")
    btnSkip= poco("btnSkip")
    btnSelectTable=poco("btnSelectTable")
    pnGold = poco("pnGold")
    ibID= poco("lbID")
    btn_closeInfo= poco("btnHide")
def clear():
    fruits =[
    pocoTag.btnSwitch,
    pocoTag.inputUser,
    pocoTag.logo,
    pocoTag.inputPass,
    pocoTag.btnLogin,
    pocoTag.btnSetting,
    pocoTag.btnClose,
    pocoTag.btnPlay,
    pocoTag.btnLeaveGame,
    pocoTag.btnHide ,
    pocoTag.btnMain,
    pocoTag.notiShow,
    pocoTag.NOTIFICACIONES,
    pocoTag.lbTime,
    pocoTag.btnCheat,
    pocoTag.btnAddBot,
    pocoTag.lbTimeServer,
    pocoTag.btnSendCheatPlayer,
    pocoTag.btnSendCustom,
    pocoTag.btnTabCustom,
    pocoTag.btnResetCustom,
    pocoTag.pnPointEvent,
    pocoTag.pnCaseId_1,
    pocoTag.btnJoin,
    pocoTag.btnClaim,
    pocoTag.lbDayCurrent,
    pocoTag.lbDay1,
    pocoTag.lbDay2,
    pocoTag.lbDay3,
    pocoTag.lbDay4,
    pocoTag.lbDay5,
    pocoTag.lbDay6,
    pocoTag.lbDay7,
    pocoTag.lbNumTacos,
    pocoTag.lbProgress,
    pocoTag.lbGold,
    pocoTag.btnOfferEventTB,
    pocoTag.imgTruck,
    pocoTag.btnPass,
    pocoTag.btnKnock,
    pocoTag.btnExchange1,
    pocoTag.btnSwap,
    pocoTag.btnExchange5,
    pocoTag.bg_table,
    pocoTag.btnVip,
    pocoTag.iconSetting,
    pocoTag.lobbyLayer2,
    pocoTag.btnGuest,
    pocoTag.btnTomorrow,
    pocoTag.btnGooglePlus,
    pocoTag.btnFacebookNormal,
    pocoTag.btnRegister,
    pocoTag.btnDaily,
    pocoTag.btnCallBack,
    pocoTag.btnSkip,
    pocoTag.btnSelectTable,
    pocoTag.pnGold]
    for x in fruits:
        x.invalidate()
#------------------------------------------VIP-----------------------------------------------#
#------------------------------------------VIP-----------------------------------------------#
#------------------------------------------DB------------------------------------------------#

#------------------------------------------DB------------------------------------------------#
#---------------------------------------------End script--------------------------------------------------------------------#
#---------------------------------------------Report-----------------------------------------------------#
#File report
#---------------------------------------------End Report-------------------------------------------------#






