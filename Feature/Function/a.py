# -*- encoding=utf8 -*-
__author__ = "pc"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=None, devices=[
            "android://127.0.0.1:5037/R58MB47PASV?cap_method=MINICAP_STREAM&&ori_method=ADBORI&&touch_method=MINITOUCH",
    ])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=None)