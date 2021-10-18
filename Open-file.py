# !/usr/bin/python
# -*- coding: utf-8 -*-

# 功能：打开目录模块
# 作者：吴勇
# 创建时间：2020/10/10

import os


start_directory = r'C:\Users\dell\AppData\Local\LanShanOffice\dump'
os.startfile(start_directory)


def huoqu(self, event):
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    path = winreg.QueryValueEx(key, "Local AppData")[0]
    print(path)
    pwd = path + "{}".format("\\") + "{}".format("LanShanOffice") + "{}".format("\\") + "{}".format("dump")
    print(pwd)
    dlg = wx.DirDialog(self, u"选择文件夹", pwd, style=wx.DD_DEFAULT_STYLE)
    dlg.ShowModal() == wx.ID_OK
    # path1 = dlg.GetPath()