# LCBot Linux中国微信机器人

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/bestony/LCBot/blob/master/LICENSE) ![](https://img.shields.io/badge/Language-Python-blue.svg) ![](https://img.shields.io/badge/Python-3.X-red.svg)

![](https://postimg.aliavv.com/mbp/b69eb.png)

LCBot 是一个为 Linux 中国服务的微信机器人，主要为 Linux 中国下的微信群做管理、维护等工作。

**注：使用本项目有被微信网页版封号的风险，故而现已基本停止开发。如继续使用本项目，产生的后果请自行承担。**

##  演示

视频教程地址：[点我查看视频教程集合](http://dwz.cn/lcbot) | [Linux/macOS 使用教程](https://v.qq.com/x/page/k03996ry5o1.html) |[完整版 Win 10 使用教程](https://v.qq.com/x/page/y03990en5qu.html) | [单群版机器人使用教程](https://v.qq.com/x/page/p05007bqjv1.html)

注：该系列视频使用的是旧版 LCBot，新版请以本文的文字内容为准。

免登录意见反馈：[我要新功能！](https://wj.qq.com/s/1334670/bb03/)

## 特性

>> 注：使用本项目有被微信网页版封号的风险，故而现已基本停止开发。如继续使用本项目，产生的后果请自行承担。

1. 关键词添加好友自动拉群
2. 私聊发送关键词自动加群
3. 新用户进群自动发送欢迎
4. 设定管理员，管理员可以通过发送命令T人（需要机器人是群主）
5. 监控群每小时发送心跳包
6. 管理员踢人监控群内留底
7. 被拉黑的用户，无法被再次拉群。需要管理员手动释放。
8. 管理员在监控群发送指令获取状态或进行特定操作（现支持“状态”、“重启”、“刷新”）

## 需要
- Python 3
- wxpy

## 安装
下载源码
```
git clone https://github.com/LCTT/LCBot.git
```
安装拓展
```
cd LCBot
pip3 install -U -r  requirements.txt
```
## Docker 版本
感谢 [@OSMeteor](https://github.com/OSMeteor/pythonlcbot) 提供的 Docker 版本

使用方法：

```
docker pull osmeteor/pythonlcbot
# 或者使用国内镜像: docker pull registry.docker-cn.com/osmeteor/pythonlcbot
docker run -i -t osmeteor/pythonlcbot /bin/bash
cd /opt/LCBot
python bot.py
```

## 使用
首先，进行机器人相关设定（注：现已废弃旧版中使用 puid 的配置方案，不再需要导出 puid 数据）

编辑 config.py 中第 11 行和 22 行，分别填入管理员群的名称（`admin_group_name`）和被管理群的前缀（`group_prefix`）

编辑 config.py 中第 68 行，填入监控群的名称（`alert_group`）

编辑 config.py 中第 70 行，填入图灵机器人的 APIKEY（`turing_key`）

以及 config.py 中的欢迎语、邀请消息、邀请关键词等相关配置

随后执行以下命令运行机器人（首次登录需要扫二维码）
```
python3 bot.py
```

> 如果执行后，如果二维码展示不正常，可以执行 `sudo localectl set-locale LANG=C.UTF-8`

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
