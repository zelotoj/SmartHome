#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os
import sys
import ZL.ZLSharpTV
import NodeItem

SCRIPT_PATH = os.path.split(os.path.realpath(__file__))[0] + os.sep
RUNNING_PATH = sys.path[0] + os.sep


class SharpTV_NodeItem(NodeItem.NodeItem):
    def __init__(self, name=None, ip=None, port=None, is_tcp=True, mac=None, init=None, func=None):
        super(SharpTV_NodeItem, self).__init__(name, ip, port, is_tcp, mac, init, func)
        self.__sharp_tv = None

    def node_init(self):
        super(SharpTV_NodeItem, self).node_init()
        if self.ip and self.port and self.enable:
            self.__sharp_tv = ZL.ZLSharpTV.ZLSharpTV(self.ip, self.port)
            power_state = self.__sharp_tv.get_power() > 0
            node_power_on = NodeItem.NodeItem('Power On', func=self.power_on)
            node_power_on.enable = not power_state
            self.items.append(node_power_on)
            node_power_off = NodeItem.NodeItem('Power Off', func=self.power_off)
            node_power_off.enable = power_state
            self.items.append(node_power_off)

    def power_on(self):
        self.__sharp_tv.set_power(ZL.ZLSharpTV.POWER_VALUE.POWER_ON)

    def power_off(self):
        self.__sharp_tv.set_power(ZL.ZLSharpTV.POWER_VALUE.POWER_OFF)
