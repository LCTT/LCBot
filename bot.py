#!/usr/bin/env python3
# coding: utf-8

from wxpy import *
import config
import re
from wxpy.utils import start_new_thread
import time
import os
import platform
from importlib import reload
'''
使用 cache 来缓存登陆信息，同时使用控制台登陆
'''
console_qr = (False if platform.system() == 'Windows' else True)
bot = Bot('bot.pkl', console_qr=console_qr)
bot.messages.max_history = 0
'''
开启 PUID 用于后续的控制
'''
bot.enable_puid('wxpy_puid.pkl')
'''
邀请信息处理
'''
rp_new_member_name = (
    re.compile(r'^"((\n?.?)+)"通过'),
    re.compile(r'邀请"((\n?.?)+)"加入'),
    re.compile(r'invited "((\n?.?)+)" to the group chat'),
)

# 远程踢人命令: 移出 @<需要被移出的人>
rp_kick = re.compile(r'^(?:移出|移除|踢出|拉黑)\s*@((\n?.?)+?)(?:\u2005?\s*$)')

# 监控群监控等级
alert_level = 30  # DEBUG: 10, INFO: 20, WARNING: 30, ERROR: 40, FATAL: 50

# 下方为函数定义


def fresh_groups():
    '''
    管理员群及被管理群初始化
    '''
    global groups, admin_group
    # 格式化被管理群 Groups
    try:
        allgroups = bot.groups(update=True)
        groups = list(
            filter(lambda x: x.name.startswith(config.group_prefix),
                   allgroups.search(config.group_prefix)))
        groups += list(
            filter(lambda x: x.name in config.additional_groups, allgroups))
    except:
        print("查找被管理群出错！请检查被管理群前缀（group_prefix）是否配置正确")
        quit()

    # 格式化管理员群 Admin_group
    try:
        admin_group = ensure_one(
            bot.groups(update=True).search(config.admin_group_name))
    except:
        print("查找管理员群出错！请检查管理群群名（admin_group_name）是否配置正确")
        print("现将默认设置为只有本帐号为管理员")
        admin_group = None


def get_time():
    return str(time.strftime("%Y-%m-%d %H:%M:%S"))


def get_logger():
    '''
    机器人消息提醒设置
    '''
    global alert_receiver, logger
    if config.alert_group:
        try:
            alert_receiver = ensure_one(bot.groups().search(
                config.alert_group))
        except:
            print("警报群设置有误，请检查群名是否存在且唯一")
            alert_receiver = bot.file_helper
    else:
        alert_receiver = bot.file_helper

    try:
        for h in logger.handlers:
            logger.removeHandler(h)
    except:
        pass

    logger = get_wechat_logger(alert_receiver, level=alert_level)


def heartbeat():
    '''
    定时报告进程状态
    '''
    while bot.alive:
        time.sleep(3600)
        # noinspection PyBroadException
        try:
            logger.error(status())
        except ResponseError as e:
            if 1100 <= e.err_code <= 1102:
                logger.critical('LCBot offline: {}'.format(e))
                _restart()


def random_sleep():
    '''
    随机延时
    '''
    from random import randrange
    rnd_time = randrange(2, 7)
    time.sleep(rnd_time)


def _restart():
    '''
    重启机器人
    '''
    os.execv(sys.executable, [sys.executable] + sys.argv)


def status():
    '''
    状态汇报
    '''
    status_text = get_time() + " 机器人目前在线,共有好友 【" + str(len(
        bot.friends())) + "】 群 【" + str(len(bot.groups())) + "】"
    return status_text


def condition_invite(user):
    '''
    条件邀请
    '''
    if user.sex == 2:
        female_groups = bot.groups().search(config.female_group)[0]
        try:
            female_groups.add_members(user, use_invitation=True)
            pass
        except:
            pass
    if (user.province in config.city_group.keys()
            or user.city in config.city_group.keys()):
        try:
            target_city_group = bot.groups().search(
                config.city_group[user.province])[0]
            pass
        except:
            target_city_group = bot.groups().search(
                config.city_group[user.city])[0]
            pass
        try:
            if user not in target_city_group:
                target_city_group.add_members(user, use_invitation=True)
        except:
            pass


def from_admin(msg):
    """
    判断 msg 中的发送用户是否为管理员
    :param msg:
    :return:
    """
    if not isinstance(msg, Message):
        raise TypeError('expected Message, got {}'.format(type(msg)))
    from_user = msg.member if isinstance(msg.chat, Group) else msg.sender
    return (from_user in admin_group) if admin_group else from_user == bot.self


