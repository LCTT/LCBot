#!/usr/bin/env python3
# coding: utf-8

from wxpy import *

'''
使用 cache 来缓存登陆信息，同时使用控制台登陆
'''
bot = Bot('bot.pkl', console_qr=False)

'''
检测使用是否是错误的帐号
'''
if bot.self.nick_name == '白宦成':
    raise ValueError("Wrong User!")


'''
验证信息
'''
def valid_msg(msg):
    return '运维密码' in msg.text.lower()

'''
关键字到群名的映射
'''
keyword_of_group = {'运维密码':"“运维密码”体验群", 'dba':"Linux中国Dba群",\
                    'php':"Linux中国Php群", 'python':"Linux中国Python群"}


'''
定义邀请用户的方法。
按关键字搜索相应的群，如果存在相应的群，就向用户发起邀请。
'''
def invite(user, keyword):
    group = bot.groups().search(keyword_of_group[keyword])
    print("查找到的群的数量是：", len(group))
    if len(group) > 0:
        group[0].add_members(user, use_invitation=True)
    else:
        print("没有找到", keyword_of_group[keyword])

'''
处理加好友请求信息。
如果验证信息文本是字典的键值之一，则尝试拉群。
'''
@bot.register(msg_types=FRIENDS)
def new_friends(msg):
    user = msg.card.accept()
    if msg.text.lower() in keyword_of_group.keys():
        invite(user, msg.text.lower())
    else:
        print(user.name, "的验证信息是：", msg.text.lower())
        user.send('Hello {}，你忘了填写加群口令，快回去找找口令吧'.format(user.name))


'''
处理好友消息。
如果消息文本是字典的键值之一，则尝试拉群。
'''
@bot.register(Friend, msg_types=TEXT)
def exist_friends(msg):
    if msg.text.lower() in keyword_of_group.keys():
        invite(msg.sender, msg.text.lower())
    else:
        print("来自 {} 的消息是：".format(msg.sender.name), msg.text.lower())
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
