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
#params={'KNphi':60,'log10_mej_dyn':np.log(0.010),'log10_mej_wind':np.log(0.05),
#        'KNtheta':np.arccos(0.8)*180/np.pi,'luminosity_distance':40}
#params={'KNphi':53,'log10_mej_dyn':np.log(0.007),'log10_mej_wind':np.log(0.04),
#        'KNtheta':np.arccos(0.75)*180/np.pi,'luminosity_distance':40}
params={
        # 'KNphi':28.00338113,'log10_mej_dyn':-2.1685562,
        # 'log10_mej_wind':-1.62913266,'KNtheta':np.arccos(0.93810532)*180/np.pi,
        # # 'KNphi':28.84181664,'log10_mej_dyn':-1.53114099,
        # 'log10_mej_wind':-0.78967631,'KNtheta':np.arccos(0.99297351)*180/np.pi,
        # 'KNphi':21.14433759,'log10_mej_dyn':-1.89340053,
        # 'log10_mej_wind':-0.77958405,'KNtheta':np.arccos(0.50616015)*180/np.pi,
        # 'KNphi':49.46252534,'log10_mej_dyn':-2.45002188,
        # 'log10_mej_wind':-1.77082526,'KNtheta':np.arccos(0.5779006)*180/np.pi,
        # 'KNphi':59.30197033,'log10_mej_dyn':-2.72305989,
        # 'log10_mej_wind':-1.8503249,'KNtheta':np.arccos(0.10882965)*180/np.pi,
        # 'KNphi':26.84136451,'log10_mej_dyn':-2.97836487,
        # 'log10_mej_wind':-0.69157357,'KNtheta':np.arccos(0.64894437)*180/np.pi,
        # 'KNphi':51.63413138,'log10_mej_dyn':-2.22463734,
        # 'log10_mej_wind':-0.51735504,'KNtheta':np.arccos(0.09700895)*180/np.pi,
        # 'KNphi':63.41187,'log10_mej_dyn':-1.8359392,
        # 'log10_mej_wind':-1.1377273,'KNtheta':np.arccos(0.75866399)*180/np.pi,
        # 'KNphi':24.90001225,'log10_mej_dyn':-2.04675365,
        # 'log10_mej_wind':-1.58428609,'KNtheta':np.arccos(0.17907588)*180/np.pi,
        # 'KNphi':40.11151919,'log10_mej_dyn':-2.39641537,
        # 'log10_mej_wind':-0.98929691,'KNtheta':np.arccos(0.109746)*180/np.pi,
        'KNphi':42.30267616,'log10_mej_dyn':-1.93035833,
        'log10_mej_wind':-1.19203596,'KNtheta':np.arccos(0.72135561)*180/np.pi,
        # 'KNphi':18.87695094,'log10_mej_dyn':-1.99174893,
        # 'log10_mej_wind':-1.96983847,'KNtheta':np.arccos(0.57928337)*180/np.pi,
        # 'KNphi':55.06204702,'log10_mej_dyn':-2.8388448,
        # 'log10_mej_wind':-1.13579142,'KNtheta':np.arccos(0.748148 )*180/np.pi,
        # 'KNphi':53.91511799,'log10_mej_dyn':-2.91796954,
        # 'log10_mej_wind':-0.88169226,'KNtheta':np.arccos(0.29600959)*180/np.pi,
        # 'KNphi':28.64139531,'log10_mej_dyn':-2.28273025,
        # 'log10_mej_wind':-1.18216514,'KNtheta':np.arccos(0.18615174)*180/np.pi,
        # 'KNphi':41.64408314,'log10_mej_dyn':-2.10663757,
        # 'log10_mej_wind':-1.38307693,'KNtheta':np.arccos(0.37029653)*180/np.pi,
        # 'KNphi':41.50236677,'log10_mej_dyn':-2.78966645,
        # 'log10_mej_wind':-1.48061402,'KNtheta':np.arccos(0.47710132)*180/np.pi,
        # 'KNphi':30.12996258,'log10_mej_dyn':-1.71379507,
        # 'log10_mej_wind':-1.79612824,'KNtheta':np.arccos(0.24295105)*180/np.pi,
        # 'KNphi':52.79320033,'log10_mej_dyn':-2.55730184,
        # 'log10_mej_wind':-1.42620425,'KNtheta':np.arccos(0.25833745)*180/np.pi,
        # 'KNphi':61.305053,'log10_mej_dyn':-2.75972211,
        # 'log10_mej_wind':-1.89701975,'KNtheta':np.arccos(0.16137993)*180/np.pi,
        'luminosity_distance':40}
        

name = 'InjectionBaseLightcurve13'
model = SVDLightCurveModel('Bu2019lm', sample_times, svd_path='/home/thussenot/nmma/svdmodels/',
                           interpolation_type='sklearn_gp',filters=filts)
lbol,mAB = model.generate_lightcurve(sample_times,params)
ps1 = Table(mAB)
for f in ps1.keys():
    ps1[f] += 5*np.log10(params['luminosity_distance']*(10**6 /10))
ps1.write('/home/thussenot/kilonovae-H0/Injection_Recovery_IterationsVariation/'+name+'/'+name+'_ps1.dat',format='ascii.csv',overwrite=True)

filts = ['2massj','2massh','2massks']
model = SVDLightCurveModel('Bu2019lm', sample_times, svd_path='/home/thussenot/nmma/svdmodels/',
                           interpolation_type='sklearn_gp',filters=filts)
lbol,mAB = model.generate_lightcurve(sample_times,params)
mass = Table(mAB)
for f in mass.keys():
    mass[f] += 5*np.log10(params['luminosity_distance']*(10**6 /10))
mass.write('/home/thussenot/kilonovae-H0/Injection_Recovery_IterationsVariation/'+name+'/'+name+'_mass.dat',format='ascii.csv',overwrite=True)
