#!/usr/bin/env python3
# coding: utf-8

from wxpy import *

'''
使用 cache 来缓存登陆信息，同时使用控制台登陆
'''
bot = Bot('bot.pkl',console_qr=False)

'''
检测使用是否是错误的帐号
'''
if bot.self.nick_name  == '白宦成' :
    raise ValueError("Wrong User!")


'''
验证信息
'''
def valid_msg(msg):
    return '运维密码' in msg.text.lower()



'''
定义邀请用户的方法
'''
def invite(user):
    group =  bot.groups().search('“运维密码”体验群')
    group[0].add_members(user, use_invitation=True)

'''
处理加好友信息
'''
@bot.register(msg_types=FRIENDS)
def new_friends(msg):
    user = msg.card.accept()
    if valid_msg(msg):
        invite(user)
    else:
        user.send('Hello {}，你忘了填写加群口令，快回去找找口令吧'.format(user.name))


'''
处理好友消息
'''
@bot.register(Friend,msg_types=TEXT)
def exist_friedns(msg):
    if valid_msg(msg):
        invite(msg.sender)
    else:
        return '口令不正确！'

teamgroup = ensure_one(bot.groups().search('“运维密码”体验群'))

welcome_text = '''\U0001F389 欢迎加入运维密码体验群！
\U0001f603 有问题可以直接@白宦成
\U0001F4D6 提问前请看 dwz.cn/passwd'''


@bot.register(teamgroup)
def help_msg(msg):
    if msg.is_at:
        if '帮助' in msg.text.lower():
            return welcome_text
        else:
            return '我没听懂你说的啥[奸笑]'



embed()
