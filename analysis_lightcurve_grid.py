#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:28:25 2024

@author: hussenot
"""

import numpy as np
import matplotlib.pyplot as plt

###Use make_lightcurve_grid.py first to precompute the lightcurve files for filters grizyJKH

sample_times = np.arange(0.1,15,0.2)
filts = ['ps1__g','ps1__r','ps1__i','ps1__z','ps1__y']
filts = ['2massj','2massh','2massks']
filts = ['2massks']
filts = ['ps1__g','ps1__r','ps1__i','2massks']

# #Precomputing the color differences
# filt1 = '2massks'
# filt2 = 'ps1__i'
# f3 = 'k-i'

# with open('/home/hussenot/H0/kilonovae-H0/SimuLC_grid_'+filt1+'.npy', 'rb') as f:
#     result1 = np.load(f)
# with open('/home/hussenot/H0/kilonovae-H0/SimuLC_grid_'+filt2+'.npy', 'rb') as f:
#     result2 = np.load(f)
# r3 = result1-result2
# with open('/home/hussenot/H0/kilonovae-H0/SimuLC_grid_'+f3+'.npy', 'wb') as f:
#         np.save(f, r3)

filts = ['r-g','i-g','i-r','k-g','k-r','k-i']

ranges = {}
steps = {}

for filt in filts:
    with open('/home/hussenot/H0/kilonovae-H0/SimuLC_grid_'+filt+'.npy', 'rb') as f:
        result = np.load(f)

    Range_phi = np.zeros((11,11,11,75))
    Avg_step_phi = np.zeros((11,11,11,75))
    for i in range(11):
        for j in range(11):
            for k in range(11):
                for t in range(75):
                    dist = result[:,i,j,k,t]
                    Range_phi[i,j,k,t] = np.max(dist)-np.min(dist)
                    Avg_step_phi[i,j,k,t] = np.mean([np.abs(dist[i+1]-dist[i]) for i in range(10)])
    
    Range_dyn = np.zeros((11,11,11,75))
    Avg_step_dyn = np.zeros((11,11,11,75))
    for i in range(11):
        for j in range(11):
            for k in range(11):
                for t in range(75):
                    dist = result[i,:,j,k,t]
                    Range_dyn[i,j,k,t] = np.max(dist)-np.min(dist)
                    Avg_step_dyn[i,j,k,t] = np.mean([np.abs(dist[i+1]-dist[i]) for i in range(10)])
    
    Range_wind = np.zeros((11,11,11,75))
    Avg_step_wind = np.zeros((11,11,11,75))
    for i in range(11):
        for j in range(11):
            for k in range(11):
                for t in range(75):
                    dist = result[i,j,:,k,t]
                    Range_wind[i,j,k,t] = np.max(dist)-np.min(dist)
                    Avg_step_wind[i,j,k,t] = np.mean([np.abs(dist[i+1]-dist[i]) for i in range(10)])
    
    Range_theta = np.zeros((11,11,11,75))
    Avg_step_theta = np.zeros((11,11,11,75))
    for i in range(11):
        for j in range(11):
            for k in range(11):
                for t in range(75):
                    dist = result[i,j,k,:,t]
                    Range_theta[i,j,k,t] = np.max(dist)-np.min(dist)
                    Avg_step_theta[i,j,k,t] = np.mean([np.abs(dist[i+1]-dist[i]) for i in range(10)])

    ranges[filt] = [np.median(Range_phi),np.median(Range_dyn),
                  np.median(Range_wind), np.median(Range_theta)]
    steps[filt] = [np.median(Avg_step_phi),np.median(Avg_step_dyn),
                    np.median(Avg_step_wind),np.median(Avg_step_theta)]
    
# print(np.median(Range_phi), np.median(Avg_step_phi))
# print(np.median(Range_dyn), np.median(Avg_step_dyn))
# print(np.median(Range_wind), np.median(Avg_step_wind))
# print(np.median(Range_theta), np.median(Avg_step_theta))

labels = [r'$\phi$', r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
          r'cos($\iota$)']

# fig, (ax1,ax2) = plt.subplots(1,2,figsize=(18, 10))
# fig.suptitle('Probing the Bulla2019lm model and its gradients', fontsize=24)

fig, ax2 = plt.subplots(1,1,figsize=(9, 9))
# fig.suptitle(r'Average variation for steps of size $10\%$ of the prior interval', fontsize=24)
# for filt in filts:
#     ax1.plot(ranges[filt], linestyle='', marker='o', markersize=20, label=filt)
# ax1.set_ylabel(r'Range of variation [mag] (median across the grid)', fontsize=20)
# ax1.set_xticks([k for k in range(4)],labels=labels)
# ax1.tick_params(axis='x', labelrotation=90, labelsize=20)
for filt in filts:
    ax2.plot(steps[filt], linestyle='', marker='o', markersize=20, label=filt)
ax2.set_xlabel('Steps along the [...] axis', fontsize=20)
ax2.set_ylabel(r"Average size of 10%-of-prior-range steps [mag]", fontsize=20)
ax2.set_xticks([k for k in range(4)],labels=labels)
ax2.set_ylim(0, None)
# ax1.tick_params(axis='x', labelrotation=90, labelsize=20)
# ax1.tick_params(labelsize=20)
ax2.tick_params(labelsize=20)
# ax1.legend(fontsize=16)
ax2.legend(fontsize=16)
fig.savefig('/home/hussenot/H0/plots/10percentsteps_diffs_griK.pdf', format='pdf', bbox_inches='tight')
