
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
    #Check truoc su kien vai ngay 
    beforEvent(configCase["beforEvent"]["account"])
    #check truoc su kien trong thoi gian quang cao su kien
    afterEvent(configCase["afterEvent"]["account"])
    #thuc hien kiem tra nhiem vu ngay1
    day1(configCase["day1"]["account"])
    #check nhan qua hoan thanh nhiem vu
    claimGift("day"+str(configCase["claimGift"]["day"]),configCase["claimGift"]["account"])
    #thuc hien kiem tra nhiem vu ngay2
    day2(configCase["day2"]["account"])
    #check bam khong nhan qua
    noClaimGift("day"+str(configCase["noClaimGift"]["day"]),configCase["noClaimGift"]["account"])
    #check cap nhan nhiem vu khi thay doi tai khoang
    CheckChangeAcc(configCase["CheckChangeAcc"]["day"]-1,configCase["CheckChangeAcc"]["account"]) #1 -> day 1    
    #check cap nhat nhiem vu khi dang o trong ban choi qua ngay moi
    missionPassDayInTable(configCase["missionPassDayInTable"]["day"],configCase["missionPassDayInTable"]["account"])
    #qua ngay moi co qua hoan thanh nhiem vu chua nhan check auto nhan
    autoClaimGift("day"+str(configCase["autoClaimGift"]["day"]))
    #thuc hien kiem tra nhiem vu ngay3
    day3(configCase["day3"]["account"])
    #check update nhiem vu qua ngay moi khi dang mo GUI event
    missionPassDayOpenGui(configCase["missionPassDayOpenGui"]["day"],configCase["missionPassDayOpenGui"]["account"])
    #check nhan qua hoan thanh sau khi off
    passClaimGift(configCase["passClaimGift"]["day"],configCase["passClaimGift"]["account"])
    #thuc hien kiem tra nhiem vu ngay4
    day4(configCase["day4"]["account"]) 
    #check update tien trinh nhiem vu
    UpdateProgressMissionFull("day"+str(configCase["UpdateProgressMissionFull"]["day"]),configCase["UpdateProgressMissionFull"]["account"])
#     checkDisconect()
#     day5()
    #check hoat dong GUI deal
    GuiDeal(configCase["GuiDeal"]["account"]) #{*}
#     day6()
    #thuc hien kiem tra nhiem vu ngay7
    day7(configCase["day7"]["account"],configCase["day7"]["account2"])
    #check dong cac su kien sau khi ket thuc
    endEvent("day"+str(configCase["endEvent"]["day"]-1),configCase["endEvent"]["account"])
#------------------------------------------WC------------------------------------------------#
# WC()
#------------------------------------------VIP-----------------------------------------------#
def Vip():
    clearReport()
#     #Case 1: OPEN VIP
#     changeAcc("vyhn0908","123456")
    open_vip()
    reportCheckOpenVip(data)
    #Case 2: OPEN VIP NHƯNG KHÔNG MUA
    open_pack("btnBuyBroze")
    open_pack("btnBuySilver")
    open_pack("btnBuyGold")
    back_to_lobby()
    reportCheckPackVip(data)
    #Case 3: MUA VIP 1
    cheatTimeRemain(20040460, 0) #cheat non-vip
    reloadLobby()
    back_to_lobby()
    check_buy_vip(20040460, "vip.pack_1") #mua vip 1
    to_table()
    check_item() #check item trong ban choi
    back_to_lobby()
    reportBuyVip1(data)
    #Case 4: MUA VIP 2
    check_buy_vip(20040460, "vip.pack_2")
    to_table()
    check_item() #check item trong ban choi
    back_to_lobby()
    reportBuyVip2(data)
    #Case 5: Mua vip 3
    check_buy_vip(20040460, "vip.pack_3")
    buy_vip_thap("btnBuySilver") #check mua vip 1
    back_to_lobby()
    reportBuyVip3(data)
    #Case 6: Mua gold trong shop
    check_buy_gold(20040460, "iap.pack_1")
    reportBuyGold(data)
    #Case 7: Check nhan gold support
    check_gold_support(20040460)
    reloadLobby()
    reportReceivedGoldSupport(data)
    #Case 7.1: Check nhan gold support lần 2
    check_gold_support(20040460)
    reloadLobby()
    reportReceivedGoldSupport(data)
    cheatGold(20040460, 50000)
    #Case 8: Cheat qua ngay nhan gold tribute
    timeWC= {
    "Y":2020,"M":11,"D":9,"h":12,"m":0,"s":0
    }
    api_changeTimeServer(convertDayTimeToMili(timeWC))
    reloadLobby()
    check_gold_tribute(20040460)
    back_to_lobby()
    reportReceivedGoldTribute(data)
    #Case 9: Check show data vip theo account
    #   changeAcc(account["user1"]["user"],account["user1"]["pass"])
    #   changeAcc(account["user0"]["user"],account["user0"]["pass"])
    #Case 10: Check show pop-up gia han vip
    cheatTimeRemain(20040460, 1)
    checkMoGUIGH()
    back_to_lobby()
    reportExpiredVip(data)
    #Case11: Check het han trong ban choi
    api_postDoFunction(20040460, "CHEAT_TIME_REMAIN_VIP", [10])
    to_table()
    time.sleep(3)
    check_item()
    back_lobby_from_table()
    reportCheckExpiredTable(data)
    #Case12: Check het han mua vip
    checkMoGUIVip()
    check_buy_vip(20040460, "vip.pack_1")
    reportBuyVip1KHH(data)
Vip()
#------------------------------------------VIP-----------------------------------------------#
#------------------------------------------DB------------------------------------------------#
def DB():
    s=0
    #1. check có đang ở màn hình login ko
    api_changeTimeServer(convertDayTime(time_db[0]))
    check_login()
    #2. đăng kí thường
    register()     
    play_tutorial()
    s=bonus_day_1(0)
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
    s=claim_bonus_true(DailyBonus["day2"],s,userID)
    #6. Check có đang ở lobby hay không
    check_lobby()
    clear()
    #7.Kiểm tra có show GUI daily bonus khi dung o lobby cho nhan bonus,nhân bonus(day3)
    api_changeTimeServer(convertDayTime(time_db[2]))
    time.sleep(1)
    reloadLobby()
    time.sleep(10)
    s=claim_bonus_true(DailyBonus["day3"],s,userID)
    clear()
    #10. Log out-> vào lại sau 23
    log_out()
    api_changeTimeServer(convertDayTime(time_db[3]))
    log_in()
    s=claim_bonus_false(DailyBonus["day4"],s,userID)
    clear()
    #11. Vao playinggame-> ra lại lobby
    #12. Vào playing game-> Chờ qua 24h rồi ra lại lobby( Ngày 4)
    playing_24h()
    #13. Click nhận bonus của ngày 4
    time.sleep(3)
    s=claim_bonus_true(DailyBonus["day4"],s,userID)
    clear()
    #14. Đứng chờ ở GUI daily bonus 23h
    GUI_bonus_23h(s)
    close_Gui_daily()
    #15. Tiếp tục đứng ở GUI daily bonus chờ thêm 1h( ngày 5)
    GUI_bonus_24h()
    s=claim_bonus_true(DailyBonus["day5"],s,userID)
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
    s=claim_bonus_true(DailyBonus["day6"],s,userID)
    clear()
    # #18 Nhận bonus lần thứ 7
    api_changeTimeServer(convertDayTime(time_db[8]))
    reloadLobby()
    claim_bonus_true(DailyBonus["day7"],s,userID)
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







