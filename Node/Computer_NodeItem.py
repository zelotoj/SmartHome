#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os
import sys
import NodeItem
import ZL.ZLNetworkTools
from wakeonlan import wol

SCRIPT_PATH = os.path.split(os.path.realpath(__file__))[0] + os.sep
RUNNING_PATH = sys.path[0] + os.sep


class Computer_NodeItem(NodeItem.NodeItem):
    def __init__(self, name=None, ip=None, port=None, is_tcp=True, mac=None, init=None, func=None):
        super(Computer_NodeItem, self).__init__(name, ip, port, is_tcp, mac, init, func)

    def node_init(self):
        super(Computer_NodeItem, self).node_init()
        if self.ip and self.mac:
            node_wakeup = NodeItem.NodeItem('Wake up', func=self.wakeup)
            node_wakeup.enable = not self.enable
            self.items.append(node_wakeup)

    def node_run(self):
        super(Computer_NodeItem, self).node_run()

    def wakeup(self):
        if self.mac:
            wol.send_magic_packet(mac.upper())
