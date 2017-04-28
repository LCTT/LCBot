#!/usr/bin/env python3
# coding: utf-8

from wxpy import *

'''
使用 cache 来缓存登陆信息，同时使用控制台登陆
'''
bot = Bot('bot.pkl', console_qr=True)

'''
设置群组关键词和对应群名
* 关键词必须为小写，查询时会做相应的小写处理
'''
keyword_of_group = {
    "lfs":"Linux中国◆LFS群",
    "dba":"Linux中国◆DBA群"
}
'''
定义邀请用户的方法。
按关键字搜索相应的群，如果存在相应的群，就向用户发起邀请。
'''
def invite(user, keyword):
    group = bot.groups().search(keyword_of_group[keyword])
    print(len(group))
    if len(group) > 0:
        target_group = ensure_one(group)
        target_group.add_members(user, use_invitation=True)
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
        return """欢迎您，我是 Linux 中国 微信群助手，
请输入如下关键字加入群：
运维 开发 嵌入式  运维密码 学生  机器人 安全
DBA PHP Python Golang Docker LFS
进群四件事：
1、阅读群公告，
2、修改群名片，
3、做自我介绍，
4、发个总计一元、一百份的红包
请言行遵守群内规定，违规者将受到处罚，拉入黑名单。"""
'''
处理好友消息。
如果消息文本是字典的键值之一，则尝试拉群。
'''
@bot.register(Friend, msg_types=TEXT)
def exist_friends(msg):
    if msg.text.lower() in keyword_of_group.keys():
        invite(msg.sender, msg.text.lower())
    else:
        return """欢迎您，我是 Linux 中国 微信群助手，
请输入如下关键字加入群：
运维 开发 嵌入式  运维密码 学生 机器人 安全
DBA PHP Python Golang Docker LFS
进群四件事：
1、阅读群公告，
2、修改群名片，
3、做自我介绍，
4、发个总计一元、一百份的红包
请言行遵守群内规定，违规者将受到处罚，拉入黑名单。"""
embed()