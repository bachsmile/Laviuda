
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
    afterEvent()
    day1()
    claimGift()
    day2()
    noClaimGift()
    CheckChangeAcc()
    missionPassDayInTable(2)
    autoClaimGift()
    day3()
    missionPassDayOpenGui()
    passClaimGift()
    day4()
#     UpdateProgressMissionFull()
#     checkDisconect()
#     day5()
#     GuiDeal()
#     day6()
#     day7()
    endEvent()
#------------------------------------------WC------------------------------------------------#

#------------------------------------------VIP-----------------------------------------------#
def Vip():
    clearReport()
    #Case 1: OPEN VIP
    open_vip()
    reportCheckOpenVip(data)
    #Case 2: OPEN VIP NHƯNG KHÔNG MUA
    open_pack("btnBuyBroze")
    open_pack("btnBuySilver")
    open_pack("btnBuyGold")
    reportCheckPackVip(data)
    #Case 3: MUA VIP 1
    checkLevelVip() #check level vip
    api_postDoFunction("19202812", "CHEAT_TIME_REMAIN_VIP", [0]) #cheat non-vip
    check_buy_vip("vip.pack_1") #mua vip 1
    back_to_lobby()
    check_item() #check item ngoai ban choi
    to_table()
    check_item() #check item trong ban choi
    reportBuyVip(data)
    #Case 4: MUA VIP 2
    check_buy_vip("vip.pack_2")
    check_item() #check item trong ban choi
    reportBuyVip(data)
    #Case 5: Mua vip 3
    check_buy_vip("vip.pack_3")
    buy_vip_thap("btnBuyBroze") #check mua vip 1
    reportBuyVip(data)
    #Case 6: Mua gold trong shop
    check_buy_gold("19202812", "ipa.pack_1")
    reportBuyGold(data)
    #Case 7: Check nhan gold support
    check_gold_support()
    back_to_lobby()
    reportReceivedGoldSupport(data)
    #Case 8: Cheat qua ngay nhan gold tribute
    timeWC= {
    "Y":2021,"M":1,"D":13,"h":7,"m":0,"s":0
    }
    api_changeTimeServer(convertDayTimeToMili(timeWC))
    reloadLobby()
    check_gold_tribute()
    reportReceivedGoldTribute(data)
    #Case 9: Check show data vip theo account
    changeAcc(userN,passW)
    #Case 10: Check gia han vip
    cheatTimeRemain(UserID,day)
    reloadLobby()
    checkMoGUIVipGD()
    killApp()
    openApp()
    checkMoGUIVipGD()
    reportExpiredVip(data)
    #Case11: Check het han trong ban choi
    api_postDoFunction("19202812", "CHEAT_TIME_REMAIN_VIP", [60])
    to_table()
    check_item()
    reportCheckExpiredTable(data)
    #Case12: Check het han mua vip
    checkMoGUIVipGD()
    cheat_buy_vip("vip.pack_1")
    reportBuyVip(data)
#------------------------------------------VIP-----------------------------------------------#
#------------------------------------------DB------------------------------------------------#
def DB():
    #1. check có đang ở màn hình login ko
    check_login()
    #2. đăng kí thường
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
#-----#
#---------------------------------------------End script-------------------------------------------------#
#---------------------------------------------Report-----------------------------------------------------#
#File report
#---------------------------------------------End Report-------------------------------------------------#







