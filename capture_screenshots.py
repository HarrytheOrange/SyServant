import paramiko
from PIL import ImageGrab
import threading
import time
import os
import requests
from pathlib import Path


def func():
    # 目录不存在，则创建截图存放的目录
    if Path("screenshots").is_dir() != 1:
        os.mkdir("screenshots")

    # 开始截图
    pic = ImageGrab.grab((0, 0, 1920, 1080))  # 指定截取坐标(左边X，上边Y，右边X，下边Y)
    pic_name = "./screenshots/" + time.strftime('%Y%m%d%H%M%S') + '.jpg'
    print(pic.mode)
    # pic.mode = 'RGB'
    pic.save(pic_name)

    timer = threading.Timer(3, func, [])
    timer.start()
    
    
func()
