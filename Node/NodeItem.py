#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os
import sys
import ZL.ZLNetworkTools

SCRIPT_PATH = os.path.split(os.path.realpath(__file__))[0] + os.sep
RUNNING_PATH = sys.path[0] + os.sep


class NodeItem(object):
    def __init__(self, name=None, ip=None, port=None, is_tcp=True, mac=None, init=None, func=None):
        self.name = name
        self.value = None
        self.enable = True
        self.visible = True
        self.ip = ip
        self.port = port
        self.is_tcp = is_tcp
        self.mac = mac
        self.items = list()
        self.__init = init
        self.__func = func

    def ping(self):
        result = False
        if self.ip:
            result = ZL.ZLNetworkTools.ZLNetworkTools.ping(self.ip)
        return result

    def port_test(self):
        result = False
        if self.ip and self.port:
            result = ZL.ZLNetworkTools.ZLNetworkTools.port_test(self.ip, self.port, self.is_tcp)
        return result

    def node_init(self):
        if self.ip:
            if self.port:
                self.enable = self.port_test()
            else:
                self.enable = self.ping()
        else:
            self.enable = True
        if self.__init:
            self.__init()

    def node_run(self):
        if self.__func:
            self.__func()