def remote_kick(msg):
    '''
    远程踢人命令
    '''
    if msg.type is TEXT:
        match = rp_kick.search(msg.text)
        if match:
            name_to_kick = match.group(1)

            if not from_admin(msg):
                if not config.silence_mode:
                    return '感觉有点不对劲… @{}'.format(msg.member.name)
                else:
                    print('非管理员 {} 想踢人...'.format(msg.member.name))
                    return

            member_to_kick = ensure_one(
                list(
                    filter(lambda x: x.name == name_to_kick,
                           msg.sender.members)))
            if member_to_kick == bot.self:
                return '无法移出 @{}'.format(member_to_kick.name)
            if member_to_kick in admin_group.members:
                return '无法移出 @{}'.format(member_to_kick.name)

            logger_msg = get_time() + str(
                " 【" + member_to_kick.name + "】 被 【" + msg.member.name +
                "】 移出 【" + msg.sender.name + "】")
            try:
                member_to_kick.set_remark_name("[黑名单]-" + get_time())
            except:
                logger_msg += "\n" + str(
                    "为 【" + member_to_kick.name + "】 设置黑名单时出错")

            if member_to_kick in msg.chat:
                msg.chat.remove_members(member_to_kick)
                kick_info = '成功移出 @{}'.format(member_to_kick.name)
            else:
                kick_info = '@{} 已不在群中'.format(member_to_kick.name)

            for ready_to_kick_group in groups:
                if member_to_kick in ready_to_kick_group:
                    ready_to_kick_group.remove_members(member_to_kick)
                    ready_to_kick_group.send(
                        str("【" + member_to_kick.name + "】 因其在 【" +
                            msg.sender.name + "】 的行为被系统自动移出"))
                    logger_msg += "\n" + str(
                        "【" + member_to_kick.name + "】 被系统自动移出 " +
                        ready_to_kick_group.name)

            logger.error(logger_msg)
            return kick_info


def get_new_member_name(msg):
    '''
    邀请消息处理
    '''
    # itchat 1.2.32 版本未格式化群中的 Note 消息
    from itchat.utils import msg_formatter
    msg_formatter(msg.raw, 'Text')

    for rp in rp_new_member_name:
        match = rp.search(msg.text)
        if match:
            return match.group(1)


def invite(user, keyword):
    '''
    定义邀请用户的方法。
    按关键字搜索相应的群，如果存在相应的群，就向用户发起邀请。
    '''
    from random import randrange
    group = bot.groups().search(config.keyword_of_group[keyword])
    if len(group) > 0:
        for i in range(0, len(group)):
            if user in group[i]:
                content = "您已经加入了 {} [微笑]".format(group[i].nick_name)
                user.send(content)
                return
        if len(group) == 1:
            target_group = group[0]
        else:
            index = randrange(len(group))
            target_group = group[index]
        try:
            target_group.add_members(user, use_invitation=True)
        except:
            user.send("邀请错误！机器人邀请好友进群已达当日限制。请您明日再试")
    else:
        user.send("该群状态有误，您换个关键词试试？")


fresh_groups()
get_logger()
logger.error(str("机器人登陆成功！" + get_time()))

start_new_thread(heartbeat)

# 下方为消息处理


@bot.register(msg_types=FRIENDS)
def new_friends(msg):
    '''
    处理加好友请求信息。
    如果验证信息文本是字典的键值之一，则尝试拉群。
    '''
    random_sleep()
    user = msg.card.accept()
    if msg.text.lower() in config.keyword_of_group.keys():
        invite(user, msg.text.lower())
    else:
        user.send(config.invite_text)
    random_sleep()
    condition_invite(user)


@bot.register(Friend, msg_types=TEXT)
def exist_friends(msg):
    random_sleep()
    if msg.sender.name.find("黑名单") != -1:
        return "您已被拉黑！"
    else:
        if msg.text.lower() in config.keyword_of_group.keys():
            invite(msg.sender, msg.text.lower())
        else:
            return config.invite_text


# 管理群内的消息处理
@bot.register(groups, except_self=False)
def wxpy_group(msg):
    ret_msg = remote_kick(msg)
    random_sleep()
    if ret_msg:
        return ret_msg
    elif msg.is_at and not config.silence_mode:
        if config.turing_key:
            tuling = Tuling(api_key=config.turing_key)
            tuling.do_reply(msg)
        else:
            return "忙着呢，别烦我！"
            pass


@bot.register(groups, NOTE)
def welcome(msg):
    name = get_new_member_name(msg)
    if name and not config.silence_mode:
        random_sleep()
        return config.welcome_text.format(name)


@bot.register(alert_receiver, except_self=False)
def alert_command(msg):
    if from_admin(msg):
        random_sleep()
        if msg.text == "状态":
            return status()
        elif msg.text == "重启":
            _restart()
        elif msg.text == "刷新":
            fresh_groups()
            return "群信息已更新，现有被管理群 【{}】，管理员 【{}】".format(
                len(groups),
                len(admin_group) if admin_group else 1)
        elif msg.text == "更新":
            reload(config)
            fresh_groups()
            get_logger()
            return "配置重载成功，现有被管理群 【{}】，管理员 【{}】".format(
                len(groups),
                len(admin_group) if admin_group else 1)


embed()
