#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:50:57 2024

@author: hussenot
"""

import numpy as np
from astropy.table import Table
from nmma.em.model import SVDLightCurveModel
import json

sample_times = np.arange(0.1,15,0.2)
filts = ['ps1__g','ps1__r','ps1__i','ps1__z','ps1__y']
filts = ['2massj','2massh','2massks']

model = SVDLightCurveModel('Bu2019lm', sample_times, svd_path='/home/thussenot/nmma/svdmodels/',
                           interpolation_type='sklearn_gp',filters=filts)

results = {}
for f in filts:
    results[f]=np.zeros((11,11,11,11,75))

for i,phi in enumerate(np.arange(15,76,6)):
    print('Progress '+str(i)+'/10')
    for j,dyn in enumerate(np.arange(-3,-1.49,0.15)):
        for k,wind in enumerate(np.arange(-2,-0.49,0.15)):
            for l,theta in enumerate([np.arccos(k/10)*180/np.pi for k in range(11)]):
                # name = str(i)+'_'+str(j)+'_'+str(k)+'_'+str(l)
                params= {'KNphi':phi,'log10_mej_dyn':dyn,'log10_mej_wind':wind,
                        'KNtheta':theta,'luminosity_distance':40}
                
                lbol,mAB = model.generate_lightcurve(sample_times,params)
                mass = Table(mAB)
                for f in filts:
                    mass[f] += 5*np.log10(params['luminosity_distance']*(10**6 /10))
                    mass[f] = np.round(mass[f],decimals=3)
                    results[f][i,j,k,l] = mass[f]

for filt in filts:
    with open('/home/thussenot/kilonovae-H0/SimuLC_grid_'+filt+'.npy', 'wb') as f:
        np.save(f, results[filt])
        # json.dump(results[filt], f, ensure_ascii=False, indent=4)
