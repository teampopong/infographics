#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import pylab as pl

x = range(1, 19)
d = pd.read_csv('data.csv')

pl.clf()
pl.plot(x, d['reelection'], 'o-', label='reelection')
pl.plot(x, d['rerun'], 'o-', label='rerun')
pl.plot(x, d['ratio'], 'o-', label='incumbent ratio')
pl.fill_between(x, d['ratio'], np.zeros(len(d.index)), facecolor='red',\
        alpha=0.1)
pl.legend(loc='upper left')
pl.xlabel('assembly_id')
pl.ylabel('rate')
pl.xlim([1, max(x)])
pl.ylim([0, 1])
pl.xticks(x)
pl.savefig('drawing.png')
