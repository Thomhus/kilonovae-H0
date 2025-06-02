#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:14:57 2024

@author: hussenot
"""

import numpy as np
import glob
import pandas as pd
import matplotlib.pyplot as plt
import json
from astropy.table import Table

Injections = {}
#Index 0 is the 170817 bestfit injection
Injections['KNphi'] = [31.033359307564652, 60, 53,
                       28.00338113, 28.84181664, 21.14433759, 49.46252534, 59.30197033,
       26.84136451, 51.63413138, 63.41187   , 24.90001225, 40.11151919,
       42.30267616, 18.87695094, 55.06204702, 53.91511799, 28.64139531,
       41.64408314, 41.50236677, 30.12996258, 52.79320033, 61.305053  ]
Injections['log10_mej_dyn'] = [-2.236983615436653, np.log10(0.010), np.log10(0.007),
                               -2.1685562 , -1.53114099, -1.89340053, -2.45002188, -2.72305989,
       -2.97836487, -2.22463734, -1.8359392 , -2.04675365, -2.39641537,
       -1.93035833, -1.99174893, -2.8388448 , -2.91796954, -2.28273025,
       -2.10663757, -2.78966645, -1.71379507, -2.55730184, -2.75972211]
Injections['log10_mej_wind'] = [-0.9959807211519678, np.log10(0.05), np.log10(0.04),
                                -1.62913266, -0.78967631, -0.77958405, -1.77082526, -1.8503249 ,
       -0.69157357, -0.51735504, -1.1377273 , -1.58428609, -0.98929691,
       -1.19203596, -1.96983847, -1.13579142, -0.88169226, -1.18216514,
       -1.38307693, -1.48061402, -1.79612824, -1.42620425, -1.89701975]
Injections['cosKNtheta'] = [np.cos(1.2727477446277973), 0.8, 0.75,
                            0.93810532, 0.99297351, 0.50616015, 0.5779006 , 0.10882965,
       0.64894437, 0.09700895, 0.75866399, 0.17907588, 0.109746  ,
       0.72135561, 0.57928337, 0.748148  , 0.29600959, 0.18615174,
       0.37029653, 0.47710132, 0.24295105, 0.25833745, 0.16137993]
Injections['luminosity_distance'] = [41.168672037183725]+[40]*22

# ##Generating the result files
# N = 0
# supdir = '/home/hussenot/H0/kilonovae-H0/lcsimu/'
# label = 'Simu2019lm'
# dirs=[]
# for i in range(1,21):
#     dirs.append(supdir+'1perday'+str(i)+'/grizJHK')

# N = 8
# supdir = '/home/hussenot/H0/kilonovae-H0/Injection_Recovery_IterationsVariation/InjectionBaseLightcurve'+str(N)+'/'
# label = 'InjectionRecoveryIterations'

# # Open the 20 iterations of the recovery analysis
# dirs=[]
# for i in range(1,21):
#     dirs.append(supdir+'1perday_'+str(i)+'/grizy00JHK')


# result = {}
# injected = {}
# combined = {}
# total = {}
# for par in ['KNphi','log10_mej_dyn','log10_mej_wind', 'cosKNtheta', 'luminosity_distance']:
#     injected[par]=Injections[par][N]
#     combined[par]=[]
#     total[par]={}
    

# #Set up 
# KL=[]
# for d in dirs:
#     s=pd.read_csv(d+'/outdirBNSBu32cores/'+label+'_posterior_samples.dat', header=0, delimiter=" ")
#     s['cosKNtheta']=np.cos(s['inclination_EM'])
#     b=json.load(open(d+'/outdirBNSBu32cores/'+label+'_bestfit_params.json','r'))
#     bayes = b['log_bayes_factor']
#     KL.append( np.mean(s['log_likelihood']) - bayes)
#     for par in ['KNphi','log10_mej_dyn','log10_mej_wind', 'cosKNtheta', 'luminosity_distance']:
#         sp = s[par]
#         combined[par] += [sp[k] for k in range(len(sp))]


# for par in ['KNphi','log10_mej_dyn','log10_mej_wind', 'cosKNtheta', 'luminosity_distance']:
#     val = injected[par]
#     s = combined[par]
#     total[par]['mean']=np.mean(s)
#     total[par]['median']=np.median(s)
#     total[par]['offset']=np.median(s)-val
#     total[par]['std']=np.std(s)
#     total[par]['q16']=np.percentile(s,16)
#     total[par]['q84']=np.percentile(s,84)
    
    
# ###################

# mean = {}
# median = {}
# offset = {}
# std = {}
# q16 = {}
# q84 = {}
# best = {}
# sigma = {}
# perc = {}
# for metric in [mean, median, offset, std, q16, q84, best, sigma, perc]:
#     for par in ['KNphi','log10_mej_dyn','log10_mej_wind', 'cosKNtheta', 'luminosity_distance']:
#         metric[par]=[]
# for d in dirs:
#     b=json.load(open(d+'/outdirBNSBu32cores/'+label+'_bestfit_params.json','r'))
#     s=pd.read_csv(d+'/outdirBNSBu32cores/'+label+'_posterior_samples.dat', header=0, delimiter=" ")
#     s['cosKNtheta']=np.cos(s['inclination_EM'])
#     b['cosKNtheta']=np.cos(b['inclination_EM'])
#     for par in ['KNphi','log10_mej_dyn','log10_mej_wind', 'cosKNtheta', 'luminosity_distance']:
#         best[par].append(b[par])
#         val = injected[par]
#         sp = s[par]
#         median[par].append(np.median(sp))
#         mean[par].append(np.mean(sp))
#         offset[par].append(np.median(sp)-val)
#         std[par].append(np.std(sp))
#         q16[par].append(np.percentile(sp, 16))
#         q84[par].append(np.percentile(sp, 84))
#         sigma[par].append( (val-np.mean(sp))/np.std(sp))
#         perc[par].append(np.mean(sp<val)*100)

# result['injection']=injected
# result['Properties of cumulated runs']=total
# result['KL Posterior||Prior']=KL
# result['Posterior distribution means']=mean
# result['Posterior distribution medians']=median
# result['Posterior distribution bestfits']=best
# result['Posterior distribution offsets']=offset
# result['Posterior distribution standard deviations']=std
# result['Posterior distribution 16th percentile']=q16
# result['Posterior distribution 84th percentile']=q84
# result['Posterior distribution offsets (in sigmas)']=sigma
# result['Percentile of the true value in posterior distribution']=perc
# # result['Combined samples distribution']=combined

# with open('/home/hussenot/H0/Injection_Recovery_Iterations_0err_LC'+str(N)+'.json', 'w', encoding='utf-8') as f:
#     json.dump(result, f, ensure_ascii=False, indent=4)
    
####Defining the 'distance from interpolation points' metric

Grid = {}
Grid['KNphi'] = [15,30,45,60,75]
Grid['log10_mej_dyn'] = [-3, np.log10(0.005), -2, np.log10(0.020), -1.5 -1.5 -np.log10(0.020)] #open end
Grid['log10_mej_wind'] = [-2, np.log10(0.03), np.log10(0.05), np.log10(0.07), np.log10(0.09), 
                          np.log10(0.11), np.log10(0.13), -0.5 -0.5 -np.log10(0.13)] #open end
Grid['cosKNtheta'] = [k/10 for k in range(11)]

def grid_distance(x, param='KNphi'):
    G = Grid[param]
    for i in range(len(G)):
        if x < G[i+1]:
            scaled = (x-G[i])/(G[i+1]-G[i])
            return 1 - np.abs(2*scaled -1)

# test , param = np.arange(15,75,0.1),'KNphi'
# test , param = np.arange(-3,-1.5,0.001),'log10_mej_dyn'
# test , param = np.arange(-2,-0.5,0.001),'log10_mej_wind'
# test , param = np.arange(0,1,0.001),'cosKNtheta'
# dtest = [grid_distance(x, param=param) for x in test]
# plt.scatter(test, dtest)
# for x in Grid[param]:
#     plt.axvline(x)

def grid_distance_total(inject):
    result = 0
    for par in ['KNphi','log10_mej_dyn','log10_mej_wind', 'cosKNtheta']:
        result += grid_distance(inject[par],param=par)
    return result

####Making the final plots

pary,lpary = 'luminosity_distance','Distance (Mpc)'
# pary,lpary = 'KNphi',r'$\phi$ (degrees)'
# pary,lpary = 'log10_mej_dyn',r'$\log_{10}M_{ej}^{dyn}$'
# pary,lpary = 'log10_mej_wind',r'$\log_{10}M_{ej}^{wind}$'
# pary,lpary = 'cosKNtheta',r'Inclination $cos(\iota)$'

parx,lparx = 'KNphi',r'$\phi$ (degrees)'
# parx,lparx = 'log10_mej_dyn',r'$\log_{10}M_{ej}^{dyn}$'
parx,lparx = 'log10_mej_wind',r'$\log_{10}M_{ej}^{wind}$'
# parx,lparx = 'cosKNtheta',r'Inclination $cos(\iota)$'

x = []
true = []
median = []
offset = []
std = []
q16 = []
q84 = []
offsetdist = []
dist68 = []
KL = []
d_x = []
d_total = []

med_170817 = []
d68_170817 = []
KL_170817 = []

for N in range(1,23):
    result = json.load(open('/home/hussenot/H0/Injection_Recovery_Iterations_LC'+str(N)+'.json','r'))
    x.append(result['injection'][parx])
    true.append(result['injection'][pary])
    median.append(result['Properties of cumulated runs'][pary]['median'])
    offset.append(result['Properties of cumulated runs'][pary]['offset'])
    std.append(result['Properties of cumulated runs'][pary]['std'])
    q16.append(result['Properties of cumulated runs'][pary]['q16'])
    q84.append(result['Properties of cumulated runs'][pary]['q84'])
    offsetdist.append(result['Posterior distribution offsets'][pary])
    d16 = result['Posterior distribution 16th percentile'][pary]
    d84 = result['Posterior distribution 84th percentile'][pary]
    dist68.append([d84[k]-d16[k] for k in range(len(d16))])
    KL.append(result['KL Posterior||Prior'])
    d_x.append(grid_distance(result['injection'][parx], param=parx))
    d_total.append(grid_distance_total(result['injection']))
    
    supdir = '/home/hussenot/H0/kilonovae-H0/Injection_Recovery_IterationsVariation/InjectionBaseLightcurve'+str(N)+'/'
    s=pd.read_csv(supdir+'170817like_cadence/grizyJHK/outdirBNSBu32cores/InjectionRecoveryIterations_posterior_samples.dat', header=0, delimiter=" ")
    s['cosKNtheta']=np.cos(s['inclination_EM'])
    sp = s[pary]
    med_170817.append(np.median(sp))
    d68_170817.append(np.percentile(sp, 84)-np.percentile(sp, 16))
    b=json.load(open(supdir+'170817like_cadence/grizyJHK/outdirBNSBu32cores/InjectionRecoveryIterations_bestfit_params.json','r'))
    bayes = b['log_bayes_factor']
    KL_170817.append( np.mean(s['log_likelihood']) - bayes)
    
    
# fig, ax = plt.subplots(1,1, figsize = (10,10))

# ax.errorbar(x, median, yerr=[[median[k]-q16[k] for k in range(len(median))],
#                               [q84[k]-median[k] for k in range(len(median))]], linestyle='', marker='o', label='Posterior distribution: median and 68% confidence interval')
# ax.plot(x, true, marker='')
# # ax.plot(x, [true[k]+np.median(offsetdist[k]) for k in range(len(x))], linestyle='', marker='o')
# ax.set_xlabel('Injected '+lparx, fontsize = 20)
# ax.set_ylabel('Recovered '+lpary,fontsize = 20)
# # ax.set_title('Injection Recovery test', fontsize=20)
# ax.set_title('Cumulated results of 20 analyses of the same injections', fontsize=16)
# ax.legend(fontsize=16)

# # Distribution of systematic offsets
# med_off = [np.median(offsetdist[k]) for k in range(len(x))]
# print('Median offsets of '+pary+' (min, median, max): ',np.min(med_off), np.median(med_off), np.max(med_off))

# #Display posterior/prior ratios
# print(lpary, 'median value: ', np.median(median), np.median(med_170817))
# print('median 68% interval: ',np.median([q84[k]-q16[k] for k in range(len(q16))]),
#       np.median(dist68), np.median(d68_170817))
# print(np.median(KL), np.median(KL_170817))
# prior_size = 1 #60, 2, 2.5, 1, np.log(500) * 40
# print('ratio:', np.median(dist68)/prior_size, 'ratio170817:', np.median(d68_170817)/prior_size)

# fig, (ax1,ax2) = plt.subplots(2, 1, figsize=(12, 10))
# ax1.errorbar(x, offset, yerr=[[median[k]-q16[k] for k in range(len(median))],
#                               [q84[k]-median[k] for k in range(len(median))]], linestyle='', marker='o', label='Combined: offset and 68% interval', color='red')
# # ax1.violinplot(offsetdist, positions=x, showextrema=False, quantiles=None)
# # ax1.boxplot(offsetdist, positions=x, showfliers=False)
# ax1.scatter([[i]*20 for i in x], offsetdist, alpha=0.9, color='grey', label='median offsets of individual runs')
# ax1.set_ylabel('Recovered '+lpary+' offset', fontsize = 14)
# ax1.legend(fontsize=16)

# # ax2.violinplot(stddist, positions=x, showextrema=False, quantiles=None)
# # ax2.boxplot(stddist, positions=x, )
# ax2.scatter([[i]*20 for i in x], dist68, alpha=0.7, color='grey', label="intervals of individual runs")
# ax2.scatter(x, [q84[k]-q16[k] for k in range(len(q16))], color='red', label='interval of Combined results')
# ax2.set_ylabel('Recovered '+lpary+' 68% interval', fontsize = 14)
# ax2.set_xlabel('Injected '+lparx, fontsize = 20)
# ax2.legend(fontsize=16)

# fig, (ax1,ax2,ax3) = plt.subplots(3, 1, figsize=(14, 14))
# x = d_x
# x = d_total
# ax1.errorbar(x, offset, yerr=[[median[k]-q16[k] for k in range(len(median))],
#                               [q84[k]-median[k] for k in range(len(median))]], linestyle='', marker='o', label='Combined: offset and 68% interval', color='red')
# ax1.scatter([[i]*20 for i in x], offsetdist, alpha=0.9, color='grey', label='median offsets of individual runs')
# ax1.axhline(0)
# ax1.set_ylabel('Recovered '+lpary+' offset', fontsize = 14)
# ax1.legend(fontsize=16)

# ax2.scatter(x, [np.std(dist) for dist in offsetdist], color='red', label='Standard deviation of posterior medians among 20 iterations')
# ax2.legend(fontsize=16)

# ax3.scatter([[i]*20 for i in x], dist68, alpha=0.7, color='grey', label="intervals of individual runs")
# ax3.scatter(x, [q84[k]-q16[k] for k in range(len(q16))], color='red', label='interval of Combined results')
# ax3.set_ylabel('Recovered '+lpary+' 68% interval', fontsize = 14)
# # ax3.set_xlabel(lparx+' distance-to-grid', fontsize = 20)
# ax3.set_xlabel('Total distance-to-grid', fontsize = 20)
# ax3.legend(fontsize=16)

fig, ax = plt.subplots(1,1, figsize = (10,10))
# x = d_x
x = d_total
ax.scatter([[i]*20 for i in x], KL, alpha=0.2, color='grey', label="KL divergence of individual runs")
ax.scatter(x, [np.median(k) for k in KL], color='red', label="Median KL divergence")
ax.set_ylabel('K-L divergence Posterior||Prior', fontsize = 20)
# ax.scatter(x, KL_170817, color='blue', label='KL divergence with 170817 cadence')
# ax.scatter([[i]*20 for i in x], dist68, alpha=0.2, color='grey', label="Individual runs")
# ax.scatter(x, [np.median(k) for k in dist68], color='red', label="Median value")
# ax.set_ylabel('Recovered '+lpary+' 68% interval', fontsize = 20)
# ax.scatter([[i]*20 for i in x], offsetdist, alpha=0.2, color='grey', label="Individual runs")
# ax.scatter(x, [np.median(k) for k in offsetdist], color='red', label="Median value")
# ax.set_ylabel('Recovered '+lpary+' offset', fontsize = 20)

ax.set_xlabel('Injected '+lparx, fontsize = 20)
# ax.set_xlabel(lparx+' distance-to-grid', fontsize = 20)
ax.set_xlabel('Total distance-to-grid', fontsize = 20)
# ax.set_title('Constraining power of 20 analyses of the same injections', fontsize=16)
# ax.set_title('Constraining power of Injection Recovery analyses', fontsize=16)
ax.legend(fontsize=16)
# # # print([k > 10 for k in KL_170817])
# fig.savefig('/home/hussenot/H0/plots/KLWindCorrelation.pdf', format='pdf', bbox_inches='tight')

# print(np.mean(KL), np.std(KL))
y = KL
# y = dist68
# y = offsetdist
ax.axhline(np.mean(y), linestyle='dashed', label='Overall mean')
from scipy.stats import linregress
y1D = np.concatenate(y)
x1D = np.concatenate([[i]*20 for i in x])
reg = linregress(x1D, y1D)
# reg = linregress(x, [np.median(k) for k in y])
# print("slope: ",reg.slope, reg.stderr," intercept: ",reg.intercept)
ltotal = 'offset'+pary+'-dist_total'#+parx
print(ltotal)
print(f"Pearson r : {reg.rvalue:.3f}, pvalue of null(zero-slope): {reg.pvalue:.3e}, sigmas away from null: {reg.slope/reg.stderr:.3f}")
ax.plot(x1D, x1D*reg.slope+reg.intercept, label=f'Regression slope = {reg.slope:.2e} +/- {reg.stderr:.2e}')
ax.set_title(f'Linear regression: p-value {reg.pvalue:.1e} against no-slope null', fontsize=16)
ax.legend(fontsize=16)
# fig.savefig('/home/hussenot/H0/plots/Correlations/'+ltotal+'.pdf', format='pdf', bbox_inches='tight')

# #Saving the results in simpler form
# # np.save('/home/hussenot/H0/kilonovae-H0/Injection_Recovery_IterationsVariation/Correlations/Dump_KL.npy', KL)
# np.save('/home/hussenot/H0/kilonovae-H0/Injection_Recovery_IterationsVariation/Correlations/Dump_d68'+pary+'.npy', dist68)
# np.save('/home/hussenot/H0/kilonovae-H0/Injection_Recovery_IterationsVariation/Correlations/Dump_offset68'+pary+'.npy', offsetdist)

# # #Saving all the correlations in a Table
# # CorrTab.add_row([ltotal, reg.rvalue, reg.pvalue, reg.slope/reg.stderr])
# # CorrTab.write('/home/hussenot/Downloads/CorrelationTable.csv', format='ascii.csv')
# Corr = Table.read('/home/hussenot/H0/kilonovae-H0/Injection_Recovery_IterationsVariation/Correlations/CorrelationTable.csv',
#                      format='ascii.csv')
# fig, ax = plt.subplots(1,1, figsize = (10,10))
# ax.scatter(Corr['pvalue'], Corr['r_Pearson'])
# # ax.scatter(Corr['pvalue'], Corr['sigmas'])
# ax.set_xscale('log')
# ax.invert_xaxis()
# ax.set_xlabel('Slope vs no-slope p -value')
# ax.axvline(1)
# # ax.axhline(5)
# # ax.axhline(-5)
# ax.axvline(1e-6, color='red')
# ax.set_ylabel('Pearson r coefficient')
# # ax.set_ylabel('Number of sigmas away from slope=0')


# fig, ax3 = plt.subplots(1,1, figsize = (10,10))
# ax3.scatter([[i]*20 for i in x], dist68, alpha=0.2, color='grey', label="intervals of individual runs")
# ax3.scatter(x, [q84[k]-q16[k] for k in range(len(q16))], color='red', label='interval of Combined results')
# ax3.scatter(x, d68_170817, color='blue', label='Interval of 170817-like cadence')
# ax3.set_ylabel('Recovered '+lpary+' 68% interval', fontsize = 14)
# ax3.set_xlabel('Injected '+lparx, fontsize = 20)
# # ax3.set_xlabel(lparx+' distance-to-grid', fontsize = 20)
# # ax3.set_xlabel('Total distance-to-grid', fontsize = 20)
# ax3.legend(fontsize=16)

# #Spread versus posterior size test
# fig, ax = plt.subplots(1,1, figsize = (10,10))
# max_interval=None
# if pary != 'luminosity_distance':
#     max_interval = 0.68 * (Grid[pary][-1] - Grid[pary][0])
#     ax.axvline(max_interval, color='black', label='Prior interval')
# x =[np.median(k) for k in dist68]
# y = [np.percentile(k, 84)-np.percentile(k, 16) for k in offsetdist]
# ratios = [y[i]/x[i] for i in range(len(x))]
# ratio = np.mean(ratios)
# ax.scatter(x,y, label="Runs with err = 1 mag")
# ax.plot(x, [a*ratio for a in x], marker='', label = 'Average ratio = '+str(round(ratio, 3)))
# ax.set_xlabel('Recovered '+lpary+' 68% interval', fontsize = 14)
# ax.set_ylabel('68% variability in '+lpary+' posterior medians', fontsize = 14)
# ax.legend(fontsize=16)
# ax.set_title('Time-variability spread against Median posterior size', fontsize=18)
# ax.set_xscale('log')
# ax.set_yscale('log')



# # ##1 mag vs 0.5 mag Comparison
# # fig, ax = plt.subplots(1,1, figsize = (10,10))
# # ax.plot(x, [np.median(k) for k in dist68], linestyle='',marker='.', label='err = 1 mag', markersize=20)
# # ax.set_xlabel('Injected '+lparx, fontsize = 20)
# # ax.set_ylabel('Recovered '+lpary +' 68% interval',fontsize = 20)
# # # ax.set_title('Injection Recovery test', fontsize=20)
# # # ax.set_title('Cumulated results of 20 analyses of the same injections', fontsize=16)
# # ax.legend(fontsize=16)

# x = []
# offsetdist = []
# dist68 = []

# for N in range(1,9):
#     result = json.load(open('/home/hussenot/H0/Injection_Recovery_Iterations_05err_LC'+str(N)+'.json','r'))
#     x.append(result['injection'][parx])
#     offsetdist.append(result['Posterior distribution offsets'][pary])
#     d16 = result['Posterior distribution 16th percentile'][pary]
#     d84 = result['Posterior distribution 84th percentile'][pary]
#     dist68.append([d84[k]-d16[k] for k in range(len(d16))])
#     KL.append(result['KL Posterior||Prior'])

# # ax.plot(x, [np.median(k) for k in dist68], linestyle='',marker='.', label='err = 0.5 mag', markersize=20)
# # ax.legend(fontsize=16)
# # ax.axhline(0)

# x =[np.median(k) for k in dist68]
# y = [np.percentile(k, 84)-np.percentile(k, 16) for k in offsetdist]
# ratios = [y[i]/x[i] for i in range(len(x))]
# ratio = np.mean(ratios)
# ax.scatter(x,y, label="Runs with err = 0.5 mag")
# ax.plot(x, [a*ratio for a in x], marker='', label = 'Average ratio = '+str(round(ratio, 3)))
# ax.legend(fontsize=16)


# x = []
# offsetdist = []
# dist68 = []
# for N in range(1,9):
#     result = json.load(open('/home/hussenot/H0/Injection_Recovery_Iterations_02err_LC'+str(N)+'.json','r'))
#     x.append(result['injection'][parx])
#     offsetdist.append(result['Posterior distribution offsets'][pary])
#     d16 = result['Posterior distribution 16th percentile'][pary]
#     d84 = result['Posterior distribution 84th percentile'][pary]
#     dist68.append([d84[k]-d16[k] for k in range(len(d16))])

# # ax.plot(x, [np.median(k) for k in dist68], linestyle='',marker='.', label='err = 0 mag', markersize=20)
# # ax.legend(fontsize=16)

# x =[np.median(k) for k in dist68]
# y = [np.percentile(k, 84)-np.percentile(k, 16) for k in offsetdist]
# ratios = [y[i]/x[i] for i in range(len(x))]
# ratio = np.mean(ratios)
# ax.scatter(x,y, label="Runs with err = 0.2 mag")
# ax.plot(x, [a*ratio for a in x], marker='', label = 'Average ratio = '+str(round(ratio, 3)))
# ax.legend(fontsize=16)

# x = []
# offsetdist = []
# dist68 = []
# for N in range(1,9):
#     result = json.load(open('/home/hussenot/H0/Injection_Recovery_Iterations_0err_LC'+str(N)+'.json','r'))
#     x.append(result['injection'][parx])
#     offsetdist.append(result['Posterior distribution offsets'][pary])
#     d16 = result['Posterior distribution 16th percentile'][pary]
#     d84 = result['Posterior distribution 84th percentile'][pary]
#     dist68.append([d84[k]-d16[k] for k in range(len(d16))])

# # ax.plot(x, [np.median(k) for k in dist68], linestyle='',marker='.', label='err = 0 mag', markersize=20)
# # ax.legend(fontsize=16)

# x =[np.median(k) for k in dist68]
# y = [np.percentile(k, 84)-np.percentile(k, 16) for k in offsetdist]
# ratios = [y[i]/x[i] for i in range(len(x))]
# ratio = np.mean(ratios)
# ax.scatter(x,y, label="Runs with err = 0 mag")
# ax.plot(x, [a*ratio for a in x], marker='', label = 'Average ratio = '+str(round(ratio, 3)))


# xmin,xmax = ax.get_xlim()
# if max_interval!=None:
#     xmax = min(xmax,max_interval)
# ax.plot([xmin,xmax], [0.5*xmin, 0.5*xmax], color='grey', marker='', linestyle='dashed', label='0.5 ratio')
# ax.legend(fontsize=16)

# fig.savefig('/home/hussenot/H0/plots/TimeVariationSpread_angle.pdf', format='pdf')

# #######Corner plots
# samples = {}

# params = ['KNphi', 'log10_mej_dyn', 'log10_mej_wind', 'cosKNtheta']
# labels = [r'$\phi$', r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
#           r'cos($\theta_{obs}$)']

# fig, ax = plt.subplots(4,4, figsize = (10,9))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# import corner
# import matplotlib as mpl

# corner.corner(Injections , color='blue', fig=fig, bins=4,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               plot_density=False, plot_datapoints=True, fill_contours=False,plot_contours=False, 
#               smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16}, levels=None)

# for i,p in enumerate(params):
#     for z in Grid[p]:
#         xs = [None]*4
#         xs[i] = z
#         corner.overplot_lines(fig=fig, xs=xs, color='grey', linestyle='dashed', alpha=0.4)

# colorparam, label = [np.median(k) for k in KL], 'Median K-L divergence Posterior||Prior'
# # colorparam, label = [np.median(k) for k in dist68], 'Median 68% interval in '+lpary+' posterior'
# # colorparam, label = [q84[k]-q16[k] for k in range(len(q16))], 'Combined 68% interval in '+lpary+' posterior'
# # colorparam, label = [np.percentile(k, 84)-np.percentile(k, 16) for k in offsetdist], '68% variability in '+lpary+' posterior medians'



# norm = mpl.colors.Normalize(vmin=np.min(colorparam),vmax=np.max(colorparam))
# mapobject = mpl.cm.ScalarMappable(norm=norm, cmap='viridis')

# for i in range(22):
#     corner.overplot_points(fig=fig, xs=[Injections[p][i+1] for p in ['KNphi', 'log10_mej_dyn', 'log10_mej_wind', 'cosKNtheta']],
#                             color=mapobject.to_rgba(colorparam[i]), markersize=12)

# cb = fig.colorbar(mapobject, ax=ax.ravel().tolist(), orientation='vertical')
# cb.ax.tick_params(labelsize='large')
# cb.set_label(label=label, size=24)

# fig.savefig('/home/hussenot/H0/kilonovae-H0/Injection_Recovery_IterationsVariation/grid_KL.pdf', format='pdf', bbox_inches='tight')