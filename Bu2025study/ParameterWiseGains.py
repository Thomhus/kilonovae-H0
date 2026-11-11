#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:47:13 2026

@author: hussenot
"""

import numpy as np
import pandas as pd
import json

paramlist = ['log10_mej_dyn','log10_mej_wind','KNphi','cos_iota','luminosity_distance']
lablist = [r'$\log_{10}M_{ej}^{dyn}$', r'$\log_{10}M_{ej}^{wind}$',
            r'$\phi$',r'$\cos(\iota)$', 'Distance']

# paramlist = ['log10_mej_dyn','v_ej_dyn','Ye_dyn','log10_mej_wind','v_ej_wind','Ye_wind','inclination_EM','luminosity_distance']
# lablist = [r'$\log_{10}M_{ej}^{dyn}$', r'$v_{ej}^{dyn}$', r'$Y_e^{dyn}$', r'$\log_{10}M_{ej}^{wind}$',
#             r'$v_{ej}^{wind}$', r'$Y_e^{wind}$', 'Inclination', 'Distance']

outdirKN = '/home/hussenot/H0/kilonovae-H0/170817/'

direc = outdirKN+'Errsys+constraints/06Allfree/'
# direc = outdirKN+'Errsys+constraints/Allfree/'


KN = pd.read_csv(direc+'outdirBNSBu32cores/Constraints170817_posterior_samples.dat', header=0, delimiter=" ")
KN['cos_iota'] = np.cos(KN['inclination_EM'])
bf = json.load(open(direc+'outdirBNSBu32cores/Constraints170817_bestfit_params.json','r'))

def Bu19defaultprior(inc,dist):
    logprior = -np.log(75-15) -np.log(-1+3) -np.log(-0.5+3)
    logprior+= np.log(np.sin(inc)/2) - np.log(dist*np.log(500))
    return logprior

# print(KN['log_prior'][0], Bu19defaultprior(KN['inclination_EM'][0], KN['luminosity_distance'][0]))

# direc = outdirKN+'Bu2025MLP/1Default/'
# direc = outdirKN+'Bu2025MLP/06Default/'

# KN = pd.read_csv(direc+'outdirBNSBu7cores/AT2017gfoBu2025_posterior_samples.dat', header=0, delimiter=" ")

# # print(np.min(KN['log_prior']),np.max(KN['log_prior']))

# def Bu25defaultprior(dist):
#     logprior = -np.log(-1.3010299956639813+3) -np.log(0.28-0.12) -np.log(0.35-0.15) 
#     logprior+= -np.log(-0.8860566476931633+2) -np.log(0.15-0.05) - np.log(0.4-0.2) -np.log(np.pi/2-0)
#     logprior+= - np.log(dist*np.log(500))
#     return logprior

# # print(KN['log_prior'][0]-Bu25defaultprior(KN['luminosity_distance'][0]))
# # print(KN['log_prior'][1]-Bu25defaultprior(KN['luminosity_distance'][1]))


# direc = outdirKN+'Bu2026MLP/06Default/'

# KN = pd.read_csv(direc+'outdirBNSBu7cores/AT2017gfoBu2026_posterior_samples.dat', header=0, delimiter=" ")

# # print(np.min(KN['log_prior']),np.max(KN['log_prior']))

# def Bu26defaultprior(dist):
#     logprior = -np.log(-1.3010299956639813+4) -np.log(0.35-0.12) -np.log(0.35-0.15) 
#     logprior+= -np.log(-0.5502131530142267+4) -np.log(0.15-0.05) - np.log(0.4-0.2) -np.log(np.pi/2-0)
#     logprior+= - np.log(dist*np.log(500))
#     return logprior

# # print(KN['log_prior'][0]-Bu26defaultprior(KN['luminosity_distance'][0]))
# # print(KN['log_prior'][1]-Bu26defaultprior(KN['luminosity_distance'][1]))


########################

def marginalweights(samples,Nbins=50):
    w,b = np.histogram(samples,bins=Nbins)
    return w/len(samples),b

def marginaldensity(x,weights,bins):
    i = min(np.sum(x>=bins)-1,len(bins)-2)
    i = max(i,0)
    return weights[i]/(bins[i+1]-bins[i])

# ###Checks: works as intended
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(1,1, figsize = (13,13))
# ax.hist(KN['luminosity_distance'],bins=20, density=True)
# # print(np.histogram(KN['luminosity_distance'],bins=10))

# weights,bins = marginalweights(KN['luminosity_distance'],Nbins=20)
# xs = np.linspace(bins[0], bins[-1],1000)
# ax.plot(xs, [marginaldensity(x, weights, bins) for x in xs], color='black')
# weights,bins = marginalweights(np.log(KN['luminosity_distance']),Nbins=20)
# bins = np.exp(bins)
# xs = np.linspace(bins[0], bins[-1],1000)
# ax.plot(xs, [marginaldensity(x, weights, bins) for x in xs], color='red')

# for N in [5,10,20,30,50,70,100,150,200,400,700,1000]:
#     weights,bins = marginalweights(np.log(KN['luminosity_distance']),Nbins=N)
#     bins = np.exp(bins)
#     distanceKL = np.mean([np.log(marginaldensity(x, weights, bins))+np.log(x*np.log(500)) for x in KN['luminosity_distance']])
#     print("Nbins:",N,"; distance-only KL:",distanceKL)

def decomposeBu19gains(KN,bf,N=50):
    KL = np.mean(KN['log_likelihood']) - bf['log_bayes_factor']
    # print("K-L divergence: ",KL)
    weights,bins = marginalweights(np.log(KN['luminosity_distance']),Nbins=N)
    bins = np.exp(bins)
    distanceKL = np.mean([np.log(marginaldensity(x, weights, bins))+np.log(x*np.log(500)) for x in KN['luminosity_distance']])
    # print("Nbins:",N,"; distance-only KL:",distanceKL)
    weights,bins = marginalweights(KN['KNphi'],Nbins=N)
    phiKL = np.mean([np.log(marginaldensity(x, weights, bins))+np.log(75-15) for x in KN['KNphi']])
    # print("Nbins:",N,"; KNphi-only KL:",phiKL)
    weights,bins = marginalweights(KN['log10_mej_dyn'],Nbins=N)
    MdynKL = np.mean([np.log(marginaldensity(x, weights, bins))+np.log(-1+3) for x in KN['log10_mej_dyn']])
    # print("Nbins:",N,"; log10_mej_dyn-only KL:",MdynKL)
    weights,bins = marginalweights(KN['log10_mej_wind'],Nbins=N)
    MwindKL = np.mean([np.log(marginaldensity(x, weights, bins))+np.log(-0.5+3) for x in KN['log10_mej_wind']])
    # print("Nbins:",N,"; log10_mej_wind-only KL:",MwindKL)
    weights,bins = marginalweights(KN['cos_iota'],Nbins=N)
    bins = np.arccos(bins)[::-1]
    weights = weights[::-1]
    incKL = np.mean([np.log(marginaldensity(x, weights, bins))-np.log(np.sin(x)/2) for x in KN['inclination_EM']])
    # print("Nbins:",N,"; inclination-only KL:",incKL)
    # print("Mutual Information:",KL-distanceKL-phiKL-MdynKL-MwindKL-incKL)
    return KL,MdynKL,MwindKL,phiKL,incKL,distanceKL,KL-distanceKL-MdynKL-MwindKL-phiKL-incKL

def decomposeBu25gains(KN,bf,N=50):
    KL = np.mean(KN['log_likelihood']) - bf['log_bayes_factor']
    # print("K-L divergence: ",KL)
    weights,bins = marginalweights(np.log(KN['luminosity_distance']),Nbins=N)
    bins = np.exp(bins)
    distanceKL = np.mean([np.log(marginaldensity(x, weights, bins))+np.log(x*np.log(500)) for x in KN['luminosity_distance']])
    # print("Nbins:",N,"; distance-only KL:",distanceKL)
    weights,bins = marginalweights(KN['log10_mej_dyn'],Nbins=N)
    MdynKL = np.mean([np.log(marginaldensity(x, weights, bins))+np.log(-1.3010299956639813+3) for x in KN['log10_mej_dyn']])
    # print("Nbins:",N,"; log10_mej_dyn-only KL:",MdynKL)
    weights,bins = marginalweights(KN['v_ej_dyn'],Nbins=N)
    vdynKL = np.mean([np.log(marginaldensity(x, weights, bins))+np.log(0.28-0.12) for x in KN['v_ej_dyn']])
    # print("Nbins:",N,"; v_ej_dyn-only KL:",vdynKL)
    weights,bins = marginalweights(KN['Ye_dyn'],Nbins=N)
    YedynKL = np.mean([np.log(marginaldensity(x, weights, bins))+np.log(0.35-0.15) for x in KN['Ye_dyn']])
    # print("Nbins:",N,"; Ye_dyn-only KL:",YedynKL)
    weights,bins = marginalweights(KN['log10_mej_wind'],Nbins=N)
    MwindKL = np.mean([np.log(marginaldensity(x, weights, bins))+np.log(-0.8860566476931633+2) for x in KN['log10_mej_wind']])
    # print("Nbins:",N,"; log10_mej_wind-only KL:",MwindKL)
    weights,bins = marginalweights(KN['v_ej_wind'],Nbins=N)
    vwindKL = np.mean([np.log(marginaldensity(x, weights, bins))+np.log(0.15-0.05) for x in KN['v_ej_wind']])
    # print("Nbins:",N,"; v_ej_wind-only KL:",vwindKL)
    weights,bins = marginalweights(KN['Ye_wind'],Nbins=N)
    YewindKL = np.mean([np.log(marginaldensity(x, weights, bins))+np.log(0.4-0.2) for x in KN['Ye_wind']])
    # print("Nbins:",N,"; Ye_wind-only KL:",YewindKL)
    weights,bins = marginalweights(KN['inclination_EM'],Nbins=N)
    incKL = np.mean([np.log(marginaldensity(x, weights, bins))+np.log(np.pi/2-0) for x in KN['inclination_EM']])
    # print("Nbins:",N,"; inclination-only KL:",incKL)
    # print("Mutual Information:",KL-distanceKL-MdynKL-vdynKL-YedynKL-MwindKL-vwindKL-YewindKL-incKL)
    return KL,MdynKL,vdynKL,YedynKL,MwindKL,vwindKL,YewindKL,incKL,distanceKL,KL-distanceKL-MdynKL-vdynKL-YedynKL-MwindKL-vwindKL-YewindKL-incKL


#################Application to cadence thresholds

# supdir = '/home/hussenot/H0/kilonovae-H0/lcsimu/'
# direc=supdir+'10perday/grizJHK/'
# direc=supdir+'2perday/grizJHK/'
# direc=supdir+'1perday1/grizJHK/'
# direc=supdir+'05perday/grizJHK/'
# direc=supdir+'033perday/grizJHK/'
# direc=supdir+'02perday/grizJHK/'

# KN = pd.read_csv(direc+'outdirBNSBu32cores/Simu2019lm_posterior_samples.dat', header=0, delimiter=" ")
# KN['cos_iota'] = np.cos(KN['inclination_EM'])
# bf = json.load(open(direc+'outdirBNSBu32cores/Simu2019lm_bestfit_params.json','r'))
# decomposeBu19gains(KN, bf, N=10)

supdir = '/home/hussenot/Bu2025study/Injections/Bu25Injection5/'
direc=supdir+'5perday_1/1errRun7cores/'
direc=supdir+'3perday_1/1errRun7cores/'
direc=supdir+'2perday_1/1errRun7cores/'
direc=supdir+'1perday_1/1errRun7cores/'
direc=supdir+'1per2days_1/1errRun7cores/'
direc=supdir+'1per3days_1/1errRun7cores/'
direc=supdir+'1per5days_1/1errRun7cores/'
# direc=supdir+'5perday_1/05errRun7cores/'
# direc=supdir+'3perday_1/05errRun7cores/'
# direc=supdir+'2perday_1/05errRun7cores/'
# direc=supdir+'1perday_1/05errRun7cores/'
# direc=supdir+'1per2days_1/05errRun7cores/'
# direc=supdir+'1per3days_1/05errRun7cores/'
# direc=supdir+'1per5days_1/05errRun7cores/'
# direc=supdir+'5perday_1/03errRun7cores/'
# direc=supdir+'3perday_1/03errRun7cores/'
# direc=supdir+'2perday_1/03errRun7cores/'
# direc=supdir+'1perday_1/03errRun7cores/'
# direc=supdir+'1per2days_1/03errRun7cores/'
# direc=supdir+'1per3days_1/03errRun7cores/'
# direc=supdir+'1per5days_1/03errRun7cores/'
# direc=supdir+'5perday_1/02errRun7cores/'
# direc=supdir+'3perday_1/02errRun7cores/'
# direc=supdir+'2perday_1/02errRun7cores/'
# direc=supdir+'1perday_1/02errRun7cores/'
# direc=supdir+'1per2days_1/02errRun7cores/'
# direc=supdir+'1per3days_1/02errRun7cores/'
# direc=supdir+'1per5days_1/02errRun7cores/'
# direc=supdir+'5perday_1/01errRun7cores/'
# direc=supdir+'3perday_1/01errRun7cores/'
# direc=supdir+'2perday_1/01errRun7cores/'
# direc=supdir+'1perday_1/01errRun7cores/'
# direc=supdir+'1per2days_1/01errRun7cores/'
# direc=supdir+'1per3days_1/01errRun7cores/'
# direc=supdir+'1per5days_1/01errRun7cores/'
direc=supdir+'5perday_1/griz1errRun7cores/'
direc=supdir+'3perday_1/griz1errRun7cores/'
direc=supdir+'2perday_1/griz1errRun7cores/'
direc=supdir+'1perday_1/griz1errRun7cores/'
direc=supdir+'1per2days_1/griz1errRun7cores/'
direc=supdir+'1per3days_1/griz1errRun7cores/'
direc=supdir+'1per5days_1/griz1errRun7cores/'
direc=supdir+'5perday_1/griz05errRun7cores/'
direc=supdir+'3perday_1/griz05errRun7cores/'
direc=supdir+'2perday_1/griz05errRun7cores/'
direc=supdir+'1perday_1/griz05errRun7cores/'
direc=supdir+'1per2days_1/griz05errRun7cores/'
direc=supdir+'1per3days_1/griz05errRun7cores/'
direc=supdir+'1per5days_1/griz05errRun7cores/'

# KN = pd.read_csv(direc+'Bu2025InjRecovery_posterior_samples.dat', header=0, delimiter=" ")
# bf = json.load(open(direc+'Bu2025InjRecovery_bestfit_params.json','r'))
# decomposeBu25gains(KN, bf, N=20)

# ###Outputting to LaTeX tables:
# output = ''
# for x in decomposeBu25gains(KN, bf, N=20):
#     output += ' & '
#     if x<0.2:
#         output += '\cellcolor{orange!40}'
#     output += f'{x:.2f}'
# output += '\\\\'
# print(output)


import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ##########Plotting in cadence/error heatmap grid

# cadences = ['5 per day', '3 per day', '2 per day', '1 per day', '1 per 2 days', '1 per 3 days', '1 per 5 days']
# cads = ['5perday', '3perday', '2perday', '1perday', '1per2days', '1per3days', '1per5days']
# errormargins = [r'$\sigma_{\rm{sys}} = 1$ mag', r'$\sigma_{\rm{sys}} = 0.5$ mag', r'$\sigma_{\rm{sys}} = 0.3$ mag',
#                 r'$\sigma_{\rm{sys}} = 0.2$ mag', r'$\sigma_{\rm{sys}} = 0.1$ mag']
# errs = ['1err','05err','03err','02err','01err']
# errs = ['griz1err','griz05err','griz03err','griz02err','griz01err']
# lablist = [r'$\log_{10}M_{ej}^{dyn}$', r'$v_{ej}^{dyn}$', r'$Y_e^{dyn}$', r'$\log_{10}M_{ej}^{wind}$',
#             r'$v_{ej}^{wind}$', r'$Y_e^{wind}$', 'Inclination', 'Distance']


# paramlist = ['log10_mej_dyn','v_ej_dyn','Ye_dyn','log10_mej_wind','v_ej_wind','Ye_wind','inclination_EM','luminosity_distance']
# paramwisegains = {}
# for p in paramlist:
#     paramwisegains[p]=np.zeros((len(cadences),len(errormargins)))

# supdir = '/home/hussenot/Bu2025study/Injections/Bu25Injection5/'
# for i,cad in enumerate(cads):
#     print(cad)
#     for j,err in enumerate(errs):
#         direc=supdir+cad+'_1/'+err+'Run7cores/'
#         KN = pd.read_csv(direc+'Bu2025InjRecovery_posterior_samples.dat', header=0, delimiter=" ")
#         bf = json.load(open(direc+'Bu2025InjRecovery_bestfit_params.json','r'))
#         gains = decomposeBu25gains(KN, bf, N=20)
#         for k,p in enumerate(paramlist):
#             paramwisegains[p][i,j]=gains[k+1]

# colors=['red', 'white']
# threshold = 0.2

# for N in range(8):
#     fig,ax = plt.subplots(1,1,figsize=(6,9))
#     im = ax.imshow(paramwisegains[paramlist[N]], vmin=0,vmax=6)
#     ax.set_xticks(range(len(errs)), labels=errormargins, rotation=30, fontsize=20)
#     ax.set_yticks(range(len(cads)), labels=cadences, fontsize=20)
    
#     for i in range(len(cadences)):
#         for j in range(len(errormargins)):
#             dat = paramwisegains[paramlist[N]][i, j]
#             text = ax.text(j, i, np.round(dat,decimals=2), fontsize=20,
#                             ha="center", va="center", color=colors[int(dat>threshold)])
    
#     ax.set_title(lablist[N], fontsize=24)
#     # fig.savefig('/home/hussenot/Bu2025study/Plots/ParamWiseGains/CadenceErrHeatmapBu2025griz_'+paramlist[N]+'.pdf', format='pdf', bbox_inches='tight')


# ##############Plotting Bu25 Injection 5 1perday1 among 1perday
# paramlist = ['log10_mej_dyn','v_ej_dyn','Ye_dyn','log10_mej_wind','v_ej_wind','Ye_wind','inclination_EM','luminosity_distance','Mutual Information']
# paramwisegains = {}
# for p in paramlist:
#     paramwisegains[p]=np.zeros(8)

# supdir = '/home/hussenot/Bu2025study/Injections/Bu25Injection5/'
# cad='1perday_'
# err='/05err'
# for i in range(1,9):
#     direc=supdir+cad+str(i)+err+'Run7cores/'
#     KN = pd.read_csv(direc+'Bu2025InjRecovery_posterior_samples.dat', header=0, delimiter=" ")
#     bf = json.load(open(direc+'Bu2025InjRecovery_bestfit_params.json','r'))
#     gains = decomposeBu25gains(KN, bf, N=20)
#     for k,p in enumerate(paramlist):
#         paramwisegains[p][i-1]=gains[k+1]

# fig,ax = plt.subplots(1,1,figsize=(6,8))
# for k,p in enumerate(paramlist):
#     plt.plot([k]*8,paramwisegains[p], linestyle='', marker='+', alpha=0.5, color='grey', markersize=10)
#     plt.plot(k,paramwisegains[p][0], color='red', marker='+')
# ax.set_xticks(range(9), labels=paramlist, rotation=60, fontsize=14)
# ax.set_ylabel('Parameter-wise information gain [nat]', fontsize=20)
# plt.show()
# fig.savefig('/home/hussenot/Bu2025study/Plots/ParamWiseGains/GainsInjection5_1perday_05err.pdf', format='pdf', bbox_inches='tight')

# ##############Plotting Bu25 1perday1 Injection5 among all Injections
# paramlist = ['log10_mej_dyn','v_ej_dyn','Ye_dyn','log10_mej_wind','v_ej_wind','Ye_wind','inclination_EM','luminosity_distance','Mutual Information']
# paramwisegains = {}
# for p in paramlist:
#     paramwisegains[p]=np.zeros(100)

# supdir = '/home/hussenot/Bu2025study/Injections/Bu25Injection'
# cad='/1perday_1/'
# err='05err'
# for i in range(100):
#     direc=supdir+str(i)+cad+err+'Run7cores/'
#     KN = pd.read_csv(direc+'Bu2025InjRecovery_posterior_samples.dat', header=0, delimiter=" ")
#     bf = json.load(open(direc+'Bu2025InjRecovery_bestfit_params.json','r'))
#     gains = decomposeBu25gains(KN, bf, N=20)
#     for k,p in enumerate(paramlist):
#         paramwisegains[p][i]=gains[k+1]

# fig,ax = plt.subplots(1,1,figsize=(6,8))
# for k,p in enumerate(paramlist):
#     plt.plot([k]*100,paramwisegains[p], linestyle='', marker='+', alpha=0.5, color='grey', markersize=10)
#     plt.plot(k,paramwisegains[p][5], color='red', marker='+')
# ax.set_xticks(range(9), labels=paramlist, rotation=60, fontsize=14)
# ax.set_ylabel('Parameter-wise information gain [nat]', fontsize=20)
# plt.show()
# fig.savefig('/home/hussenot/Bu2025study/Plots/ParamWiseGains/Gains_1perday1_05err_Inj5among100.pdf', format='pdf', bbox_inches='tight')

##############Violin Plot Bu25 1perday1 all Injections
paramlist = ['log10_mej_dyn','v_ej_dyn','Ye_dyn','log10_mej_wind','v_ej_wind','Ye_wind','inclination_EM','luminosity_distance']#,'Mutual Information']
labels = [r'$\log_{10}M_{ej}^{dyn}$', r'$v_{ej}^{dyn}$', r'$Y_e^{dyn}$', r'$\log_{10}M_{ej}^{wind}$',
            r'$v_{ej}^{wind}$', r'$Y_e^{wind}$', r'cos($\iota$)', r'$D_L$']#, 'M.I.']
paramwisegains = {}
errs=['1err','05err']
for e in errs:
    paramwisegains[e]={}
    for p in paramlist:
        paramwisegains[e][p]=[]

# supdir = '/home/hussenot/Bu2025study/Injections/Bu25Injection'
# cad='/1perday_1/'
# errs=['1err','05err']
# for e in errs:
#     for i in range(100):
#         direc=supdir+str(i)+cad+e+'Run7cores/'
#         KN = pd.read_csv(direc+'Bu2025InjRecovery_posterior_samples.dat', header=0, delimiter=" ")
#         bf = json.load(open(direc+'Bu2025InjRecovery_bestfit_params.json','r'))
#         gains = decomposeBu25gains(KN, bf, N=20)
#         for k,p in enumerate(paramlist):
#             paramwisegains[e][p].append(gains[k+1])

# with open('/home/hussenot/Bu2025study/Paramwise_MLP25Sims_1perday1.json','w') as f:
#     json.dump(paramwisegains, f)

# paramwisegains=json.load(open('/home/hussenot/Bu2025study/Paramwise_MLP25Sims_1perday1.json','r'))

# fig,ax = plt.subplots(1,1,figsize=(8,7))
# parts=ax.violinplot([paramwisegains['1err'][p] for p in paramlist],vert=True,showextrema=False, side='low')
# for pc in parts['bodies']:
#     pc.set_edgecolor('black')
#     pc.set_alpha(1)
#     pc.set_facecolor('blue')
# legs = [(mpatches.Patch(color='blue'),r'$\sigma_{\rm sys} = 1$ mag'),
#           (mpatches.Patch(color='green'),r'$\sigma_{\rm sys} = 0.5$ mag')]
# parts2=ax.violinplot([paramwisegains['05err'][p] for p in paramlist],vert=True,showextrema=False, side='high')
# for pc in parts2['bodies']:
#     pc.set_edgecolor('black')
#     pc.set_alpha(1)
#     pc.set_facecolor('green')
# ax.axhline(0.2,color='red')
# ax.legend(*zip(*legs), fontsize=20)
# ax.set_xticks(range(1,9), labels=labels, rotation=0, fontsize=14)
# ax.set_ylabel('Parameter-wise information gain [nat]', fontsize=20)
# ax.set_title('Bu2025MLP simulations (1perday)', fontsize=20)
# # fig.savefig('/home/hussenot/Bu2025study/Plots/ParamWiseGains/Gains_1perday1_Bu25All100.pdf', format='pdf', bbox_inches='tight')

##############Violin Plot Bu19 ManySims 1perday1 all Injections
paramlist = ['log10_mej_dyn','log10_mej_wind','KNphi','cos_iota','luminosity_distance']#,'Mutual Information']
labels = [r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
          r'$\phi$', r'cos($\iota$)', r'$D_L$']#, 'M.I.']
paramwisegains = {}
errs=['grizyJHK','grizy05JHK']
for e in errs:
    paramwisegains[e]={}
    for p in paramlist:
        paramwisegains[e][p]=[]

# supdir = '/home/hussenot/H0/kilonovae-H0/Injection_Recovery_IterationsVariation/InjectionBaseLightcurve'
# cad='/1perday_'
# errs=['grizyJHK','grizy05JHK']
# for e,N in [('grizy05JHK',8),('grizyJHK',22),]:
#     for i in range(1,N+1):
#         print(i)
#         for j in range(1,21):
#             direc=supdir+str(i)+cad+str(j)+'/'+e+'/outdirBNSBu32cores/'
#             KN = pd.read_csv(direc+'InjectionRecoveryIterations_posterior_samples.dat', header=0, delimiter=" ")
#             KN['cos_iota'] = np.cos(KN['inclination_EM'])
#             bf = json.load(open(direc+'InjectionRecoveryIterations_bestfit_params.json','r'))
#             bf['cos_iota'] = np.cos(bf['inclination_EM'])
#             gains = decomposeBu19gains(KN, bf, N=20)
#             for k,p in enumerate(paramlist):
#                 paramwisegains[e][p].append(gains[k+1])

# with open('/home/hussenot/Bu2025study/Paramwise_Bu19ManySims22x20_1perday.json','w') as f:
#     json.dump(paramwisegains, f)

# paramwisegains=json.load(open('/home/hussenot/Bu2025study/Paramwise_Bu19ManySims22x20_1perday.json','r')) 
# fig,ax = plt.subplots(1,1,figsize=(6,7))
# parts=ax.violinplot([paramwisegains['grizyJHK'][p] for p in paramlist],vert=True,showextrema=False, side='low')
# for pc in parts['bodies']:
#     pc.set_edgecolor('black')
#     pc.set_alpha(1)
#     pc.set_facecolor('blue')
# legs = [(mpatches.Patch(color='blue'),r'$\sigma_{\rm sys} = 1$ mag'),
#           (mpatches.Patch(color='green'),r'$\sigma_{\rm sys} = 0.5$ mag')]
# parts2=ax.violinplot([paramwisegains['grizy05JHK'][p] for p in paramlist],vert=True,showextrema=False, side='high')
# for pc in parts2['bodies']:
#     pc.set_edgecolor('black')
#     pc.set_alpha(1)
#     pc.set_facecolor('green')
# ax.axhline(0.2,color='red')
# ax.legend(*zip(*legs), fontsize=18)
# ax.set_xticks(range(1,6), labels=labels, rotation=0, fontsize=13)
# ax.set_ylabel('Parameter-wise information gain [nat]', fontsize=20)
# ax.set_title('Bu2019lm simulations (1perday)', fontsize=20)
# # fig.savefig('/home/hussenot/Bu2025study/Plots/ParamWiseGains/Gains_1perday_Bu19All22x20.pdf', format='pdf', bbox_inches='tight')



# ################Injection Recovery Plot Bu25Injection5 against cadence with param-wise gain
# supdir = '/home/hussenot/Bu2025study/Injections/Bu25Injection5/'
# dirs = []
# title='Recovery of Bu2025MLP injection 5 with grizyJHK filters'
# label = 'Bu2025InjRecovery'

# paramlist = ['log10_mej_dyn','v_ej_dyn','Ye_dyn','log10_mej_wind','v_ej_wind','Ye_wind','inclination_EM','luminosity_distance']
# lablist = [r'$\log_{10}M_{ej}^{dyn}$', r'$v_{ej}^{dyn}$', r'$Y_e^{dyn}$', r'$\log_{10}M_{ej}^{wind}$',
#            r'$v_{ej}^{wind}$', r'$Y_e^{wind}$', 'Inclination', 'Distance']
# Inj = [-2.7887955581604307,0.21004272454740489,0.2669085351958312,-1.4759670187165341,0.07665437605400971,
#        0.26859221386679843,0.2812965809719635,40.0]

# npar=5
# par, lpar , val = paramlist[npar],lablist[npar], Inj[npar]

# ###Cadences
# dirs.append(supdir+'5perday_1/1errRun7cores/')
# dirs.append(supdir+'3perday_1/1errRun7cores/')
# dirs.append(supdir+'2perday_1/1errRun7cores/')
# dirs.append(supdir+'1perday_1/1errRun7cores/')
# dirs.append(supdir+'1per2days_1/1errRun7cores/')
# dirs.append(supdir+'1per3days_1/1errRun7cores/')
# dirs.append(supdir+'1per5days_1/1errRun7cores/')

# # dirs.append(supdir+'5perday_1/05errRun7cores/')
# # dirs.append(supdir+'3perday_1/05errRun7cores/')
# # dirs.append(supdir+'2perday_1/05errRun7cores/')
# # dirs.append(supdir+'1perday_1/05errRun7cores/')
# # dirs.append(supdir+'1per2days_1/05errRun7cores/')
# # dirs.append(supdir+'1per3days_1/05errRun7cores/')
# # dirs.append(supdir+'1per5days_1/05errRun7cores/')
# labels=['5 per day', '3 per day', '2 per day', '1 per day', '1 per 2 days', '1 per 3 days', '1 per 5 days']
# lbly='Average frequency of observations in each band'

# sample = []
# mean = []
# median = []
# std = []
# best = []
# sig = []
# perc = []
# KL = []
# chi2 = []
# logL = []
# combine = []
# partialgain = []
# # val = np.log(val)
# for d in dirs:
#     s=pd.read_csv(d+label+'_posterior_samples.dat', header=0, delimiter=" ")
#     sp = s[par]
#     combine += [sp[k] for k in range(len(sp))]
#     # sp = np.log(sp)
#     sample.append(sp)
#     median.append(np.median(sp))
#     mean.append(np.mean(sp))
#     std.append(np.std(sp))
#     b=json.load(open(d+label+'_bestfit_params.json','r'))
#     best.append(b[par])
#     bayes = b['log_bayes_factor']
#     KL.append( np.mean(s['log_likelihood']) - bayes)
#     logL.append(b['log_likelihood'])
#     chi2.append(b['chi2_per_dof'])
#     sig.append( (val-np.mean(sp))/np.std(sp))
#     perc.append(np.mean(sp<val)*100)
#     partialgain.append(decomposeBu25gains(s, b, N=20)[npar+1])


# #Violin plots of the posterior distributions
# quant = [0.5]
# quant = [0.16,0.5,0.84]
# # quant = [0.05,0.5,0.95]

# fig, ax = plt.subplots(1,1, figsize = (7,9)) #12,12 for overleaf KL plots. 9,9 for pdf

# #Plotting posterior distributions
# ax.axvline(val, label='Injected value', color='black')
# # ax.boxplot(sample, vert=False, showfliers=False, labels=labels)
# ax.violinplot(sample, vert=False, showextrema=False, quantiles=[quant for s in sample])#, side='low')
# ax.plot(best, np.arange(len(dirs))+1, linestyle='', marker='o', label='bestfit estimate')
# # ax.plot(best, np.arange(len(dirs))+1, linestyle='', marker='o', label='bestfit err=0mag', color='blue')



# ax.set_yticks(np.arange(1, len(labels)+1), labels=labels, fontsize=18)
# # ax.yaxis.set_tick_params(labelleft=False)
# plt.xticks(fontsize=16)
# ax.invert_yaxis()
# ax.set_xlabel(lpar, fontsize = 20)
# ax.set_ylabel(lbly,fontsize = 20)
# # ax.set_title(title, fontsize=20)

# ax.legend(fontsize=18)

# #Adding the partial gain on the right-side
# pargain=np.round(partialgain,decimals=2)
# ax2 = ax.twinx()
# ax2.set_ylim(ax.get_ylim())
# ax2.set_yticks(np.arange(1, len(pargain)+1), labels=pargain, fontsize=20)
# ax2.set_ylabel(lpar+' partial information gain [nat]', fontsize=24)
# # fig.savefig('/home/hussenot/Bu2025study/Plots/Bu25_Cadence_ParamGain_Yewind.pdf', format='pdf', bbox_inches='tight')


###########
# for d in ['06Allfree','06Angleradio','06AngleradioGWdistance','06AngleradioGWdistance+masses']:
#     sub = '/home/hussenot/H0/kilonovae-H0/170817/Errsys+constraints/'+d+'/outdirBNSBu32cores/Constraints170817'
#     KN = pd.read_csv(sub+'_posterior_samples.dat', header=0, delimiter=" ")
#     KN['cos_iota']=np.cos(KN['inclination_EM'])
#     bf = json.load(open(sub+'_bestfit_params.json','r'))
#     bf['cos_iota'] = np.cos(bf['inclination_EM'])
#     gains = decomposeBu19gains(KN,bf,N=20)
#     print(d)
#     # print(['log10_mej_dyn','log10_mej_wind','KNphi','cos_iota','luminosity_distance'])
#     print([f'{g:.2f}' for g in gains])

for d in ['06Default','06Angleradio','06AngleradioGWdistance','06AngleradioGWdistance+masses']:
    sub = '/home/hussenot/H0/kilonovae-H0/170817/Bu2025MLP/'+d+'/outdirBNSBu7cores/AT2017gfoBu2025'
    KN = pd.read_csv(sub+'_posterior_samples.dat', header=0, delimiter=" ")
    bf = json.load(open(sub+'_bestfit_params.json','r'))
    gains = decomposeBu25gains(KN,bf,N=20)
    print(d)
    # print(['log10_mej_dyn','v_ej_dyn','Ye_dyn','log10_mej_wind','v_ej_wind','Ye_wind','inclination_EM','luminosity_distance']#,'Mutual Information'])
    print([f'{g:.2f}' for g in gains])