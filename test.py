#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os
import sys

SCRIPT_PATH = os.path.split(os.path.realpath(__file__))[0] + os.sep
RUNNING_PATH = sys.path[0] + os.sep

import ZL.ZLReflection
import ZL.ZLSharpTV
import Node.NodeItem
import Node.SharpTV_NodeItem
import Node.Computer_NodeItem


if __name__ == '__main__':
    item_root = Node.NodeItem.NodeItem('Root')

    item_sharptv = Node.SharpTV_NodeItem.SharpTV_NodeItem('Sharp TV', '192.168.1.4', 10002)
    item_sharptv.node_init()
    item_root.items.append(item_sharptv)

    item_zelotoj_note = Node.Computer_NodeItem.Computer_NodeItem('Server', '192.168.1.9', 22, mac='60:a4:4c:b5:8f:06')
    item_zelotoj_note.node_init()
    item_root.items.append(item_zelotoj_note)

    dict_item = ZL.ZLReflection.ZLReflection.to_value(item_root)
    print ZL.ZLReflection.ZLReflection.to_json_string(dict_item)
    item_zelotoj_note.items[0].node_run()
    item_zelotoj_note.items[1].node_run()
