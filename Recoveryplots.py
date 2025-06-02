#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:13:05 2024

@author: hussenot
"""

import numpy as np
import glob
import pandas as pd
import matplotlib.pyplot as plt
import json
from astropy.table import Table

# dirs = [] + glob.glob('/home/hussenot/H0/kilonovae-H0/lcsimu/*perday')
# dirs = [d+'/grizyJHK' for d in dirs]
supdir = '/home/hussenot/H0/kilonovae-H0/lcsimu/'
dirs = []
title='Recovery of the 170817 Bu2019lm bestfit curve with grizJHK filters'
label = 'Simu2019lm'

#Cadences
dirs.append(supdir+'10perday/grizJHK')
dirs.append(supdir+'2perday/grizJHK')
dirs.append(supdir+'cadence170817/grizyJHK')
dirs.append(supdir+'1perday1/grizJHK')
dirs.append(supdir+'05perday/grizJHK')
dirs.append(supdir+'033perday/grizJHK')
dirs.append(supdir+'02perday/grizJHK')
labels=['10 per day', '2 per day', '1 per day', '1 per 2 days', '1 per 3 days', '1 per 5 days']
labels=['10 per day', '2 per day', '170817like','1 per day', '1 per 2 days', '1 per 3 days', '1 per 5 days']
lbly='Average frequency of observations in each band'

# # Times
# # dirs.append(supdir+'10perday/grizJHK')
# dirs.append(supdir+'2perday/grizJHK')
# dirs.append(supdir+'2perday0-2/grizJHK')
# dirs.append(supdir+'2perday1-4/grizJHK')
# dirs.append(supdir+'2perday4-15/grizJHK')
# labels=['[0-15] days', '[0-2] days', '[1-4] days', '[4-15] days']
# lbly='Time range of observations in each band'
# title='Recovery of the 170817 Bu2019lm bestfit curve with grizJHK filters, avg 2 obs/day'



# #Variation
# dirs.append(supdir+'10perday/grizJHK')
# dirs.append(supdir+'1perday1/grizJHK')
# dirs.append(supdir+'1perday2/grizJHK')
# dirs.append(supdir+'1perday3/grizJHK')
# dirs.append(supdir+'1perday4/grizJHK')
# dirs.append(supdir+'1perday5/grizJHK')
# dirs.append(supdir+'1perday6/grizJHK')
# dirs.append(supdir+'1perday7/grizJHK')
# dirs.append(supdir+'1perday8/grizJHK')
# labels=['Best-case (10 per day)', '1 per day, iteration 1','1 per day, iteration 2',
#         '1 per day, iteration 3','1 per day, iteration 4','1 per day, iteration 5',
#         '1 per day, iteration 6','1 per day, iteration 7','1 per day, iteration 8',]


# # Allthe1perday
# dirs=[]
# labels=[]
# for i in range(1,51):
#     dirs.append(supdir+'1perday'+str(i)+'/grizJHK')
#     labels.append(str(i))
# lbly='Iteration number'
# title = 'Recovery of the 170817 Bu2019lm bestfit curve with grizJHK filters'


# params = ['KNphi', 'log10_mej_dyn', 'log10_mej_wind', 'inclination_EM','luminosity_distance']
# labels = [r'$\phi$', r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
#           r'$\iota [rad]',r'$D_L$']
par,lpar,val = 'luminosity_distance','Distance (Mpc)',41.168672037183725
# par,lpar,val = 'KNphi',r'$\phi$ (degrees)',31.033359307564652
# par,lpar,val = 'log10_mej_dyn',r'$\log_{10}M_{ej}^{dyn}$',-2.236983615436653
# par,lpar,val = 'log10_mej_wind',r'$\log_{10}M_{ej}^{wind}$',-0.9959807211519678
# par,lpar,val = 'inclination_EM',r'Inclination $\iota$ [rad]',1.2727477446277973

# par,lpar,val = 'log10_mej_dyn',r'$\log_{10}M_{ej}^{dyn}$',-2.2#previousSim2019lm

# supdir = '/home/hussenot/H0/kilonovae-H0/Simu2019lm/'
# dirs = []

# # Filters
# supdir = '/home/hussenot/H0/kilonovae-H0/lcsimu/cadence170817/'
# dirs.append(supdir+'grizyJHK')
# # dirs.append(supdir+'grizyJH')
# # dirs.append(supdir+'grizyJ')
# # dirs.append(supdir+'grizy')
# # dirs.append(supdir+'griz')
# # dirs.append(supdir+'gri')
# dirs.append(supdir+'gr')
# # dirs.append(supdir+'g')
# # dirs.append(supdir+'g')
# dirs.append(supdir+'r')
# # dirs.append(supdir+'i')
# # dirs.append(supdir+'z')
# # dirs.append(supdir+'y')
# # dirs.append(supdir+'J')
# # dirs.append(supdir+'H')
# # dirs.append(supdir+'K')
# # dirs.append(supdir+'rizyJHK')
# # dirs.append(supdir+'all_but_r')
# # dirs.append(supdir+'all_but_i')
# # dirs.append(supdir+'all_but_z')
# # dirs.append(supdir+'all_but_y')
# # dirs.append(supdir+'all_but_J')
# # dirs.append(supdir+'all_but_H')
# # dirs.append(supdir+'grizyJH')
# # dirs.append(supdir+'grizyJHK')
# # dirs.append(supdir+'rizyJHK')
# # dirs.append(supdir+'izyJHK')
# # dirs.append(supdir+'zyJHK')
# # dirs.append(supdir+'yJHK')
# # dirs.append(supdir+'JHK')
# # dirs.append(supdir+'HK')
# # dirs.append(supdir+'K')
# dirs.append(supdir+'rK')
# # labels=['grizyJHK', 'grizyJH', 'grizyJ', 'grizy', 'griz', 'gri', 'gr', 'g']
# labels=['g', 'r', 'i', 'z', 'y', 'J', 'H', 'K']
# # labels=['all but '+k for k in ['g', 'r', 'i', 'z', 'y', 'J', 'H', 'K']]
# # labels=['grizyJHK', 'rizyJHK', 'izyJHK', 'zyJHK', 'yJHK', 'JHK', 'HK', 'K']
# labels = ['all', 'gr', 'r','rK']
# lbly='Filters used'
# title = 'Recovery of the 170817 Bu2019lm bestfit curve, true 170817 cadence'

# supdir = '/home/hussenot/H0/kilonovae-H0/170817/Bu2019full_MWcorrected/1errtightangle_'
# label = 'AT170817'
# dirs.append(supdir+'all')
# dirs.append(supdir+'grizy')
# dirs.append(supdir+'griz')
# dirs.append(supdir+'ri')
# labels=['grizyJHK', 'grizy', 'griz', 'ri']
# lbly='Filters used'
# title = r'Analysis of AT2017gfo MW-corrected lightcurve, $\sigma_{\rm sys} = 1$ mag'


# #Sigmasys variations
# supdir = '/home/hussenot/H0/kilonovae-H0/lcsimu/varying_sigma_sys_truecadence_0.5noise/'
# dirs.append(supdir+'0grizyJHK')
# dirs.append(supdir+'0.05grizyJHK')
# dirs.append(supdir+'0.1grizyJHK')
# dirs.append(supdir+'0.2grizyJHK')
# dirs.append(supdir+'0.4grizyJHK')
# dirs.append(supdir+'0.8grizyJHK')
# dirs.append(supdir+'1grizyJHK')
# dirs.append(supdir+'1.5grizyJHK')
# dirs.append(supdir+'2grizyJHK')
# labels=['0','0.05', '0.1', '0.2', '0.4','0.8','1','1.5','2']
# lbly=r'$\sigma_{sys}$ [mag]'
# title='Recovery of the 170817 Bu2019lm bestfit grizyJHK curve, error 0.5 margin 0.3 mag'


# N = '1'
# supdir = '/home/hussenot/H0/kilonovae-H0/Injection_Recovery_IterationsVariation/InjectionBaseLightcurve'+N+'/'
# title='Recovery of simulated Bu2019lm curve (Lightcurve '+N+') with grizJHK filters'
# label = 'InjectionRecoveryIterations'
# dirs = []

# # Allthe1perday
# dirs=[]
# labels=[]
# for i in range(1,51):
#     dirs.append(supdir+'1perday_'+str(i)+'/grizy05JHK')
#     labels.append('i '+str(i))
# lbly='Iteration numbers'

# par,lpar,val = 'luminosity_distance','Distance (Mpc)',40
# par,lpar,val = 'KNphi',r'$\phi$ (degrees)',60
# par,lpar,val = 'log10_mej_dyn',r'$\log_{10}M_{ej}^{dyn}$',np.log10(0.01)
# par,lpar,val = 'log10_mej_wind',r'$\log_{10}M_{ej}^{wind}$',np.log10(0.05)
# par,lpar,val = 'inclination_EM',r'Inclination $\iota$ [rad]',np.arccos(0.8)


###################
#Generating the plots

sample = []
mean = []
median = []
std = []
best = []
sig = []
perc = []
KL = []
chi2 = []
logL = []
combine = []
# val = np.log(val)
for d in dirs:
    s=pd.read_csv(d+'/outdirBNSBu32cores/'+label+'_posterior_samples.dat', header=0, delimiter=" ")
    sp = s[par]
    combine += [sp[k] for k in range(len(sp))]
    # sp = np.log(sp)
    sample.append(sp)
    median.append(np.median(sp))
    mean.append(np.mean(sp))
    std.append(np.std(sp))
    b=json.load(open(d+'/outdirBNSBu32cores/'+label+'_bestfit_params.json','r'))
    best.append(b[par])
    bayes = b['log_bayes_factor']
    KL.append( np.mean(s['log_likelihood']) - bayes)
    logL.append(b['log_likelihood'])
    chi2.append(b['chi2_per_dof'])
    sig.append( (val-np.mean(sp))/np.std(sp))
    perc.append(np.mean(sp<val)*100)


#Violin plots of the posterior distributions
quant = [0.5]
quant = [0.16,0.5,0.84]
# quant = [0.05,0.5,0.95]

fig, ax = plt.subplots(1,1, figsize = (9,9)) #12,12 for overleaf KL plots. 9,9 for pdf
# #Trying the triple axis version
# from mpl_toolkits.axisartist.parasite_axes import HostAxes

# fig = plt.figure(figsize = (8,7))
# # ax.set_axis_off()
# ax = fig.add_axes([0.15, 0.1, 0.65, 0.8], axes_class=HostAxes)
# par1 = ax.get_aux_axes(viewlim_mode=None, sharex=ax)
# par2 = ax.get_aux_axes(viewlim_mode=None, sharex=ax)

# ax.axis["right"].set_visible(False)

# par1.axis["right"].set_visible(True)
# par1.axis["right"].major_ticklabels.set_visible(True)
# par1.axis["right"].label.set_visible(True)

# par2.axis["right2"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

#Plotting posterior distributions
ax.axvline(val, label='Injected value: mock17', color='black')
# ax.boxplot(sample, vert=False, showfliers=False, labels=labels)
ax.violinplot(sample, vert=False, showextrema=False, quantiles=[quant for s in sample])#, side='low')
ax.plot(best, np.arange(len(dirs))+1, linestyle='', marker='o', label='bestfit estimate')
# ax.plot(best, np.arange(len(dirs))+1, linestyle='', marker='o', label='bestfit err=0mag', color='blue')

# #Code to visualise the combined distribution of all posteriors 
# #(they are assumed to all have a similar number of samples so we ignore reweighting by 1/Nsamples)
# parts = ax.violinplot(combine, vert=False, showextrema=False, quantiles=quant, positions = [len(sample)+2], widths = 2)
# parts['bodies'][0].set_facecolor('blue')
# labels.append('')
# labels.append('Combined')

#Labeling axes and ticks
# # For the repeated iterations:
# ax.set_ylim(-2, None)

ax.set_yticks(np.arange(1, len(labels)+1), labels=labels, fontsize=14)
# ax.yaxis.set_tick_params(labelleft=False)
plt.xticks(fontsize=16)
ax.invert_yaxis()
ax.set_xlabel(lpar, fontsize = 20)
ax.set_ylabel(lbly,fontsize = 20)
# ax.set_title(title, fontsize=20)

# ax.set_ylabel('Filters used',fontsize = 16)
# ax.set_title('Recovery of a Bu2019lm simulated curve, avg cadence 2/day', fontsize=16)
ax.legend(fontsize=16)

# #Adding the KL-divergence on the right-side
# KL=np.round(KL,decimals=2)
# ax2 = ax.twinx()
# ax2.set_yticks(np.arange(1, len(KL)+1), labels=KL, fontsize=14)
# ax2.set_ylim(ax.get_ylim())
# ax2.set_ylabel('KL Divergence Posterior||Prior', fontsize=20)

#Adding the logL and chi2/dof on the right-side
logL=np.round(logL,decimals=2)
chi2=np.round(chi2,decimals=2)
logL=[str(i) for i in logL]
chi2=[str(i) for i in chi2]

# ax2 = ax.twinx()
# # ax2.set_yticks(np.arange(1, len(KL)+1), labels=logL, fontsize=14)
# # ax2.set_ylim(ax.get_ylim())
# # ax2.set_ylabel(r'Best Log-likelihood', fontsize=20)
# ax3 = ax.twinx()
# ax3.axis["right"] = ax3.new_fixed_axis(loc="right", offset=(60, 0))
# ax3.set_yticks(np.arange(1, len(KL)+1), labels=chi2, fontsize=14)
# ax3.set_ylim(ax.get_ylim())
# ax3.set_ylabel(r'$\chi^2 /dof$', fontsize=20)

# # par1.set(ylim=ax.get_ylim(), ylabel=r'Best Log-likelihood')
# par1.set_yticks(np.arange(1, len(KL)+1), labels=chi2, fontsize=14)
# par1.set_ylim(ax.get_ylim())
# par1.set_ylabel(r'$\chi^2 /dof$', fontsize=20)
# par2.set_yticks(np.arange(1, len(KL)+1), labels=logL, fontsize=14)
# par2.set_ylim(ax.get_ylim())
# par2.set_ylabel(r'Best Log-likelihood', fontsize=30)

# print('two')
# ax.axis["bottom"].label.set(fontsize=20)
# ax.axis["left"].label.set(fontsize=16)
# par1.axis["right"].label.set(fontsize=16)
# par2.axis["right2"].label.set(fontsize=16)
# # plt.show()


# fig.savefig('/home/hussenot/H0/plots/KLCadenceDist.pdf', format='pdf', bbox_inches='tight')

# ax.set_xlim(0,100)


# print(np.std(median[:21]),np.std(median))
# print(np.median(median), np.median(std))

# ##Adding the syserr=0.5mag
# dirs=[]
# labels=[]
# for i in range(1,21):
#     # dirs.append(supdir+'1perday_'+str(i)+'/grizy05JHK')
#     dirs.append(supdir+'1perday_'+str(i)+'/grizy00JHK')
#     labels.append('i '+str(i))
# lbly='Iteration numbers'

# sample = []
# mean = []
# median = []
# std = []
# best = []
# sig = []
# perc = []
# KL = []
# combine = []
# # val = np.log(val)
# for d in dirs:
#     s=pd.read_csv(d+'/outdirBNSBu32cores/'+label+'_posterior_samples.dat', header=0, delimiter=" ")
#     sp = s[par]
#     combine += [sp[k] for k in range(len(sp))]
#     # sp = np.log(sp)
#     sample.append(sp)
#     median.append(np.median(sp))
#     mean.append(np.mean(sp))
#     std.append(np.std(sp))
#     b=json.load(open(d+'/outdirBNSBu32cores/'+label+'_bestfit_params.json','r'))
#     best.append(b[par])
#     bayes = b['log_bayes_factor']
#     KL.append( np.mean(s['log_likelihood']) - bayes)
#     sig.append( (val-np.mean(sp))/np.std(sp))
#     perc.append(np.mean(sp<val)*100)

# parts=ax.violinplot(sample, vert=False, showextrema=False, quantiles=[quant for s in sample])#, side='low')
# for pc in parts['bodies']:
#     pc.set_facecolor('red')
# # ax.plot(best, np.arange(len(dirs))+1, linestyle='', marker='o', label='bestfit err=0.5mag', color='red')
# ax.plot(best, np.arange(len(dirs))+1, linestyle='', marker='o', label='bestfit err=0mag', color='red')
# parts = ax.violinplot(combine, vert=False, showextrema=False, quantiles=quant, positions = [len(sample)+2], widths = 2)
# parts['bodies'][0].set_facecolor('red')
# ax.legend(fontsize=16)


# fig, ax = plt.subplots(1,1, figsize = (8,4))
# # ax.set_xlabel('Iterations')
# # ax.set_title('Cumulative distribution', fontsize=16)
# # # ax.set_ylabel('Percentile of bestfit against posterior in '+lpar,fontsize = 16)
# # # ax.plot(np.sort(perc))
# # ax.set_ylabel(r'Number of $\sigma$ away the true'+lpar +' is from posterior',fontsize = 16)
# # ax.plot(np.sort(sig))
# ax.set_xlabel(lpar+r': Truth - Posterior mean ($\sigma$)', fontsize=18)
# ax.hist(sig)
