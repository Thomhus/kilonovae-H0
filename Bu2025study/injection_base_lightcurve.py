#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:50:57 2024

@author: hussenot
"""

import numpy as np
from astropy.table import Table
from nmma.em.model import FiestaKilonovaModel
from fiesta.inference.lightcurve_model import FluxModel

import os, os.path
import errno

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
            
# tab = np.zeros((100,9))
# Injections = Table(tab, names=['log10_mej_dyn','v_ej_dyn','Ye_dyn','log10_mej_wind','v_ej_wind','Ye_wind','inclination_EM',
#                                'luminosity_distance','redshift'])
# Injections.write('/home/hussenot/Bu2025study/Bu25injections.csv', format='ascii.csv', overwrite=True)

sample_times = np.arange(0.1,15,0.1)
filts = ['ps1::g','ps1::r','ps1::i','ps1::z','ps1::y']
model = FluxModel(name='Bu2025', filters=filts, directory = "/home/hussenot/fiestaEM/surrogates/KN/Bu2025_MLP/model/")
pardist = model.parameter_distributions
Injections = Table.read('/home/hussenot/Bu2025study/Bu25injections.csv', format='ascii.csv')

for N in range(100):
    name = 'Bu25Injection'+str(N)
    if Injections[N]['luminosity_distance']!=0:
        print('Recovering existing injection: Overwrite avoided row '+str(N))
        params={}
        for p, val in pardist.items():
            params[p] = Injections[N][p]
    else:
        mkdir_p('/home/hussenot/Bu2025study/Injections/'+name)
        params={}
        for p, val in pardist.items():
            x = np.random.random()
            params[p]= val[0]+x*(val[1]-val[0])
            Injections[N][p] = params[p]
        params['luminosity_distance']=40
        Injections[N]['luminosity_distance']=40
    
    params['luminosity_distance']=40
    filts = ['ps1::g','ps1::r','ps1::i','ps1::z','ps1::y']
    model = FiestaKilonovaModel(model='Bu2025_MLP', surrogate_dir='/home/hussenot/fiestaEM/surrogates', filters=filts)
    mAB = model.generate_lightcurve(sample_times,params)
    ps1 = Table(mAB)
    for f in ps1.keys():
        ps1[f] += 5*np.log10(params['luminosity_distance']*(10**6 /10))
    ps1.write('/home/hussenot/Bu2025study/Injections/'+name+'/'+name+'_ps1.dat',format='ascii.csv',overwrite=True)
    
    filts = ['2massj','2massh','2massks']
    model = FiestaKilonovaModel(model='Bu2025_MLP', surrogate_dir='/home/hussenot/fiestaEM/surrogates', filters=filts)
    mAB = model.generate_lightcurve(sample_times,params)
    mass = Table(mAB)
    for f in mass.keys():
        mass[f] += 5*np.log10(params['luminosity_distance']*(10**6 /10))
    mass.write('/home/hussenot/Bu2025study/Injections/'+name+'/'+name+'_mass.dat',format='ascii.csv',overwrite=True)

Injections.write('/home/hussenot/Bu2025study/Bu25injections.csv', format='ascii.csv', overwrite=True)