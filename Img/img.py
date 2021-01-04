
#---------------------------------------------Tile-------------------------------------------------------#
__author__ = "QC"
__title__ ="List Img"
__desc__="""
    Tong hop danh sach cac img in game
"""
#---------------------------------------------End Tile---------------------------------------------------#
#---------------------------------------------Import LIB-------------------------------------------------#
from airtest.core.api import *
from airtest.cli.parser import cli_setup
#---------------------------------------------End Import Lib---------------------------------------------#
#---------------------------------------------Link-------------------------------------------------------#
# from Lavuavi.Img.img import *
#---------------------------------------------Link-------------------------------------------------------#
#---------------------------------------------Import FILE------------------------------------------------#

#---------------------------------------------End Import FILE--------------------------------------------#

#---------------------------------------------Connect Device---------------------------------------------#
if not cli_setup():
    auto_setup(__file__)
#------------------------------------------End Connect---------------------------------------------------#

#------------------------------------------Poco----------------------------------------------------------#
#------------------------------------------End Poco------------------------------------------------------#
#------------------------------------------script content------------------------------------------------#
#------------------------------------------Main----------------------------------------------#
#------------------------------------------Main------------------------------------------#
#------------------------------------------WC------------------------------------------------#

#------------------------------------------WC------------------------------------------------#
#------------------------------------------VIP-----------------------------------------------#
class imageInOutAcc:
    imgBtnOut=Template(r"tpl1607683227106.png", record_pos=(-0.098, 0.08), resolution=(2400, 1080))
    imgOutOk=Template(r"tpl1607683352695.png", record_pos=(0.08, 0.068), resolution=(2400, 1080))
class imageWC:
    imgBtnEvent=Template(r"tpl1607566321368.png", record_pos=(-0.284, -0.009), resolution=(652, 1212))
    imgWin=Template(r"tpl1608545722831.png", record_pos=(0.35, -0.125), resolution=(2400, 1080))
    imgProgessBarON=Template(r"tpl1607566598040.png", record_pos=(0.326, 0.22), resolution=(731, 1212))
    imgDeal=Template(r"tpl1608534993305.png", record_pos=(-0.003, 0.007), resolution=(2400, 1080))
    imgGoldCheat=Template(r"tpl1608185711465.png", record_pos=(-0.104, -0.161), resolution=(2340, 1079))
    imgGoldCheat1=Template(r"tpl1608102303058.png", record_pos=(0.184, 0.083), resolution=(2400, 1080))
class image_vip:
    list_item = Template(r"tpl1608003653170.png", record_pos=(-0.103, 0.124), resolution=(2340, 1079))
    btn_profile = Template(r"tpl1608619319065.png", record_pos=(-0.218, 0.149), resolution=(2340, 1079))

    cachua = Template(r"tpl1608013600710.png", record_pos=(-0.175, 0.123), resolution=(2340, 1079))
    votay = Template(r"tpl1608013625566.png", record_pos=(-0.104, 0.122), resolution=(2340, 1079))
    xonuoc = Template(r"tpl1608013651272.png", record_pos=(-0.029, 0.122), resolution=(2340, 1079))
    trung = Template(r"tpl1608013670433.png", record_pos=(0.042, 0.122), resolution=(2340, 1079))
    hoahong = Template(r"tpl1608013711710.png", record_pos=(-0.04, 0.123), resolution=(2340, 1079))
    hoavang = Template(r"tpl1608013735462.png", record_pos=(0.033, 0.123), resolution=(2340, 1079))
    sungnuoc = Template(r"tpl1608013753862.png", record_pos=(0.106, 0.122), resolution=(2340, 1079))
    boom = Template(r"tpl1608087183486.png", record_pos=(-0.048, 0.122), resolution=(2340, 1079))
    bongnuoc = Template(r"tpl1608087273775.png", record_pos=(0.026, 0.122), resolution=(2340, 1079))
    lyruou = Template(r"tpl1608087305552.png", record_pos=(0.097, 0.122), resolution=(2340, 1079))
    cup = Template(r"tpl1608087329463.png", record_pos=(0.171, 0.123), resolution=(2340, 1079))
    tym = Template(r"tpl1608087357654.png", record_pos=(-0.011, 0.122), resolution=(2340, 1079))
    hon = Template(r"tpl1608087404315.png", record_pos=(0.117, 0.122), resolution=(2340, 1079))
    tien = Template(r"tpl1608087427485.png", record_pos=(0.188, 0.123), resolution=(2340, 1079))
    traibong = Template(r"tpl1608087455447.png", record_pos=(0.206, 0.123), resolution=(2340, 1079))
    btn_play_now = Template(r"tpl1608006794393.png", record_pos=(0.399, -0.037), resolution=(2340, 1079))
    btn_vip = Template(r"tpl1607915160724.png", record_pos=(0.235, 0.045), resolution=(2340, 1079))
    btn_cancel = Template(r"tpl1607501575359.png", record_pos=(-0.066, 0.081), resolution=(2340, 1079))
    btn_ok = Template(r"tpl1607501814421.png", record_pos=(0.098, 0.081), resolution=(2340, 1079))
    btn_yes = Template(r"tpl1608711034073.png", record_pos=(0.099, 0.069), resolution=(2340, 1079))
    btn_no = Template(r"tpl1608711053674.png", record_pos=(-0.066, 0.069), resolution=(2340, 1079))


    image_vip_silver = Template(r"tpl1607916065983.png", record_pos=(0.021, -0.028), resolution=(2340, 1079))
    image_vip_gold = Template(r"tpl1607916089476.png", record_pos=(0.163, -0.03), resolution=(2340, 1079))
    image_vip_dynamion = Template(r"tpl1607916128309.png", record_pos=(0.307, -0.029), resolution=(2340, 1079))
    btn_claim = Template(r"tpl1607998065419.png", record_pos=(0.179, 0.19), resolution=(2340, 1079))

    btn_giahan = Template(r"tpl1608196142533.png", record_pos=(0.016, 0.185), resolution=(2340, 1079))
    pop_up_giahan = Template(r"tpl1608199295143.png", record_pos=(0.011, -0.006), resolution=(2340, 1079))
    icon_app = Template(r"tpl1608201973810.png", record_pos=(0.354, -0.842), resolution=(1079, 2340))
    icon_close = Template(r"tpl1608260634718.png", record_pos=(0.214, -0.107), resolution=(2340, 1079))

    back = Template(r"tpl1608001910288.png", record_pos=(0.468, -0.201), resolution=(2340, 1079))
    close = Template(r"tpl1608004769423.png", record_pos=(0.262, -0.16), resolution=(2340, 1079))
    outroom = Template(r"tpl1608105320117.png", record_pos=(0.45, -0.195), resolution=(2340, 1079))
#------------------------------------------END VIP-----------------------------------------------#
#------------------------------------------DB------------------------------------------------#
 class Daily_bonus:
        
#------------------------------------------DB------------------------------------------------#
#---------------------------------------------End script--------------------------------------------------#

