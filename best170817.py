#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:50:57 2024

@author: hussenot
"""

import numpy as np
from astropy.table import Table
from nmma.em.model import SVDLightCurveModel

sample_times = np.arange(0.1,15,0.1)
filts = ['ps1__g','ps1__r','ps1__i','ps1__z','ps1__y']
params={'KNphi':31.033359307564652,'log10_mej_dyn':-2.236983615436653,'log10_mej_wind':-0.9959807211519678,
        'KNtheta':1.2727477446277973*180/np.pi,'luminosity_distance':41.168672037183725}
model = SVDLightCurveModel('Bu2019lm', sample_times, svd_path='/home/thussenot/nmma/svdmodels/',
                           interpolation_type='sklearn_gp',filters=filts)
lbol,mAB = model.generate_lightcurve(sample_times,params)
ps1 = Table(mAB)
for f in ps1.keys():
    ps1[f] += 5*np.log10(params['luminosity_distance']*(10**6 /10))
ps1.write('/home/thussenot/kilonovae-H0/170817ps1.dat',format='ascii.csv',overwrite=True)

filts = ['2massj','2massh','2massks']
model = SVDLightCurveModel('Bu2019lm', sample_times, svd_path='/home/thussenot/nmma/svdmodels/',
                           interpolation_type='sklearn_gp',filters=filts)
lbol,mAB = model.generate_lightcurve(sample_times,params)
mass = Table(mAB)
for f in mass.keys():
    mass[f] += 5*np.log10(params['luminosity_distance']*(10**6 /10))
mass.write('/home/thussenot/kilonovae-H0/170817mass.dat',format='ascii.csv',overwrite=True)
