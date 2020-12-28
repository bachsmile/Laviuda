# -*- encoding=utf8 -*-
__author__ = "pc"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.drivers.cocosjs import CocosJsPoco
from test.Autotest.chat.Feature.Daily_Bonus.Py.a import *
from test.Autotest.chat.Feature.Daily_Bonus.Py.Repoert_log import *
from test.Autotest.chat.Feature.Daily_Bonus.Py.Api import *
from test.Autotest.chat.ConFig.Py.daily_bonus import*
if not cli_setup():
    auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = CocosJsPoco()
# script content
print("start...")
# 1. check có đang ở log_in screen hay ko
data= {
    "status": "False"
}
if poco("btnSwitch").exists():
    data["status"]="true"
    print("success!")
else:
    print ("Please go to Login page")
reportdailybonus(data)
# 2.1 Register lan dau băng google-> play tutorial
# poco("btnGooglePlus").click()
# touch(Template(r"tpl1607677907767.png", record_pos=(-0.17, -0.02), resolution=(1280, 720)))
#    #play tutorial----------------------------------------
# try:
#     poco("btnClaim").exists()
# except:
#     print("Không tự động show Gui daily bonus sau play tutorial")
# else:
#     print("Success!")
# poco("btnClaim").click()
# try:
#     poco("btnPlay").exists()
# except:
#     print("Không auto về lại lobby sau khi nhận bonus")
# else:
#     print("Success!")

#2.2 Register_thường
data= {
    "status": "false"
}
poco("btnSwitch").click()
poco("Image_4").click()
text("ngocnt72")
poco("Image_4_0").click()
text("12345678")
poco("btnRegister").click()          
# poco("<no-name>").offspring("layer_5")[1].child("<no-name>")[1].child("<no-name>").child("<no-name>")[6].click()
# poco(type="LabelBMFont")
# poco(type="Label").click()
   #Play tutorial---------------------------------------
time.sleep(3)
if poco("btnClaim").exists():
    data["status"]="true"
    poco("btnClaim").click()
    poco("btnClaim").click()
    print("Success!")
else:
    print("Không tự động show Gui daily bonus sau play tutorial")
reportdailybonus(data)
gold_befor1= 0
data={
"status":"Fail"
}
gold_after1= gold_number()
if 40000==(gold_after1 - gold_befor1):
    data["status"]="True"
else:
    data["status"]="Fail"
reportdailybonus(data)
try:
    poco("btnPlay").exists()
except:
    print("Không auto về lại lobby sau khi nhận bonus")
else:
    print("Success!")
# 3. Log out-> Log in sau 24h
log_out()
time.sleep(3)
api_changeTimeServer(1608624000000)
log_in_FB()
time.sleep(3)
#4. khong nhan bonus, kill app vao lai
# kill_app()
# start_app()
#5. Nhận bonus lần 2
data={
"status":"Fail"
}
time.sleep(3)
if poco("btnClaim").exists():
    data["status"]="True"
    gold_befor2= gold_number()
    poco("btnClaim").click()
    gold_after2= gold_number()
    if DailyBonus["day2"]["bonus"]==(gold_after2 - gold_befor2):    
        data["status"]="True"
    else:
        data["status"]="False"
    reportdailybonus(data)
else:
    print("Dont show GUI bonus")
    data["status"]="False"
reportdailybonus(data)
#6. Check co dang o lobby khong
try:
    poco("btnPlay").exists()
except:
    print("Không auto về lại lobby sau khi nhận bonus")
else:
    print("Success!")
#7.dung o lobby cho nhan bonus
api_changeTimeServer(1608796800000)
try:
    poco("btnClaim").exists()
except:
    print("Không auto show GUI daily bonus ở lobby sau 24h")
else:
    print("Success!")
#8. Nhận bonus lan 3
data={
"status":"Fail"
}
time.sleep(3)
if poco("btnClaim").exists():
    gold_befor3= gold_number()
    poco("btnClaim").click()
    gold_after3= gold_number()
    if DailyBonus["day3"]["bonus"]==(gold_after3 - gold_befor3):    
        data["status"]="True"
    else:
        data["status"]="False"
    reportdailybonus(data)
else:
    print("Khong show GUI dailly bonus ngày 3")
    data["status"]="False"
reportdailybonus(data)
#9. Vao lại Gui daily bonus
time.sleep(3)
poco("btnDaily").click()
poco("btnTomorrow").exists()
poco("textTomorrow").click()
poco("btnPlay").exists()
#10. Log out-> vào lại sau 23h
log_out()
api_changeTimeServer(1608879600000)
log_in_FB()
data={
    "status":"false"
}
time.sleep(5)
if poco("btnClaim").exists():
    poco("btnClaim").click()
    time.sleep(3)
    data["status"]="False"
    print("Show daily GUI daily bonus khi chưa đủ 24h")
else:
    data["status"]="True"
    print("Success!")
