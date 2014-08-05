#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import sys

from PIL import Image


def check_input():
    if not len(sys.argv) > 1:
        raise Exception('Usage: ./build.py [year]/[title]')

    if not os.path.isdir(sys.argv[1]):
        raise IOError('Path does not exist')

def draw_graph():
    os.chdir(sys.argv[1])
    runfile = [f for f in os.listdir('.')\
                 if os.path.basename(f).rsplit('.', 1)[0]=='draw'][0]
    os.system('./%s' % runfile)
    Image.open('drawing.png').show()


if __name__=='__main__':
    check_input()
    draw_graph()
