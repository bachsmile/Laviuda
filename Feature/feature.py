
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
    beforEvent("user0")
    afterEvent("user1")
    day1("user1")
    claimGift("day1","user1")
    day2("user1")
    noClaimGift("day2","user1")
    CheckChangeAcc(1,"user2") #1 -> day 1
    missionPassDayInTable(2,"user2")
    autoClaimGift("day2")
    day3("user2")
    missionPassDayOpenGui(3,user2)
    passClaimGift(2,"user1")
    day4("user1")
    UpdateProgressMissionFull("day4","user1")
#     checkDisconect()
#     day5()
    GuiDeal("user2")
#     day6()
    day7("user1","user3")
    endEvent("day7","user2")
#------------------------------------------WC------------------------------------------------#
# WC()
#------------------------------------------VIP-----------------------------------------------#
def Vip():
    clearReportVip()
    #Case 1: OPEN VIP
    open_vip()
    reportCheckOpenVip(data)
    #Case 2: OPEN VIP NHƯNG KHÔNG MUA
    open_pack("btnBuyBroze")
    open_pack("btnBuySilver")
    open_pack("btnBuyGold")
    back_to_lobby()
    reportCheckPackVip(data)
    #Case 3: MUA VIP 1
    checkLevelVip() #check level vip
    cheatTimeRemain(19202812, 0) #cheat non-vip
    reloadLobby()
    time.sleep(1)
    back_to_lobby()
    check_buy_vip(19202812, "vip.pack_1") #mua vip 1
#   back_to_lobby()
#   check_item() #check item ngoai ban choi
    to_table()
    check_item() #check item trong ban choi
    back_to_lobby()
    reportBuyVip(data)
    #Case 4: MUA VIP 2
    check_buy_vip(19202812, "vip.pack_2")
    to_table()
    check_item() #check item trong ban choi
    back_to_lobby()
    reportBuyVip(data)
    #Case 5: Mua vip 3
    check_buy_vip(19202812, "vip.pack_3")
    buy_vip_thap("btnBuyBroze") #check mua vip 1
    reportBuyVip(data)
    #Case 6: Mua gold trong shop
    check_buy_gold(19202812, "iap.pack_1")
    reportBuyGold(data)
    #Case 7: Check nhan gold support
    check_gold_support(19202812)
    reportReceivedGoldSupport(data)
    #Case 7.1: Check nhan gold support lần 2
    check_gold_support(19202812)
    reportReceivedGoldSupport(data)
    #Case 8: Cheat qua ngay nhan gold tribute
    timeWC= {
    "Y":2021,"M":1,"D":2,"h":12,"m":0,"s":0
    }
    api_changeTimeServer(convertDayTimeToMili(timeWC))
    reloadLobby()
    check_gold_tribute(19202812)
    reportReceivedGoldTribute(data)
    #Case 9: Check show data vip theo account
    changeAcc(account["user1"]["user"],account["user1"]["pass"])
    changeAcc(account["user0"]["user"],account["user0"]["pass"])
    #Case 10: Check show pop-up gia han vip
    cheatTimeRemain(19202812, 1)
    reloadLobby()
    checkMoGUIGH()
    reportExpiredVip(data)
    #Case11: Check het han trong ban choi
    api_postDoFunction("19202812", "CHEAT_TIME_REMAIN_VIP", [10])
    to_table()
    time.sleep(3)
    check_item()
    back_lobby_from_table()
    reportCheckExpiredTable(data)
    #Case12: Check het han mua vip
    checkMoGUIVip()
    check_buy_vip(19202812, "vip.pack_1")
    reportBuyVip(data)
# Vip()
#------------------------------------------VIP-----------------------------------------------#
#------------------------------------------DB------------------------------------------------#
def DB():
    #1. check có đang ở màn hình login ko
    api_changeTimeServer(convertDayTime(time_db[0]))
    check_login()
    #2. đăng kí thường
    register()     
    play_tutorial()
    s=bonus_day_1(s)
    check_lobby()
    clear()
    userID= get_user_id()
    time.sleep(3)
    close_info()
    # 3.Log out-> Log in sau 24h
    log_out()
    time.sleep(3)
    api_changeTimeServer(convertDayTime(time_db[1]))
    time.sleep(3)
    log_in()
    time.sleep(3)
    #5. Nhận bonus lần 2
    s=claim_bonus_true(DailyBonus["day2"],s)
    #6. Check có đang ở lobby hay không
    check_lobby()
    clear()
    #7.Kiểm tra có show GUI daily bonus khi dung o lobby cho nhan bonus,nhân bonus(day3)
    api_changeTimeServer(convertDayTime(time_db[2]))
    time.sleep(1)
    reloadLobby()
    time.sleep(10)
    s=claim_bonus_true(DailyBonus["day3"],s)
    clear()
    #10. Log out-> vào lại sau 23
    log_out()
    api_changeTimeServer(convertDayTime(time_db[3]))
    log_in()
    s=claim_bonus_false(DailyBonus["day4"],s)
    clear()
    #11. Vao playinggame-> ra lại lobby
    #12. Vào playing game-> Chờ qua 24h rồi ra lại lobby( Ngày 4)
    playing_24h()
    #13. Click nhận bonus của ngày 4
    time.sleep(3)
    s=claim_bonus_true(DailyBonus["day4"],s)
    clear()
    #14. Đứng chờ ở GUI daily bonus 23h
    GUI_bonus_23h(s)
    close_Gui_daily()
    #15. Tiếp tục đứng ở GUI daily bonus chờ thêm 1h( ngày 5)
    GUI_bonus_24h()
    s=claim_bonus_true(DailyBonus["day5"],s)
    clear()
    close_Gui_daily()
    #16 Nhận bonus 5 lần-> Log out-> Login sau 24h nhưng không nhận bonus->Login lại sau 24h tiếp theo
    time.sleep(2)
    log_out()
    api_changeTimeServer(convertDayTime(time_db[7]))
    time.sleep(3)
    log_in()
    #kill app
    #start app
    #17 Click nhận bonus của ngày 6
    s=claim_bonus_true(DailyBonus["day6"],s)
    clear()
    # #18 Nhận bonus lần thứ 7
    api_changeTimeServer(convertDayTime(time_db[8]))
    reloadLobby()
    claim_bonus_true(DailyBonus["day7"],s)
    clear()
    #check an btn Daily bonus ở lobby khi đã nhận đủ 7 lần
    checkCompleteBonus(s)
    time.sleep(3)
    checkIconDaily()
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
#---------------------------------------------End Report-------------------------------------------------#





