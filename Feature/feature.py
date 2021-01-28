
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
# def WC():
#     beforEvent("user0")
#     afterEvent("user1")
#     day1("user1")
#     claimGift("day1","user1")
#     day2("user1")
#     noClaimGift("day2","user1")
#     CheckChangeAcc(1,"user2") #1 -> day 1
#     missionPassDayInTable(2,"user2")
#     autoClaimGift("day2")
#     day3("user2")
#     missionPassDayOpenGui(3,"user2")
#     passClaimGift(2,"user1")
#     day4("user1")
#     UpdateProgressMissionFull("day4","user1")
# #     checkDisconect()
# #     day5()
#     GuiDeal("user1")
# #     day6()
#     day7("user1","user3")
#     endEvent("day7","user2")
def WC():
    beforEvent(configCase["beforEvent"]["account"])
    afterEvent(configCase["afterEvent"]["account"])
    day1(configCase["day1"]["account"])
    claimGift("day"+str(configCase["claimGift"]["day"]),configCase["claimGift"]["account"])
    day2(configCase["day2"]["account"])
    noClaimGift("day"+str(configCase["noClaimGift"]["day"]),configCase["noClaimGift"]["account"])
    CheckChangeAcc(configCase["CheckChangeAcc"]["day"]-1,configCase["CheckChangeAcc"]["account"]) #1 -> day 1
    missionPassDayInTable(configCase["missionPassDayInTable"]["day"],configCase["missionPassDayInTable"]["account"])
    autoClaimGift("day"+str(configCase["autoClaimGift"]["day"]))
    day3(configCase["day3"]["account"])
    missionPassDayOpenGui(configCase["missionPassDayOpenGui"]["day"],configCase["missionPassDayOpenGui"]["account"])
    passClaimGift(configCase["passClaimGift"]["day"],configCase["passClaimGift"]["account"])
    day4(configCase["day4"]["account"])
    UpdateProgressMissionFull("day"+str(configCase["UpdateProgressMissionFull"]["day"]),configCase["UpdateProgressMissionFull"]["account"])
#     checkDisconect()
#     day5()
    GuiDeal(configCase["GuiDeal"]["account"])
#     day6()
    day7(configCase["day7"]["account"],configCase["day7"]["account2"])
    endEvent("day"+str(configCase["endEvent"]["day"]-1),configCase["endEvent"]["account"])
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
    cheatTimeRemain(19202812, 0) #cheat non-vip
    reloadLobby()
    back_to_lobby()
    check_buy_vip(19202812, "vip.pack_1") #mua vip 1
    to_table()
    check_item() #check item trong ban choi
    back_to_lobby()
    reportBuyVip1(data)
    #Case 4: MUA VIP 2
    check_buy_vip(19202812, "vip.pack_2")
    to_table()
    check_item() #check item trong ban choi
    back_to_lobby()
    reportBuyVip2(data)
    #Case 5: Mua vip 3
    check_buy_vip(19202812, "vip.pack_3")
    buy_vip_thap("btnBuySilver") #check mua vip 1
    back_to_lobby()
    reportBuyVip3(data)
    #Case 6: Mua gold trong shop
    check_buy_gold(19202812, "iap.pack_1")
    reportBuyGold(data)
    #Case 7: Check nhan gold support
    check_gold_support(19202812)
    reloadLobby()
    reportReceivedGoldSupport(data)
    #Case 7.1: Check nhan gold support lần 2
    check_gold_support(19202812)
    reloadLobby()
    reportReceivedGoldSupport(data)
    cheatGold(19202812, 50000)
    #Case 8: Cheat qua ngay nhan gold tribute
    timeWC= {
    "Y":2020,"M":11,"D":24,"h":12,"m":0,"s":0
    }
    api_changeTimeServer(convertDayTimeToMili(timeWC))
    reloadLobby()
    check_gold_tribute(19202812)
    back_to_lobby()
    reportReceivedGoldTribute(data)
    #Case 9: Check show data vip theo account
    #   changeAcc(account["user1"]["user"],account["user1"]["pass"])
    #   changeAcc(account["user0"]["user"],account["user0"]["pass"])
    #Case 10: Check show pop-up gia han vip
    cheatTimeRemain(19202812, 1)
    checkMoGUIGH()
    back_to_lobby()
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
#---------------------------------------------End Report-------------------------------------------------#


