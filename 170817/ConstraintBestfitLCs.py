#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 12:50:32 2025

@author: hussenot
"""

import numpy as np
# from scipy.interpolate import interp1d
# import pandas as pd
# from astropy import time
import matplotlib.pyplot as plt
import json

# #old NMMA
# from nmma.em.io import loadEvent
# from nmma.em.utils import getFilteredMag
from nmma.em.model import SVDLightCurveModel

#Fiesta NMMA
from nmma.em.model import FiestaKilonovaModel
# from fiesta.inference.lightcurve_model import FluxModel
from nmma.em.io import load_em_observations
from nmma.em.utils import get_filtered_mag

plt.close()


# data = loadEvent('AT2017gfoMWcorrected.dat')
data = load_em_observations('AT2017gfoMWcorrected.dat')

trigger_time = 57982.52851851852
sample_times = np.arange(0.2, 15, 0.1)

fig, ax = plt.subplots(figsize=(6, 5))
ax.set_title(r'Lightcurves in $y$-band', fontsize=24)

filt = 'ps1::y'
color='black'


samples = data[filt]

# t, y, sigma_y = samples[:, 0], samples[:, 1], samples[:, 2]
t, y, sigma_y = samples['time'],samples['mag'],samples['mag_error']

t -= trigger_time
idx = np.where(~np.isnan(y))[0]
t, y, sigma_y = t[idx], y[idx], sigma_y[idx]

cut = [(t0<15) for t0 in t] #For Kband data
t, y, sigma_y = t[cut], y[cut], sigma_y[cut]


idx = np.where(np.isfinite(sigma_y))[0]
det_idx = idx
ax.errorbar(
    t[idx],
    y[idx],
    sigma_y[idx],
    fmt="o",
    color=color,
    label='AT2017gfo'
)

idx = np.where(~np.isfinite(sigma_y))[0]
ax.scatter(
    t[idx],
    y[idx],
    marker="v",
    color=color,
)

ax.invert_yaxis()
ax.set_ylabel('Apparent magnitude',fontsize=20)
ax.set_xlabel('Time [days]',fontsize=20)

# ##Adding Bu2019lm bestfits

# light_curve_model = SVDLightCurveModel('Bu2019lm', sample_times, svd_path='/home/hussenot/nmma/svdmodels/',
#                                         interpolation_type='sklearn_gp',filters=[filt])

# supdir = '/home/hussenot/H0/kilonovae-H0/170817/Errsys+constraints/'


# priors = [('06Allfree/','Bestfit A0.6'),
#           ('06Angleradio/','Bestfit B0.6'),
#           ('06AngleradioGWdistance/','Bestfit C0.6')
#            # ,('06AngleradioGWdistance+masses/','Bestfit D0.6')
#           ]
# for d,l in priors:
#     bestfit_params = json.load(open(supdir+d+'/outdirBNSBu32cores/Constraints170817_bestfit_params.json','r'))
    
#     _, mag = light_curve_model.generate_lightcurve(sample_times, bestfit_params)
#     mag_plot = getFilteredMag(mag, filt)
    
    
#     mag[filt] += 5.0 * np.log10(bestfit_params["luminosity_distance"] * 1e6 / 10.0)
    
#     ax.plot(
#         sample_times,
#         mag_plot,
#         linewidth=3,
#         linestyle="--"
#     )
    
#     ax.fill_between(sample_times, mag_plot+bestfit_params['em_syserr'], mag_plot-bestfit_params['em_syserr'], alpha=0.2, label=l)

# ##Adding Bu2025MLP bestfits

# model = FiestaKilonovaModel(model='Bu2025_MLP', surrogate_dir='/home/hussenot/fiestaEM/surrogates', filters=[filt])

# supdir = '/home/hussenot/H0/kilonovae-H0/170817/Bu2025MLP/'


# priors = [('06Default/','Bestfit A0.6'),
#           ('06Angleradio/','Bestfit B0.6'),
#           ('06AngleradioGWdistance/','Bestfit C0.6')
#            # ,('06AngleradioGWdistance+masses/','Bestfit D0.6')
#           ]
# for d,l in priors:
#     bestfit_params = json.load(open(supdir+d+'/outdirBNSBu7cores/AT2017gfoBu2025_bestfit_params.json','r'))
    
#     mAB = model.generate_lightcurve(sample_times,bestfit_params)

#     # _, mag = light_curve_model.generate_lightcurve(sample_times, bestfit_params)
#     mag_plot = get_filtered_mag(mAB, filt)
    
    
#     mag_plot += 5.0 * np.log10(bestfit_params["luminosity_distance"] * 1e6 / 10.0)
    
#     ax.plot(
#         sample_times,
#         mag_plot,
#         linewidth=3,
#         linestyle="--"
#     )
    
#     ax.fill_between(sample_times, mag_plot+bestfit_params['em_syserr'], mag_plot-bestfit_params['em_syserr'], alpha=0.2, label=l)


##Comparing both models
light_curve_model = SVDLightCurveModel('Bu2019lm', sample_times=sample_times, svd_path='/home/hussenot/nmma/svdmodels/',
                                        interpolation_type='sklearn_gp',filters=[filt])
#Technically this Bu2019lm surrogate through fiesta is not exactly the same as the old NMMA surrogate,
#It's close enough but a bit noisier
supdir = '/home/hussenot/H0/kilonovae-H0/170817/Errsys+constraints/06AngleradioGWdistance'
bestfit_params = json.load(open(supdir+'/outdirBNSBu32cores/Constraints170817_bestfit_params.json','r'))
bestfit_params['KNtheta']=bestfit_params['inclination_EM']
mag = light_curve_model.generate_lightcurve(sample_times, bestfit_params)
mag_plot = get_filtered_mag(mag, filt)
mag_plot += 5.0 * np.log10(bestfit_params["luminosity_distance"] * 1e6 / 10.0)
ax.plot(sample_times,mag_plot,linewidth=3, label = "Bu2019lm C0.6 bestfit")
ax.fill_between(sample_times, mag_plot+bestfit_params['em_syserr'], mag_plot-bestfit_params['em_syserr'], alpha=0.2)
   

model = FiestaKilonovaModel(model='Bu2025_MLP', surrogate_dir='/home/hussenot/fiestaEM/surrogates', filters=[filt])
supdir = '/home/hussenot/H0/kilonovae-H0/170817/Bu2025MLP/06AngleradioGWdistance'
bestfit_params = json.load(open(supdir+'/outdirBNSBu7cores/AT2017gfoBu2025_bestfit_params.json','r'))

mAB = model.generate_lightcurve(sample_times,bestfit_params)
mag_plot = get_filtered_mag(mAB, filt)
mag_plot += 5.0 * np.log10(bestfit_params["luminosity_distance"] * 1e6 / 10.0)
ax.plot(sample_times,mag_plot,linewidth=3, label = "Bu2025MLP C'0.6 bestfit")
ax.fill_between(sample_times, mag_plot+bestfit_params['em_syserr'], mag_plot-bestfit_params['em_syserr'], alpha=0.2)

ax.legend(fontsize=16)
ax.tick_params(axis='both', labelsize=15)
# plt.show()
# fig.savefig('/home/hussenot/H0/kilonovae-H0/170817/Errsys+constraints/Comparison06curves_'+filt+'.pdf', format='pdf', bbox_inches='tight')
# fig.savefig('/home/hussenot/H0/kilonovae-H0/170817/Bu2025MLP/Comparison06curves_'+filt+'.pdf', format='pdf', bbox_inches='tight')
fig.savefig('/home/hussenot/H0/kilonovae-H0/170817/Bu2025MLP/Bu19_vs_Bu25_'+filt+'.pdf', format='pdf', bbox_inches='tight')