#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:28:25 2024

@author: hussenot
"""

import numpy as np
import matplotlib.pyplot as plt
import json

###Use make_lightcurve_grid.py first to precompute the lightcurve files for filters grizyJKH
# period, Nt = '10-28days',18

# filts = ['ps1::g','ps1::r','ps1::i','ps1::z','ps1::y']
filts = ['2massj','2massh','2massks']
filts = ['2massks']
# filts = ['ps1::g','ps1::r','ps1::i','2massks']
# filts = ['r-g','i-g','i-r','k-g','k-r','k-i']

def computestepsBu19(filt, filt2=None):
    Ranges = {}
    AvgSteps = {}
    paramlist = ['KNphi','log10_mej_dyn','log10_mej_wind','cos_iota']
    for p in paramlist:
        Ranges[p]=[]
        AvgSteps[p]=[]
        
    with open('/home/hussenot/H0/kilonovae-H0/SimuLC_grid_'+filt+'.npy', 'rb') as f:
        result = np.load(f)
    if filt2!=None:
        with open('/home/hussenot/H0/kilonovae-H0/SimuLC_grid_'+filt2+'.npy', 'rb') as f:
            result2 = np.load(f)
        result = result-result2
        

    for t in range(75):
        for i in range(11):
            for j in range(11):
                for k in range(11):
                    
                    dist = result[:,i,j,k,t]
                    Ranges['KNphi'].append(np.max(dist)-np.min(dist))
                    AvgSteps['KNphi'].append(np.mean([np.abs(dist[i+1]-dist[i]) for i in range(10)]))
                    dist = result[i,:,j,k,t]
                    Ranges['log10_mej_dyn'].append(np.max(dist)-np.min(dist))
                    AvgSteps['log10_mej_dyn'].append(np.mean([np.abs(dist[i+1]-dist[i]) for i in range(10)]))
                    dist = result[i,j,:,k,t]
                    Ranges['log10_mej_wind'].append(np.max(dist)-np.min(dist))
                    AvgSteps['log10_mej_wind'].append(np.mean([np.abs(dist[i+1]-dist[i]) for i in range(10)]))
                    dist = result[i,j,k,:,t]
                    Ranges['cos_iota'].append(np.max(dist)-np.min(dist))
                    AvgSteps['cos_iota'].append(np.mean([np.abs(dist[i+1]-dist[i]) for i in range(10)]))
                    
    medianRanges = {}
    medianAvgSteps = {}
    meanRanges = {}
    meanAvgSteps = {}
    for p in paramlist:
        medianRanges[p]=[]
        medianAvgSteps[p]=[]
        for t in range(75):
            medianRanges[p].append(np.median(Ranges[p][t*1331:(t+1)*1331]))
            medianAvgSteps[p].append(np.median(AvgSteps[p][t*1331:(t+1)*1331]))
        medianRanges[p].append(np.median(Ranges[p]))
        medianAvgSteps[p].append(np.median(AvgSteps[p]))
        
        meanRanges[p]=[]
        meanAvgSteps[p]=[]
        for t in range(75):
            meanRanges[p].append(np.mean(Ranges[p][t*1331:(t+1)*1331]))
            meanAvgSteps[p].append(np.mean(AvgSteps[p][t*1331:(t+1)*1331]))
            
    if filt2==None:
        with open('/home/hussenot/H0/10percentsteps/meanRanges'+filt+'.json','w') as f:
            json.dump(meanRanges, f)
        with open('/home/hussenot/H0/10percentsteps/meanSteps'+filt+'.json','w') as f:
            json.dump(meanAvgSteps, f)
        with open('/home/hussenot/H0/10percentsteps/medianRanges'+filt+'.json','w') as f:
            json.dump(medianRanges, f)
        with open('/home/hussenot/H0/10percentsteps/medianSteps'+filt+'.json','w') as f:
            json.dump(medianAvgSteps, f)
    
    else:
        with open('/home/hussenot/H0/10percentsteps/meanRanges'+filt+'-'+filt2+'.json','w') as f:
            json.dump(meanRanges, f)
        with open('/home/hussenot/H0/10percentsteps/meanSteps'+filt+'-'+filt2+'.json','w') as f:
            json.dump(meanAvgSteps, f)
        with open('/home/hussenot/H0/10percentsteps/medianRanges'+filt+'-'+filt2+'.json','w') as f:
            json.dump(medianRanges, f)
        with open('/home/hussenot/H0/10percentsteps/medianSteps'+filt+'-'+filt2+'.json','w') as f:
            json.dump(medianAvgSteps, f)
                                
    return [np.median(AvgSteps[p]) for p in paramlist]
    

def compute20stepsBu19(filt, filt2=None):
    AvgSteps = {}
    paramlist = ['KNphi','log10_mej_dyn','log10_mej_wind','cos_iota']
    for p in paramlist:
        AvgSteps[p]=[]
        
    with open('/home/hussenot/H0/kilonovae-H0/SimuLC_grid_'+filt+'.npy', 'rb') as f:
        result = np.load(f)
    if filt2!=None:
        with open('/home/hussenot/H0/kilonovae-H0/SimuLC_grid_'+filt2+'.npy', 'rb') as f:
            result2 = np.load(f)
        result = result-result2
        

    for t in range(75):
        for i in range(11):
            for j in range(11):
                for k in range(11):
                    
                    dist = result[:,i,j,k,t]
                    AvgSteps['KNphi'].append(np.mean([np.abs(dist[i+2]-dist[i]) for i in range(9)]))
                    dist = result[i,:,j,k,t]
                    AvgSteps['log10_mej_dyn'].append(np.mean([np.abs(dist[i+2]-dist[i]) for i in range(9)]))
                    dist = result[i,j,:,k,t]
                    AvgSteps['log10_mej_wind'].append(np.mean([np.abs(dist[i+2]-dist[i]) for i in range(9)]))
                    dist = result[i,j,k,:,t]
                    AvgSteps['cos_iota'].append(np.mean([np.abs(dist[i+2]-dist[i]) for i in range(9)]))
                    
    medianAvgSteps = {}
    meanAvgSteps = {}
    for p in paramlist:
        medianAvgSteps[p]=[]
        for t in range(75):
            medianAvgSteps[p].append(np.median(AvgSteps[p][t*1331:(t+1)*1331]))
        medianAvgSteps[p].append(np.median(AvgSteps[p]))
        
        meanAvgSteps[p]=[]
        for t in range(75):
            meanAvgSteps[p].append(np.mean(AvgSteps[p][t*1331:(t+1)*1331]))
            
    if filt2==None:
        with open('/home/hussenot/H0/20percentsteps/meanSteps'+filt+'.json','w') as f:
            json.dump(meanAvgSteps, f)
        with open('/home/hussenot/H0/20percentsteps/medianSteps'+filt+'.json','w') as f:
            json.dump(medianAvgSteps, f)
    
    else:
        with open('/home/hussenot/H0/20percentsteps/meanSteps'+filt+'-'+filt2+'.json','w') as f:
            json.dump(meanAvgSteps, f)
        with open('/home/hussenot/H0/20percentsteps/medianSteps'+filt+'-'+filt2+'.json','w') as f:
            json.dump(medianAvgSteps, f)
                                
    return [np.median(AvgSteps[p]) for p in paramlist]



labels = [r'$\phi$', r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
          r'cos($\iota$)']
paramlist = ['KNphi','log10_mej_dyn','log10_mej_wind','cos_iota']


fig, ax = plt.subplots(1,1,figsize=(9, 8))
fig.suptitle(r'Magnitude variation for $20\%$-of-prior-interval steps', fontsize=24)
labfilts = [r'$g$', r'$r$', r'$i$', r'$z$', r'$y$', r'$J$', r'$H$', r'$K$']
for i,filt in enumerate(['ps1__g','ps1__r','ps1__i','ps1__z','ps1__y','2massj','2massh','2massks']):
    # ranges = json.load(open('/home/hussenot/H0/20percentsteps/medianRanges'+filt+'.json','r'))
    steps = json.load(open('/home/hussenot/H0/20percentsteps/medianSteps'+filt+'.json','r'))
    # ax.plot([ranges[p][-1] for p in paramlist], linestyle='', marker='o', markersize=20, label=labfilts[i])
    ax.plot([steps[p][-1] for p in paramlist], linestyle='', marker='o', markersize=16, label=labfilts[i])
ax.set_ylabel(r'Range of variation [mag]', fontsize=20)
ax.set_ylabel(r'Median size of variation [mag]', fontsize=24)
ax.set_xticks([k for k in range(4)],labels=labels)
ax.tick_params(axis='x', labelrotation=0, labelsize=20)
ax.set_ylim(0, None)
ax.set_xlabel('Steps along the [...] axis', fontsize=24)
ax.tick_params(labelsize=20)
ax.legend(fontsize=22)
fig.savefig('/home/hussenot/H0/20percentsteps/20percentstepsBu19_grizyJHK.pdf', format='pdf', bbox_inches='tight')