reportdailybonus(data)
time.sleep(3)
#11. Vao playinggame-> ra lại lobby
poco("btnPlay").click()
api_changeTimeServer(1608882000000)
poco("btnLeaveGame").click()
try:
    poco("btnPlay").exists() #leave khi chưa đủ 24h
    data["status"]="True"
except:
    print("playing->lobby: show GUI daily bonus khi chưa đủ 24h")
    time.sleep(3)
    poco("btnClaim").click()
    data["status"]="False"
else:
    print("Success!")
reportdailybonus(data)
#12. Vào playing game-> Chờ qua 24h rồi ra lại lobby( Ngày 4)
data= {
    "status":"False"
}
poco("btnPlay").click()
api_changeTimeServer(1608883200000)
poco("btnLeaveGame").click()
time.sleep(3)
if poco("btnClaim").exists():
    poco("btnClaim").click()
    print("Success!")
    data["status"]="True"
else:
    print("Không auto show GUI daily bonus khi play game về lobby sau 24h")
    data["status"]="False"
reportdailybonus(data)   
#13. Click nhận bonus của ngày 4
data={
"status":"Fail"
}
time.sleep(3)
if poco("btnClaim").exists():
    gold_befor4= gold_number()
    poco("btnClaim").click()
    gold_after4= gold_number()
    if DailyBonus["day4"]["bonus"]==(gold_after4 - gold_befor4):    
        data["status"]="True"
    else:
        data["status"]="False"
else:
    print("Dont show daily bonus on day 4")
    data["status"]="False"
reportdailybonus(data)
#14. Đứng chờ ở GUI daily bonus 23h
api_changeTimeServer(1608966000000)
poco("btnDaily").click()
poco("btnTomorrow").exists()
#15. Tiếp tục đứng ở GUI daily bonus chờ thêm 1h( ngày 5)
api_changeTimeServer(1608969600000)
#16 Nhận bonus 5 lần-> Log out-> Login sau 24h nhưng không nhận bonus->Login lại sau 24h tiếp theo
data={
"status":"Fail"
}
time.sleep(3)
if poco("btnClaim").exists():
    print("Show daily bonus day 5 Success!")
    gold_befor5= gold_number()
    poco("btnClaim").click()
    gold_after5= gold_number()
    if DailyBonus["day5"]["bonus"]==(gold_after5 - gold_befor5):    
        data["status"]="True"
    else:
        print("Không auto show daily bonus khi đứng chờ sẳn ở GUI daily bonus sau 24h")
        data["status"]="False"
reportdailybonus(data)
log_out()
api_changeTimeServer(1609056000000)
log_in_FB()
     #kill app vào lại sau 24h
# kill_app()
# start_app()
try:
    poco("btnClaim").exists()
except:
    print("Không auto show daily bonus khi không nhận bonus của ngày trc")
else:
    print("Success!")
api_changeTimeServer(1609142400000)
log_in_gg()
#17 Click nhận bonus của ngày 6
data={
"status":"Fail"
}
time.sleep(3)
if poco("btnClaim").exists():
    print("Show bonus ngay 6 sau 48h success!")
    gold_befor6= gold_number()
    poco("btnClaim").click()
    gold_after6= gold_number()
    if DailyBonus["day6"]["bonus"]==(gold_after6 - gold_befor6):    
        data["status"]="True"
    else:
        print("Update không đúng số gold")
        data["status"]="False"
else:
    print("Không show GUI daily bonus nếu trc đó đã show nhưng không nhận,kill app vào lại")
    data["status"]="False"
reportdailybonus(data)
#18 Nhận bonus lần thứ 7
api_changeTimeServer(1609228800000)
data={
"status":"Fail"
}
time.sleep(3)
if poco("btnClaim").exists():
    print("Show bonus day 7 success!")
    data["status"]="True"
    gold_befor7= gold_number()
    poco("btnClaim").click()
    gold_after7= gold_number()
    if DailyBonus["day7"]["bonus"]==(gold_after7 - gold_befor7):    
        data["status"]="True"
    else:
        data["status"]="False"
else:
    print("Show show daily bonus day 7 sau 24h")
    data["status"]="False"
reportdailybonus(data)
#check an btn Daily bonus ở lobby khi đã nhận đủ 7 lần
if poco("btnLuckyChest").exists():
    print("Van show icon Daily bonus ở lobby khi đã nhận đủ 7 lần")
else:
    print("Ẩn icon daily bonus khi đã nhận đủ thành công")
#19. Ra lại lobby-> đứng ở lobby chờ sau 24
poco("btnPlay").exists()
api_changeTimeServer(1609315200000)
if poco("btnClaim").exists():
    print("Vẩn show daily bonus khi đã nhận đủ 7 lần")
else:
    print("Success!")
#20. Log out-> Login lại sau 24h
log_out()
api_changeTimeServer(1609401600000)
log_in_gg()
if poco("btnClaim").exists():
    print("Vẩn show daily bonus khi đã nhận đủ 7 lần")
else:
    print(" Success!")

    
reportdailybonus()
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)


