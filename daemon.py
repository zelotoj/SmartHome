#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os
import sys

SCRIPT_PATH = os.path.split(os.path.realpath(__file__))[0] + os.sep
RUNNING_PATH = sys.path[0] + os.sep

import ZL.ZLDaemon
import ZL.ZLThread
import ZL.ZLWebpy
import ZL.ZLWebServer
import ZL.web

render = ZL.web.template.render('templates/', globals={})
menu_urls = (
    '/', 'menu_index',
)
menu_links = [
    ('http://192.168.1.8:80/', '智能遥控器'),
    ('http://192.168.1.8:8081/', '客厅摄像头'),
    ('http://192.168.1.1:82/', '客户端日志'),
    ('http://192.168.1.1:81/', '路由器设置')
    ]


class menu_index:
    def GET(self):
        global menu_links
        user_cmd = ZL.web.input(index=0)
        # raise web.seeother("/")
        return render.index(menu_links, int(user_cmd.index))


def web_frame():
    frame = ZL.ZLWebServer.ZLWebServer(8888)
    frame.start()


def web_menu():
    web_menu = ZL.ZLWebpy.ZLWebpy(menu_urls, globals())
    web_menu.run(8889)


def daemon_worker():
    thread_web_menu = ZL.ZLThread.ZLThread(web_menu)
    thread_web_menu.start()
    thread_web_menu.join(1)
    web_frame()

if __name__ == '__main__':
    daemon_worker()
    # daemon = ZL.ZLDaemon.ZLDaemon(daemon_worker, 'smarthome.pid')
    # daemon.start()
