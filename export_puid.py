#!/usr/bin/env python3
# coding: utf-8

from wxpy import *
import platform

'''
使用 cache 来缓存登陆信息，同时使用控制台登陆
'''
console_qr=(False if platform.system() == 'Windows' else True)
bot = Bot('bot.pkl', console_qr=console_qr)


'''
开启 PUID 用于后续的控制
'''
bot.enable_puid('wxpy_puid.pkl')

friends = bot.friends()
groups = bot.groups()

with  open('data', 'w',encoding='UTF-8') as output:
    output.write("-----Bots-------\n")
    output.write(str(bot.self.name + '--->'+ bot.self.puid + "\n"))
    output.write("-----Friends-------\n")
    for i in friends:
        output.write(str(i.nick_name + " ---> " + i.puid + "\n"))

    output.write("-----Groups-------\n")
    for i in groups:
        output.write(str(i.name + " ---> " + i.puid + "\n"))

print("数据输出成功！")
