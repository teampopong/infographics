#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import struct

def hex2rgb(hexstr):
    return struct.unpack('BBB', hexstr.decode('hex'))
