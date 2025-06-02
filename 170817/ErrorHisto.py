#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 15:02:33 2025

@author: hussenot
"""

from astropy.table import Table
from astropy.time import Time
import numpy as np
import matplotlib.pyplot as plt

t = Table.read('/home/hussenot/H0/kilonovae-H0/170817/AT2017gfoMWcorrected.dat', format='ascii.no_header',
               names=['time','filter','mag','err'])

true = t[t['err']!=np.inf]

fig, ax = plt.subplots(1,1, figsize = (10,6))

ax.hist(true['err'], bins=50, cumulative=False, density=False)
ax.set_xlabel(r'Observed magnitudes uncertainty $\sigma_i^j$ [mag]', fontsize=20)
# ax.set_title('Histogram of observational uncertainties in the AT2017gfo lightcurve', fontsize=18)

fig.savefig('/home/hussenot/H0/plots/Obs_histo.pdf', format='pdf', bbox_inches='tight')