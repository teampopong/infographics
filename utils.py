#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import json
import struct

def hex2rgb(hexstr):
    return struct.unpack('BBB', hexstr.decode('hex'))

def popong_colors(colortype='hex'):
    with open('static/colors.json', 'r') as f:
        d = json.load(f)
    if colortype=='rgb':
        d = { k: hex2rgb(v[1:]) for k, v in d.items() }
    return d
