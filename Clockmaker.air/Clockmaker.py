# -*- encoding=utf8 -*-
__author__ = "Admin"
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()


from airtest.core.api import *


# My Device - huawei media pad 5 lite

start_app('com.belkatechnologies.clockmaker')
wait(Template(r"tpl1628182556832.png", rgb=True, record_pos=(-0.266, 0.549), resolution=(1200, 1920)))

if assert_exists(Template(r"tpl1628182556832.png", rgb=True, record_pos=(-0.266, 0.549), resolution=(1200, 1920)), "Кнопка стала достпна."):
    touch(Template(r"tpl1628182556832.png", rgb=True, record_pos=(-0.266, 0.549), resolution=(1200, 1920)))
else:
    wait(Template(r"tpl1628182556832.png", rgb=True, record_pos=(-0.266, 0.549), resolution=(1200, 1920))) and touch(Template(r"tpl1628182556832.png", rgb=True, record_pos=(-0.266, 0.549), resolution=(1200, 1920)))
if assert_exists(Template(r"tpl1628176112911.png", record_pos=(0.449, -0.44), resolution=(1200, 1920)), "Меню с настройками появилось."):
    touch(Template(r"tpl1628176759901.png", record_pos=(0.453, -0.434), resolution=(1200, 1920)))
else:
    wait(Template(r"tpl1628176782042.png", record_pos=(0.458, -0.433), resolution=(1200, 1920))) and touch(Template(r"tpl1628176759901.png", record_pos=(0.453, -0.434), resolution=(1200, 1920)))

wait(Template(r"tpl1628176832564.png", record_pos=(0.046, -0.483), resolution=(1200, 1920)))

if assert_exists(Template(r"tpl1628176875765.png", record_pos=(0.052, -0.473), resolution=(1200, 1920)), "Панель появилась."):
    touch(Template(r"tpl1628176895058.png", record_pos=(0.195, -0.475), resolution=(1200, 1920))) 
else:
    wait(Template(r"tpl1628176922694.png", record_pos=(0.06, -0.479), resolution=(1200, 1920))) and touch(Template(r"tpl1628176939001.png", record_pos=(0.191, -0.471), resolution=(1200, 1920))) 

touch(Template(r"tpl1628177040674.png", record_pos=(-0.438, 0.644), resolution=(1200, 1920)))

wait(Template(r"tpl1628177069479.png", record_pos=(0.348, 0.653), resolution=(1200, 1920)))

assert_not_exists(Template(r"tpl1628177104366.png", record_pos=(0.188, -0.479), resolution=(1200, 1920)), "Кнопки нет на экране.")




