
#---------------------------------------------Tile-------------------------------------------------------#
__author__ = "QC"
__title__ ="Danh sach các feature"
__desc__="""
    Tong hop danh sach cac feature in game
"""
#---------------------------------------------End Tile---------------------------------------------------#
#---------------------------------------------Import LIB-------------------------------------------------#
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.cocosjs import CocosJsPoco
#---------------------------------------------End Import Lib---------------------------------------------#
#---------------------------------------------Link-------------------------------------------------------#
#---------------------------------------------Link-------------------------------------------------------#
# from Laviuda.Feature.feature import *
#---------------------------------------------Import FILE------------------------------------------------#
from Laviuda.Feature.Function.function import *
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
# WC--------------------------->
def WC():
    beforEvent()
#     afterEvent()
# WC()
#------------------------------------------WC------------------------------------------------#

#------------------------------------------VIP-----------------------------------------------#
    
#------------------------------------------VIP-----------------------------------------------#
#------------------------------------------DB------------------------------------------------#
def DB():
    check_login()
    register()     
       #Play tutorial---------------------------------------
    time.sleep(3)
    bonus_day_1()
    check_lobby()
    # 3. Log out-> Log in sau 24h
    log_out()
    time.sleep(3)
    api_changeTimeServer(1608624000000)
    time.sleep(3)
    log_in_FB()
    time.sleep(3)
    #5. Nhận bonus lần 2
    claim_bonus()
    #6. Check có đang ở lobby hay không
    check_lobby()
    #7.Kiểm tra có show GUI daily bonus khi dung o lobby cho nhan bonus,nhân bonus 
    claim_bonus()
    #9. Vao lại Gui daily bonus
    into_gui_bonus()
    #10. Log out-> vào lại sau 23h
    Logout_login_23h()
    #11. Vao playinggame-> ra lại lobby
    playing_23h()
    #12. Vào playing game-> Chờ qua 24h rồi ra lại lobby( Ngày 4)
    playing_24h()
    #13. Click nhận bonus của ngày 4
    claim_bonus()
    #14. Đứng chờ ở GUI daily bonus 23h
    GUI_bonus_23h()
    #15. Tiếp tục đứng ở GUI daily bonus chờ thêm 1h( ngày 5)
    api_changeTimeServer(1608969600000)
    #16 Nhận bonus 5 lần-> Log out-> Login sau 24h nhưng không nhận bonus->Login lại sau 24h tiếp theo
    claim_kill_login_24h()
    #17 Click nhận bonus của ngày 6
    claim_bonus()
    #18 Nhận bonus lần thứ 7
    api_changeTimeServer(1609228800000)
    claim_bonus()
    #check an btn Daily bonus ở lobby khi đã nhận đủ 7 lần
    complete_icon_bonus_lobby()
    #19. Ra lại lobby-> đứng ở lobby chờ sau 24
    complete_lobby_24h()
    #20. Log out-> Login lại sau 24h
    complete_logout_login_24h()
#------------------------------------------DB-------------------------------------------
DB()
#-----#
#---------------------------------------------End script-------------------------------------------------#
#---------------------------------------------Report-----------------------------------------------------#
#File report
#---------------------------------------------End Report-------------------------------------------------#
