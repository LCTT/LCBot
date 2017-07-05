#!/usr/bin/env python3
# coding: utf-8

from wxpy import *
import platform


console_qr=(False if platform.system() == 'Windows' else True)
bot = Bot('bot.pkl', console_qr=console_qr)


bot.enable_puid('wxpy_puid.pkl')

def search_group_puid(puid):
    try:
        return bot.groups().search(puid=puid)[0]
        pass
    except:
        return "查无此群"
        pass

def search_user_puid(puid):
    try:
        return bot.friends().search(puid=puid)[0]
        pass
    except:
        return "查无此人"
        pass


embed()
