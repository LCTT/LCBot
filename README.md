# LCBot Linux中国微信机器人

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/bestony/LCBot/blob/master/LICENSE) ![](https://img.shields.io/badge/Language-Python-blue.svg) ![](https://img.shields.io/badge/Python-3.X-red.svg)

![](https://postimg.aliavv.com/mbp/b69eb.png)

LCBot 是一个为 Linux 中国服务的微信机器人，主要为 Linux 中国下的微信群做管理、维护等工作。

##  演示
![linux_cn](https://ooo.0o0.ooo/2017/04/28/5903576f5d014.jpeg)

扫描二维码或搜索微信号`linux_cn`，回复关键词 `机器人` ，即可拉入本项目微信讨论群

视频教程地址：[点我查看视频教程](http://dwz.cn/lcbot) | [Linux/macOS 使用教程](https://v.qq.com/x/page/k03996ry5o1.html) |[Win 10完整使用教程](https://v.qq.com/x/page/y03990en5qu.html)

免登录意见反馈：[我要新功能！](https://wj.qq.com/s/1334670/bb03/)

## 特性

1. 关键词添加好友自动拉群
2. 私聊发送关键词自动加群
3. 新用户进群自动发送欢迎
4. 设定管理员，管理员可以通过发送命令T人（需要机器人是群主）

## 需要
- Python 3

## 安装
下载源码
```
git clone https://github.com/LCTT/LCBot.git
```
安装拓展
```
cd LCBot
pip3 install -U wxpy
pip3 install pillow
```

## 使用
首先，获取puid
```
python3 export_puid.py
```
执行成功后，在当前目录下会生成一个data文件，在data文件中，你可以看的用户的puid和群的puid
编辑bot.py中第 34 行和 41行，分别填入用户的puid 和群的puid 
执行命令
```
python3 bot.py
```
## FAQ
查看 [FAQ](https://github.com/LCTT/LCBot/wiki/FAQ)
## Todo

查看 [Todo](TODO.md)

## 贡献指南

查看 [CONTRIBUTING](CONTRIBUTING.md)

## LICENSE

代码基于 [MIT](LICENSE) 协议开源

文档以 [CC-BY-ND](https://creativecommons.org/licenses/by-nd/4.0/) 协议分享

## 致谢

- [wxpy](https://github.com/youfou/wxpy) : 微信机器人 / 优雅而强大的微信个人号 API
