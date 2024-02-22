# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time

import win32com.client

import os
import sys
import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_cmd(cmd):
    res = os.popen(cmd)
    output = res.buffer.read().decode("gbk")
    return output


def click_pos(dm, x, y):
    dm.MoveTo(x, y)
    time.sleep(0.1)
    dm.LeftClick()



def dm_test(hwnd, dm):
    ret = dm.BindWindow(hwnd, "dx2", "windows", "windows", 0)

    print("bind window", ret)
    # dm_ret = dm.Capture(337,122,358,144, "shop.bmp")
    # print("capture", dm_ret)
    # dm_ret = dm.SetPicFindRange(left, top, right, bottom)
    # print("设置找图的range", dm_ret)

    # ret, x, y = dm.FindPic(0, 0, 2000, 2000, "shop.bmp", "000000", 0.8, 0)

    x, y = 547, 278
    print("x = ", x, "y = ", y)

    # ret, colorx, colory = dm.FindColor(0,0, 1600, 900, "8c7bfe", 1.0, 0)
    print('ret', ret, x, y, "error", dm.getLastError())
    # click_pos(dm, colorx, colory)

    # ret = dm.FindStr(0,0, 1200, 1200,"雷电","000000",0.8)
    # base_path = dm.GetBasePath()
    # print("base_path", base_path)
    # dm_ret = dm.SetPath(base_path)

    # print("set_base", dm_ret )
    # dm_ret = dm.SetDict(0, "E:\\Download\\125034f3ci2vxv6jy7pci6 (1)\\dm_soft.txt")
    dm_ret = dm.SetDict(0, "dm_soft.txt")
    print("set dict", dm_ret)

    ret =  dm.FindStr(0, 0, 2000, 2000,"零零","000000-000000",1.0)
    print("findStr", ret)
    # ret = dm.FindPic(0, 0, 2000, 2000, "leidian.bmp", "000000", 0.8, 0)
    # click_pos(dm, ret[1], ret[2])
    # print("findPic", ret)
    # ret = dm.Ocr(202,131,255,151,"8f9196-000000|a5a7aa-000000|4b4d55-000000|797b81-000000",0.8)
    click_pos(dm, 453,215)


    # 判断是否有商城图标
    # while True:
    #     ret, x, y = dm.FindPic(0, 0, 2000, 2000, "shop.bmp", "000000", 0.8, 0)
    #     if not ret:
    #         click_pos(dm, 200, 200)
    #         time.sleep(0.5)
        # rett
    ret = dm.UnBindWindow()
    print("unbindWindow", ret)


def findLeidian(dm):
    hwnds = dm.EnumWindow(0, "雷电模拟器", "", 1 + 4 + 8 + 16)
    # print(hwnds)
    """
    item =  雷电模拟器 LDPlayerMainFrame
sub  3474738 TheRender RenderWindow
item =  雷电模拟器-1 LDPlayerMainFrame
sub  4854868 TheRender RenderWindow
item =  雷电模拟器 FindPic失败_百度搜索 - Google Chrome Chrome_WidgetWin_1
sub  1513274 Chrome Legacy Window Chrome_RenderWidgetHostHWND

    """
    # print("直接找 ", dm.FindWindowEx(0, "TheRender", "RenderWindow"))
    leidians = []
    for item in hwnds.split(","):
        # print("item = ", dm.GetWindowTitle(item), dm.GetWindowClass(item))
        sub = dm.FindWindowEx(item, "", "")
        leidians.append(sub)
        # print("sub ", sub , dm.GetWindowTitle(sub), dm.GetWindowClass(sub))
    return leidians


def start_action():

    dm = win32com.client.Dispatch("dm.dmsoft")
    print(dm.ver())

    dm_ret = dm.Reg("yonghu84f875b03fb0d5c536a56a631156628a","yk0061141" )
    print("register " , dm_ret)
    print("is 64 os ", dm.Is64Bit())

    ret = dm.bindWindow(67866, "dx", "windows", "windows", 0)
    print("bindWindow", ret)
    click_pos(dm, 294,93)


if __name__ == "__main__":
    if is_admin():
        print("now is already admin")
        # dm_test()
        # findLeidian()
        start_action()
    else:
        print("run as admin")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        # findLeidian()
        start_action()

        print(is_admin())
        if is_admin():
            print('111')

        else:
            print("222")
