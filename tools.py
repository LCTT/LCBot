#!/usr/bin/env python3
# coding: utf-8

from wxpy import *
import re


bot = Bot('bot.pkl', console_qr=True)


bot.enable_puid('wxpy_puid.pkl')

def search_group_puid(puid):
    return bot.groups().search(puid=puid)[0]

def search_user_puid(puid):
    return bot.friends().search(puid=puid)[0]

    
embed()