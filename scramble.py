#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:26:03 2024

@author: hussenot
"""

import numpy as np
times = np.arange(0.1, 15, 0.1)
from astropy.table import Table
from astropy.time import Time

# ps1 = Table.read('/home/hussenot/H0/kilonovae-H0/170817ps1.dat', format='ascii.csv')
# mass = Table.read('/home/hussenot/H0/kilonovae-H0/170817mass.dat', format='ascii.csv')

name = 'InjectionBaseLightcurve22'
folder = '/home/hussenot/H0/kilonovae-H0/Injection_Recovery_IterationsVariation/'+name+'/'
ps1 = Table.read(folder+name+'_ps1.dat', format='ascii.csv')
mass = Table.read(folder+name+'_mass.dat', format='ascii.csv')
isot = Time(times+60000, format='mjd').isot


table = Table(np.zeros((8*149,4)), names=['isot','filter','mag','err'],dtype=[str,str,float,float])
for i,f in enumerate(ps1.keys()):
    table['isot'][i*149:(i+1)*149] = isot
    table['filter'][i*149:(i+1)*149] = f
    table['mag'][i*149:(i+1)*149] = ps1[f]
    
for i,f in enumerate(mass.keys()):
    table['isot'][(i+5)*149:(i+6)*149] = isot
    table['filter'][(i+5)*149:(i+6)*149] = f
    table['mag'][(i+5)*149:(i+6)*149] = mass[f]
    
table['err']=0.05

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


###Make 20 randomly sampled realisations of observations with 1obs/day/filter average
for z in np.arange(1,21):
    
    outdir = folder+'1perday_'+str(z)
    mkdir_p(outdir)
    
    samples=[]
    for i in range(8):
        N = len(times)
        samples.append(np.sort(np.random.choice(N, size=15, replace=False)+i*N))
    # print(samples)
    tab = table[samples]
    kept = tab[tab['mag']<24]#Removing data at magnitudes >24, unlikely to be reached by most telescopes
    output = outdir+'/'+name+'_1perday.dat'
    kept.write(output,format='ascii.no_header')
    with open(output) as file:
        s=file.read().replace("_", ":" )
    with open(output, 'w') as file:
        file.write(s)
    # mkdir_p(outdir+'/grizyJHK')


# ##Reproduce AT2017gfo's cadence
# f17 = Table.read('/home/hussenot/H0/kilonovae-H0/170817/AT2017gfoMWcorrected.csv', format='ascii.csv')
# t17= Time(f17['time'],format='isot').mjd - 57982.52851851852
# t17 = np.round(t17, decimals=1)

# N=len(times)
# samples=[]
# outdir = folder+'170817like_cadence'
# mkdir_p(outdir)
# for i,f in enumerate(['ps1::g','ps1::r','ps1::i','ps1::z','ps1::y']+mass.keys()):
#     samples += [N*i + int(10*dt)-1 for dt in t17[(f17['filt']==f)*(t17<15)]]
# tab = table[samples]
# kept = tab[tab['mag']<24]#Removing data at magnitudes >24, unlikely to be reached by most telescopes
# output = outdir+'/'+name+'_1perday.dat'
# kept.write(output,format='ascii.no_header',overwrite=True)
# with open(output) as file:
#     s=file.read().replace("_", ":" )
# with open(output, 'w') as file:
#     file.write(s)
# # mkdir_p(outdir+'/grizyJHK')