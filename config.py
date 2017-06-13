#!/usr/bin/env python3
# coding: utf-8

'''
为保证兼容，在下方admins中使用标准用法
在 admin_puids 中确保将机器人的puid 加入
机器人的puid 可以通过 bot.self.puid 获得
其他用户的PUID 可以通过 执行 export_puid.py 生成 data 文件，在data 文件中获取
'''
admin_puids = (
    '3414c23b',
    '80a52fdf',
    '69849278'
)

'''
定义需要管理的群
群的PUID 可以通过 执行 export_puid.py 生成 data 文件，在data 文件中获取
'''
group_puids = (
     '6128fb06',
     '2eaf2824',
)

 # 新人入群的欢迎语
welcome_text = '''🎉 欢迎 @{} 的加入！
😃 有问题请私聊我。
'''

invite_text = """欢迎您，我是「Linux 中国」微信群助手，
请输入如下关键字加入群：
- 运维 开发 安全 嵌入式 学生 找工作
- 运维密码  机器人 
- DBA PHP Python Golang Docker LFS vim
进群四件事：
1、阅读群公告，
2、修改群名片，
3、做自我介绍，
4、发个总计一元、一百份的红包
请言行遵守群内规定，违规者将受到处罚，拉入黑名单。"""


'''
设置群组关键词和对应群名
* 关键词必须为小写，查询时会做相应的小写处理

关于随机加群功能：
针对同类的群有多个的场景，例如群名 LFS群1、LFS群2、LFS群3...
设置关键词字典如下：
keyword_of_group = {
"lfs":"LFS群"
}
机器人会以"LFS群"为群名搜索，搜索结果为同类群名的列表，
再从列表中随机选取一个发出加群邀请。
'''
keyword_of_group = {
    "测试":"机器人测试群"
}

'''
地区群
'''
city_group = {
    "测试":"机器人测试群"
}

female_group="机器人测试群"

alert_group="机器人测试群"

turing_key=''