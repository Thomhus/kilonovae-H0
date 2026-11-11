#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:36:52 2024

@author: hussenot
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

import corner




from matplotlib.collections import PathCollection
from matplotlib.patches import Polygon
def over_plot(ax, axKN):
   """
   This function takes two axes. All artists from the latter will
   be transfered onto the first.
   """
   artists = axKN.get_children()
   for artist in artists:
       if isinstance(artist, PathCollection) or isinstance(artist, Polygon):
           artist.remove()
           artist.axes = ax
           artist.set_transform(ax.transData)
           ax.add_artist(artist)
           

###################################
# COMPARISON OF BU2019LM ANALYSES OF AT2017GFO
# USED FOR FIGURES 3 and 14 OF ARTICLE
###################################

outdir = '/home/hussenot/H0/kilonovae-H0/170817/Errsys+constraints/'
Bu19 = pd.read_csv(outdir+'06Allfree/outdirBNSBu32cores/Constraints170817_posterior_samples.dat', header=0, delimiter=" ")
Bu19angle = pd.read_csv(outdir+'06Angleradio/outdirBNSBu32cores/Constraints170817_posterior_samples.dat', header=0, delimiter=" ")
Bu19angleGW = pd.read_csv(outdir+'06AngleradioGWdistance/outdirBNSBu32cores/Constraints170817_posterior_samples.dat', header=0, delimiter=" ")
# Bu19angleGWmasses = pd.read_csv(outdir+'06AngleradioGWdistance+masses/outdirBNSBu32cores/Constraints170817_posterior_samples.dat', header=0, delimiter=" ")

Bu19['cos_iota'] = np.cos(Bu19['inclination_EM'])
Bu19angle['cos_iota'] = np.cos(Bu19angle['inclination_EM'])
Bu19angleGW['cos_iota'] = np.cos(Bu19angleGW['inclination_EM'])
# Bu19angleGWmasses['cos_iota'] = np.cos(Bu19angleGWmasses['inclination_EM'])

bfBu19 = json.load(open(outdir+'06Allfree/outdirBNSBu32cores/Constraints170817_bestfit_params.json','r'))
bfBu19angle = json.load(open(outdir+'06Angleradio/outdirBNSBu32cores/Constraints170817_bestfit_params.json','r'))
bfBu19angleGW = json.load(open(outdir+'06AngleradioGWdistance/outdirBNSBu32cores/Constraints170817_bestfit_params.json','r'))
# bfBu19angleGWmasses = json.load(open(outdir+'06AngleradioGWdistance+masses/outdirBNSBu32cores/Constraints170817_bestfit_params.json','r'))
bfBu19['cos_iota'] = np.cos(bfBu19['inclination_EM'])
bfBu19angle['cos_iota'] = np.cos(bfBu19angle['inclination_EM'])
bfBu19angleGW['cos_iota'] = np.cos(bfBu19angleGW['inclination_EM'])
# bfBu19angleGWmasses['cos_iota'] = np.cos(bfBu19angleGWmasses['inclination_EM'])

# # # BuTF19 = pd.read_csv(outdir+'TF06Allfree/outdirBNSBu32cores/Constraints170817_posterior_samples.dat', header=0, delimiter=" ")
# # # BuTF19angle = pd.read_csv(outdir+'TF06Angleradio/outdirBNSBu32cores/Constraints170817_posterior_samples.dat', header=0, delimiter=" ")
# # # BuTF19angleGW = pd.read_csv(outdir+'TF06AngleradioGWdistance/outdirBNSBu32cores/Constraints170817_posterior_samples.dat', header=0, delimiter=" ")
# # # BuTF19angleGWmasses = pd.read_csv(outdir+'TF06AngleradioGWdistance+masses/outdirBNSBu32cores/Constraints170817_posterior_samples.dat', header=0, delimiter=" ")

# # # BuTF19['cos_iota'] = np.cos(BuTF19['inclination_EM'])
# # # BuTF19angle['cos_iota'] = np.cos(BuTF19angle['inclination_EM'])
# # # BuTF19angleGW['cos_iota'] = np.cos(BuTF19angleGW['inclination_EM'])
# # # BuTF19angleGWmasses['cos_iota'] = np.cos(BuTF19angleGWmasses['inclination_EM'])

# # # bfBuTF19 = json.load(open(outdir+'TF06Allfree/outdirBNSBu32cores/Constraints170817_bestfit_params.json','r'))
# # # bfBuTF19angle = json.load(open(outdir+'TF06Angleradio/outdirBNSBu32cores/Constraints170817_bestfit_params.json','r'))
# # # bfBuTF19angleGW = json.load(open(outdir+'TF06AngleradioGWdistance/outdirBNSBu32cores/Constraints170817_bestfit_params.json','r'))
# # # bfBuTF19angleGWmasses = json.load(open(outdir+'TF06AngleradioGWdistance+masses/outdirBNSBu32cores/Constraints170817_bestfit_params.json','r'))
# # # bfBuTF19['cos_iota'] = np.cos(bfBuTF19['inclination_EM'])
# # # bfBuTF19angle['cos_iota'] = np.cos(bfBuTF19angle['inclination_EM'])
# # # bfBuTF19angleGW['cos_iota'] = np.cos(bfBuTF19angleGW['inclination_EM'])
# # # bfBuTF19angleGWmasses['cos_iota'] = np.cos(bfBuTF19angleGWmasses['inclination_EM'])

params = ['KNphi', 'log10_mej_dyn', 'log10_mej_wind', 'cos_iota', 'luminosity_distance']
labels = [r'$\phi$', r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
          r'$cos(\iota)$', r'$D_L$']
levels = [0.9545] #crediblity levels to plot
ranges=None

# params = ['log10_mej_dyn', 'log10_mej_wind', 'cos_iota', 'luminosity_distance']
# labels = [r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
#           r'$cos(\iota)$', r'$D_L$']

# fig, ax = plt.subplots(4,4, figsize = (10,10))
# ranges=[[-2.5,-1.5],[-1.7,-1],[0.3,1],[20,60]]
# # fig, ax = plt.subplots(5,5, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)
fig, ax = plt.subplots(5,5, figsize = (10,10))

corner.corner(Bu19, color='blue', fig=fig,
              var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
              levels=levels,
              plot_density=False, plot_datapoints=False, fill_contours=False, 
              bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})
corner.overplot_points(fig=fig, xs=[[bfBu19[k] for k in params]], color='blue', markersize=10)
corner.overplot_lines(fig=fig, xs=[bfBu19[k] for k in params], color='blue', linewidth=0.8)

corner.corner(Bu19angle, color='green', fig=fig,
              var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
              levels=levels,
              plot_density=False, plot_datapoints=False, fill_contours=False, 
              bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})
corner.overplot_points(fig=fig, xs=[[bfBu19angle[k] for k in params]], color='green', markersize=10)
corner.overplot_lines(fig=fig, xs=[bfBu19angle[k] for k in params], color='green', linewidth=0.8)

# corner.corner(Bu19angleGW, color='red', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})
# corner.overplot_points(fig=fig, xs=[[bfBu19angleGW[k] for k in params]], color='red', markersize=10)
# corner.overplot_lines(fig=fig, xs=[bfBu19angleGW[k] for k in params], color='red', linewidth=0.8)


# corner.corner(Bu19angleGWmasses, color='red', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})
# # corner.overplot_points(fig=fig, xs=[bfBu19angleGWmasses[k] for k in params], color='black', markersize=10)
# # corner.overplot_lines(fig=fig, xs=[bfBu19angleGWmasses[k] for k in params], color='black', linewidth=0.8)

# fig20, ax20 = plt.subplots(2,2) #generate another fig

# params = ['cos_iota','luminosity_distance']
# labels = [r'$cos(\iota)$',r'$D_L$']

# corner.corner(Diet20, color='green', fig=fig20,
#               var_names=params, labels = labels, range=[[0.3,1],[20,60]], hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3)

# for j, line in enumerate([2,3]): #overplot the axis you want to overplot
#     for k, row in enumerate([2,3]):
#         over_plot(ax[line, row], ax20[j,k])

# fig20, ax20 = plt.subplots(2,2) #generate another fig

# params = ['log10_mej_dyn', 'log10_mej_wind']
# labels = [r'$\log_{10}M_{ej}^{dyn}$', r'$\log_{10}M_{ej}^{wind}$']

# corner.corner(Andrew, color='green', fig=fig20,
#               var_names=params, labels = labels, range=[[-2.5,-1.5],[-1.7,-1]], hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3)

# for j, line in enumerate([0,1]): #overplot the axis you want to overplot
#     for k, row in enumerate([0,1]):
#         over_plot(ax[line, row], ax20[j,k])

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#             [("green", None), ("blue", None), ("red", None)]]#legend stuff
# ax[0,3].legend(handles = handles, labels = ["GW-only (Dietrich20)", "KN-only (Bu2019)",
#                                             "Bu2019 prior informed by GW+VLBI"],
#                 fancybox= False, framealpha = 1, fontsize = 20)

# fig.suptitle(r'170817 Analyses, $\sigma_{sys} =$ 0.6 mag', fontsize=20)
# fig.savefig(outdir+'Slide_Errsys06Bu19_sklearn.png')


# corner.corner(BuTF19, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#                 bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})
# corner.overplot_points(fig=fig, xs=[bfBuTF19[k] for k in params], color='blue', markersize=10)
# corner.overplot_lines(fig=fig, xs=[bfBuTF19[k] for k in params], color='blue', linewidth=0.8)
              

# corner.corner(BuTF19angle, color='green', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})
# corner.overplot_points(fig=fig, xs=[bfBuTF19angle[k] for k in params], color='green', markersize=10)
# corner.overplot_lines(fig=fig, xs=[bfBuTF19angle[k] for k in params], color='green', linewidth=0.8)


# corner.corner(BuTF19angleGW, color='red', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})
# corner.overplot_points(fig=fig, xs=[bfBuTF19angleGW[k] for k in params], color='red', markersize=10)
# corner.overplot_lines(fig=fig, xs=[bfBuTF19angleGW[k] for k in params], color='red', linewidth=0.8)


# corner.corner(BuTF19angleGWmasses, color='black', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})
# corner.overplot_points(fig=fig, xs=[bfBuTF19angleGWmasses[k] for k in params], color='black', markersize=10)
# corner.overplot_lines(fig=fig, xs=[bfBuTF19angleGWmasses[k] for k in params], color='black', linewidth=0.8)


handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
            [("blue", None), ('green',None)]]#legend stuff
            # [("green", None), ('red',None)]]#legend stuff
# ax[0,4].legend(handles = handles, labels = ['Full prior','Constrained angle'
#                                             # ,'Constrained angle+GW distances'
#                                             # ,'Constrained angle+GW distances and ejecta masses'
#                                             ],
#                 fancybox= False, framealpha = 1, fontsize = 20)
# fig.suptitle(r'KN-only analyses of 170817 with Bu2019lm(sklearn) + tight priors, $\sigma_{sys} =$ 0.6 mag', fontsize=20)

ax[0,4].legend(handles = handles, labels = ['A0.6: Default prior ',
                                            'B0.6: Constrained angle'
                                            # ,'C0.6:Constrained angle+GW distances'
                                            # ,'Constrained angle+GW distances and ejecta masses'
                                            ],
                fancybox= False, framealpha = 1, fontsize = 20)


fig.savefig(outdir+'Errsys06Bu19_sklearn_Constraint_cornerplot_withbestfit3.pdf', format='pdf')
###Figure 14

# ####### Bu2019 with the different lighcurves

outdirKN = '/home/hussenot/H0/kilonovae-H0/170817/'
KN24 = pd.read_csv(outdirKN+'Bu2019full_MWcorrected/1err/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
bfKN24 = json.load(open(outdirKN+'Bu2019full_MWcorrected/1err/outdirBNSBu32cores/AT170817_bestfit_params.json','r'))
KN24errfree = pd.read_csv(outdirKN+'Bu2019full_MWcorrected/freeerr/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
KN24err025 = pd.read_csv(outdirKN+'Bu2019full_MWcorrected/025err/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
bfKN24err025 = json.load(open(outdirKN+'Bu2019full_MWcorrected/025err/outdirBNSBu32cores/AT170817_bestfit_params.json','r'))

KN24['cos_iota'] = np.cos(KN24['inclination_EM'])
bfKN24['cos_iota'] = np.cos(bfKN24['inclination_EM'])
KN24errfree['cos_iota'] = np.cos(KN24errfree['inclination_EM'])
KN24err025['cos_iota'] = np.cos(KN24err025['inclination_EM'])
bfKN24err025['cos_iota'] = np.cos(bfKN24err025['inclination_EM'])


params = ['KNphi', 'log10_mej_dyn', 'log10_mej_wind', 'cos_iota', 'luminosity_distance']
labels = [r'$\phi$', r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
          r'$cos(\iota)$', r'$D_L$']
levels = [0.9545] #crediblity levels to plot
ranges=None

fig, ax = plt.subplots(5,5, figsize = (10,10))
fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

corner.corner(KN24, color='blue', fig=fig,
              var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
              levels=levels,
              plot_density=False, plot_datapoints=False, fill_contours=False, 
              bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

corner.corner(KN24errfree, color='green', fig=fig,
              var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
              levels=levels,
              plot_density=False, plot_datapoints=False, fill_contours=False, 
              bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

corner.corner(KN24err025, color='red', fig=fig,
              var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
              levels=levels,
              plot_density=False, plot_datapoints=False, fill_contours=False, 
              bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})


#Adding more reference lines
# corner.overplot_lines(fig=fig, xs=[None, None, None, np.cos(0.33), None], color='orange', linestyle='dashed')
# corner.overplot_lines(fig=fig, xs=[None, None, None, np.cos(0.44), None], color='orange', linestyle='dashed')
best1=[]
for k in params: best1.append(bfKN24[k])
best025=[]
for k in params: best025.append(bfKN24err025[k])
corner.overplot_lines(fig, best1, color='blue')
corner.overplot_lines(fig, best025, color='red')



handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
            [("blue", None), ("green", None), ("red", None)]]#legend stuff ('orange', 'dashed')
ax[0,4].legend(handles = handles, labels = [r"$\sigma_{\rm sys}= 1 mag$",
                                            r"$\sigma_{\rm sys}= 0.5 mag$",
                                            r"$\sigma_{\rm sys}= 0.25 mag$"],#'VLBI angle constraint'
                fancybox= False, framealpha = 1, fontsize = 20)
# fig.suptitle(r'Bu2019-only Analyses (MW-corrected LC)', fontsize=24)


fig.savefig(outdirKN+'MWcorrected_ErrMargins_cornerplot4.pdf', format='pdf')
###Figure 3

# params = ['KNphi', 'log10_mej_dyn', 'log10_mej_wind', 'cos_iota', 'luminosity_distance']
# labels = [r'$\phi$', r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
#           r'$cos(\iota)$', r'$D_L$']
# levels = [0.9545] #crediblity levels to plot
# ranges=None

# fig, ax = plt.subplots(5,5, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# corner.corner(KN24, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# mask = (KN24['inclination_EM']>0.33)*(KN24['inclination_EM']<0.42)
# sub24 = KN24[mask]

# corner.corner(sub24, color='red', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=10, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#            [("blue", None), ("red", None)]]#legend stuff
# ax[1,4].legend(handles = handles, labels = ["Bu2019-only",
#                                             'Samples compatible with VLBI angles'],
#                fancybox= False, framealpha = 1, fontsize = 20)
# fig.suptitle(r'AT2017gfo Analyses (MW-corrected LC)', fontsize=24)

# fig.savefig(outdir+'MWcorrected_KNanglesubset_cornerplot.png')

###################################
# Exploratory plots, not used in article
###################################


# ######Combining all GW corner plots

# outdir = '/home/hussenot/170817/data_release_170817NMMAPangPaper/MWcorrected_samples/'
# Pang24 = pd.read_csv(outdir+'GW170817-AT2017gfo_0_posterior_samples.dat', header=0, delimiter=" ")
# GWKasen = pd.read_csv(outdir+'GW170817-AT2017gfo_0_posterior_samples_Ka2017_ext_fixed.dat', header=0, delimiter=" ")

outdir = '/home/hussenot/170817/Dietrich20/GW170817_posterior_samples_NRTv2.dat'
Diet20 = pd.read_csv(outdir, header=0, delimiter=" ")
Diet20['inclination'] = np.pi - Diet20['theta_jn']

outdir = '/home/hussenot/170817/data_release_170817NMMAPangPaper/posterior_samples/'
# Pang22GRB = pd.read_csv(outdir+'GW170817-AT2017gfo-GRB170817A_afterglow_posterior_samples.dat', header=0, delimiter=" ")
# Pang22 = pd.read_csv(outdir+'GW170817-AT2017gfo_posterior_samples.dat', header=0, delimiter=" ")

import pickle
path = '/home/hussenot/Downloads/ejecta_table_gp_35389x50_1.0.pickle'
# with open (path, 'rb') as f:
#     data = pickle.load(f)
# Andrew = data.to_pandas()
# Andrew['dyn_mej'][Andrew['dyn_mej']<1E-4] = 1E-4
# Andrew['log10_mej'] = np.log10(Andrew['mej'])
# Andrew['log10_mej_dyn'] = np.log10(Andrew['dyn_mej'])
# Andrew['log10_mej_wind'] = np.log10(Andrew['wind_mej'])
# print(np.min(Andrew['log10_mej_dyn']),np.min(Andrew['log10_mej_wind']))


# #Displaying the cosine of the inclination angle
Diet20['cos_iota'] = np.cos(Diet20['inclination'])
# #print(Diet20['cos_iota'][:5], Diet20['cos_theta_jn'])
# Pang22['cos_iota'] = np.cos(Pang22['inclination_EM'])
# #print(Pang22['cos_iota'][:5], Pang22['cos_theta_jn'])
# Pang22GRB['cos_iota'] = np.cos(Pang22GRB['inclination_EM'])
# Pang24['cos_iota'] = np.cos(Pang24['inclination_EM'])
# GWKasen['cos_iota'] = np.cos(GWKasen['inclination_EM'])
# Andrew['cos_iota'] = np.cos(np.pi-Andrew['theta'])


params = ['KNphi', 'log10_mej_dyn', 'log10_mej_wind', 'cos_iota', 'luminosity_distance',
          'mass_1_source', 'mass_2_source']
labels = [r'$\phi$', r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
          r'$cos(\iota)$', r'$D_L$', r'$M_1 [M_{\odot}]$', r'$M_2 [M_{\odot}]$']
levels = [0.9545] #crediblity levels to plot
ranges = [[40,80], [-2.5, -1.8], [-1.5, -0.9], [0.5, 1], [25, 55], [1.34, 1.7], [1.1, 1.38]] #parameter ranges to plot
# label_kwargs = {"labelpad": 0}

# bins = [         30, #log10_mej_dyn           number of bins in hist
#                  30, #log10_mej_wind
#                  20, #log10_E0
#                  42, #inclination
#                  25, #luminosity_distance
#                  30, #luminosity_distance
# xs = samples[params]
# print(len(xs))

# fig, ax = plt.subplots(7,7, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# corner.corner(Pang24, color='red', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(Pang22, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3)

# corner.corner(Pang22GRB, color='black', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3)

# fig20, ax20 = plt.subplots(4,4) #generate another fig

# params = ['cos_iota', 'luminosity_distance','mass_1_source', 'mass_2_source']
# labels = [r'$cos(\iota)$', r'$D_L$', r'$M_1 [M_{\odot}]$', r'$M_2 [M_{\odot}]$']

# corner.corner(Diet20, color='green', fig=fig20,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3)

# for j, line in enumerate([3,4,5,6]): #overplot the axis you want to overplot
#     for k, row in enumerate([3,4,5,6]):
#         over_plot(ax[line, row], ax20[j,k])

# for axis in fig.get_axes():
#     axis.tick_params(axis = "both", pad = 0)

# #Adding more reference lines
# corner.overplot_lines(fig=fig, xs=[None, None, None, np.cos(0.33), None, None, None], color='orange', linestyle='dashed')
# corner.overplot_lines(fig=fig, xs=[None, None, None, np.cos(0.44), None, None, None], color='orange', linestyle='dashed')
# corner.overplot_lines(fig=fig, xs=[None, None, None, None, None, 1.188*np.power(2,1/5), 1.188*np.power(2,1/5)], color='brown',linestyle='dotted')


# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#            [("green", None), ("blue", None), ("black", None), ("red", None),
#             ('orange', 'dashed'), ('brown','dotted')]]#legend stuff
# ax[1,6].legend(handles = handles, labels = ["Dietrich20 GW", "Pang22 GW+Bu2019", "Pang22 GW+Bu2019+GRB",
#                                             "Pang24 GW+Bu2019 (MW corrected)", 'VLBI angle constraint', '$M_1 = M_2 = M_c * 2^{1/5}$'],
#                fancybox= False, framealpha = 1, fontsize = 20)

# fig.suptitle(r'GW170817+Bu2019 Analyses ($\sigma_{err} = 1 mag$)', fontsize=24)
# fig.savefig(outdir+'Combinedcornerplot.png')

###############3Combining GW, KN et GW+KN

# outdirKN = '/home/hussenot/H0/kilonovae-H0/170817/'
# # # KN22 = pd.read_csv(outdirKN+'Before_MW_correction/Bu2019_freedistance/1mag/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
# KN24 = pd.read_csv(outdirKN+'Bu2019full_MWcorrected/1err/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
# bfKN24 = json.load(open(outdirKN+'Bu2019full_MWcorrected/1err/outdirBNSBu32cores/AT170817_bestfit_params.json','r'))
# KN24errfree = pd.read_csv(outdirKN+'Bu2019full_MWcorrected/freeerr/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
# KN24err025 = pd.read_csv(outdirKN+'Bu2019full_MWcorrected/025err/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
# bfKN24err025 = json.load(open(outdirKN+'Bu2019full_MWcorrected/025err/outdirBNSBu32cores/AT170817_bestfit_params.json','r'))
# # Kasen = pd.read_csv(outdirKN+'Kasen/KN_freeerr/outdirBNSKa32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
# # Kasenfree = pd.read_csv(outdirKN+'Kasen/KN_freeerrjoblib/outdirBNSKa32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
# # Kasen1mag = pd.read_csv(outdirKN+'Kasen/KN_1mag/outdirBNSKa32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
# # Kasendist = pd.read_csv(outdirKN+'AngleDLtight/Ka2017_1mag/outdirBNSKa32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")

# KN24tight =  pd.read_csv(outdirKN+'AngleDLtight/Bu2019_1mag/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
# KN24tight['cos_iota'] = np.cos(KN24tight['inclination_EM'])
# KN24t =  pd.read_csv(outdirKN+'Bu2019full_MWcorrected/tightangle/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
# KN24t['cos_iota'] = np.cos(KN24t['inclination_EM'])


# KN22['cos_iota'] = np.cos(KN22['inclination_EM'])
# #print(np.max(KN22['inclination_EM']))
# KN24['cos_iota'] = np.cos(KN24['inclination_EM'])
# bfKN24['cos_iota'] = np.cos(bfKN24['inclination_EM'])
# KN24errfree['cos_iota'] = np.cos(KN24errfree['inclination_EM'])
# KN24err025['cos_iota'] = np.cos(KN24err025['inclination_EM'])
# bfKN24err025['cos_iota'] = np.cos(bfKN24err025['inclination_EM'])
# #Kasen['cos_iota'] = np.cos(Kasen['inclination_EM']) il y a pas!
# Kasen['cos_iota'] = Kasen['luminosity_distance']*0+1
# print(np.max(Kasen['log10_vej']))



# fig20, ax20 = plt.subplots(2,2) #generate another fig

# params = ['cos_iota', 'luminosity_distance']
# labels = [r'$cos(\iota)$', r'$D_L$']

# corner.corner(Diet20, color='green', fig=fig20,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3)

# params = ['KNphi', 'log10_mej_dyn', 'log10_mej_wind', 'cos_iota', 'luminosity_distance']
# labels = [r'$\phi$', r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
#           r'$cos(\iota)$', r'$D_L$']
# levels = [0.9545] #crediblity levels to plot
# ranges=None

# fig, ax = plt.subplots(5,5, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# corner.corner(KN22, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})


# corner.corner(Pang22, color='red', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# for j, line in enumerate([3,4]): #overplot the axis you want to overplot
#     for k, row in enumerate([3,4]):
#         over_plot(ax[line, row], ax20[j,k])

# for axis in fig.get_axes():
#     axis.tick_params(axis = "both", pad = 0)

# #Adding more reference lines
# corner.overplot_lines(fig=fig, xs=[None, None, None, np.cos(0.33), None], color='orange', linestyle='dashed')
# corner.overplot_lines(fig=fig, xs=[None, None, None, np.cos(0.44), None], color='orange', linestyle='dashed')

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#            [("green", None), ("blue", None), ("red", None),
#             ('orange', 'dashed')]]#legend stuff
# ax[1,4].legend(handles = handles, labels = ["Dietrich20 GW", "Bu2019-only (MW uncorrected)","Pang22 GW+Bu2019 (MW uncorrected)",
#                                             'VLBI angle constraint'],
#                fancybox= False, framealpha = 1, fontsize = 20)

# fig.suptitle(r'170817 Analyses ($\sigma_{err} = 1 mag$), MW-uncorrected LC', fontsize=24)
# fig.savefig(outdir+'MWuncorrected_cornerplot.png')
################
# fig, ax = plt.subplots(5,5, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# params = ['KNphi', 'log10_mej_dyn', 'log10_mej_wind', 'cos_iota', 'luminosity_distance']
# labels = [r'$\phi$', r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
#           r'$cos(\iota)$', r'$D_L$']
# ranges = None#[[40,80], [-2.5, -1.8], [-1.5, -0.9], [0.5, 1], [25, 55]]
# levels = [0.9545] #crediblity levels to plot

# corner.corner(KN24, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(Pang24, color='red', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# fig20, ax20 = plt.subplots(2,2) #generate another fig

# params = ['cos_iota', 'luminosity_distance']
# labels = [r'$cos(\iota)$', r'$D_L$']

# corner.corner(Diet20, color='green', fig=fig20,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3)

# for j, line in enumerate([3,4]): #overplot the axis you want to overplot
#     for k, row in enumerate([3,4]):
#         over_plot(ax[line, row], ax20[j,k])

# for axis in fig.get_axes():
#     axis.tick_params(axis = "both", pad = 0)

# params = ['log10_mej_dyn', 'log10_mej_wind']
# labels = [r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$']

# corner.corner(Andrew, color='green', fig=fig20,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3)

# for j, line in enumerate([1,2]): #overplot the axis you want to overplot
#     for k, row in enumerate([1,2]):
#         over_plot(ax[line, row], ax20[j,k])

# for axis in fig.get_axes():
#     axis.tick_params(axis = "both", pad = 0)

# #Adding more reference lines
# corner.overplot_lines(fig=fig, xs=[None, None, None, np.cos(0.33), None], color='orange', linestyle='dashed')
# corner.overplot_lines(fig=fig, xs=[None, None, None, np.cos(0.44), None], color='orange', linestyle='dashed')

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#             [("green", None), ("blue", None), ("red", None),
#             ('orange', 'dashed')]]#legend stuff
# ax[1,4].legend(handles = handles, labels = ["Dietrich20 GW", "Bu2019-only (MW corrected)","Pang24 GW+Bu2019 (MW corrected)",
#                                             'VLBI angle constraint'],
#                 fancybox= False, framealpha = 1, fontsize = 20)

# fig.suptitle(r'170817 Analyses ($\sigma_{err} = 1 mag$), MW-corrected LC', fontsize=24)
# fig.savefig(outdir+'MWcorrected_cornerplot.png')

# fig, ax = plt.subplots(2,2, figsize=(10,10)) #generate another fig

# params = ['cos_iota', 'luminosity_distance']
# labels = [r'$cos(\iota)$', r'$D_L$']

# corner.corner(Diet20, color='green', fig=fig,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3)

# corner.corner(KN24, color='blue', fig=fig,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})


# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#             [("green", None), ("blue", None)]]#legend stuff
# ax[0,1].legend(handles = handles, labels = ["GW-only analysis of GW170817",
#                                             'KN-only analysis of AT2017gfo (Bu2019)'],
#                 fancybox= False, framealpha = 1, fontsize = 20)

# fig.suptitle(r'GW170817/AT2017gfo Analyses', fontsize=24)
# fig.savefig(outdir+'MWcorrected_angledist.png')

########################
# fig, ax = plt.subplots(4,4, figsize = (16,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# params = ['log10_mej_dyn', 'log10_mej_wind', 'cos_iota', 'luminosity_distance']
# labels = [r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
#           r'$cos(\iota)$', r'$D_L$']
# ranges = [[-2.8, -1.5], [-1.9, -0.8], [0, 1], [25, 60]]
# levels = [0.9545] #crediblity levels to plot

# corner.corner(KN24, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(KN24tight, color='black', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})


# corner.corner(Pang24, color='red', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# fig20, ax20 = plt.subplots(2,2) #generate another fig

# params = ['cos_iota', 'luminosity_distance']
# labels = [r'$cos(\iota)$', r'$D_L$']

# corner.corner(Diet20, color='green', fig=fig20,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3)

# for j, line in enumerate([2,3]): #overplot the axis you want to overplot
#     for k, row in enumerate([2,3]):
#         over_plot(ax[line, row], ax20[j,k])

# for axis in fig.get_axes():
#     axis.tick_params(axis = "both", pad = 0)

# fig20, ax20 = plt.subplots(3,3) #generate another fig

# params = ['log10_mej_dyn', 'log10_mej_wind', 'cos_iota']
# labels = [r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',r'$cos(\iota)$']

# corner.corner(Andrew, color='green', fig=fig20,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3)

# for j, line in enumerate([0,1,2]): #overplot the axis you want to overplot
#     for k, row in enumerate([0,1,2]):
#         over_plot(ax[line, row], ax20[j,k])

# for axis in fig.get_axes():
#     axis.tick_params(axis = "both", pad = 0)

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#             [("green", None), ("blue", None), ("black", None),
#             ('red',None)]]#legend stuff
# ax[0,3].legend(handles = handles, labels = ["Dietrich20 GW", "Bu2019-only (full prior)","Bu2019-only (Constrained angle-DL)",
#                                             'Pang24 GW+Bu2019 joint analysis'],
#                 fancybox= False, framealpha = 1, fontsize = 20)

# fig.suptitle(r'170817 Analyses ($\sigma_{err} = 1 mag$), MW-corrected LC', fontsize=24)
# fig.savefig(outdir+'MWcorrected_cornerplot2.png')
#################


# fig20, ax20 = plt.subplots(2,2) #generate another fig

# params = ['cos_iota', 'luminosity_distance']
# labels = [r'$cos(\iota)$', r'$D_L$']

# corner.corner(Diet20, color='green', fig=fig20,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3)

# params = ['log10_Xlan', 'log10_mej', 'log10_vej', 'cos_iota', 'luminosity_distance']
# labels = [r'$\log_{10}X_{lan}$', r'$\log_{10}M_{ej}$',r'$\log_{10}(v_{ej}/c)$',
#           r'$cos(\iota)$', r'$D_L$']
# levels = [0.9545] #crediblity levels to plot
# ranges = [[-3.7,-3], [-1.2, -2], [-0.8, -0.6], [0.5, 1], [20, 55]] #parameter ranges to plot


# fig, ax = plt.subplots(5,5, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)


# corner.corner(GWKasen, color='red', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# ranges=None
# figKasen, axKasen = plt.subplots(4,4)
# params = ['log10_Xlan', 'log10_mej', 'log10_vej', 'luminosity_distance']
# labels = [r'$\log_{10}X_{lan}$', r'$\log_{10}M_{ej}$',r'$\log_{10}(v_{ej}/c)$',
#           r'$D_L$']

# corner.corner(Kasen, color='blue', fig=figKasen,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# for j, line in enumerate([0,1,2,4]): #overplot the axis you want to overplot
#     for k, row in enumerate([0,1,2,4]):
#         over_plot(ax[line, row], axKasen[j,k])

# for j, line in enumerate([3,4]): #overplot the axis you want to overplot
#     for k, row in enumerate([3,4]):
#         over_plot(ax[line, row], ax20[j,k])

# for axis in fig.get_axes():
#     axis.tick_params(axis = "both", pad = 0)

# #Adding more reference lines
# corner.overplot_lines(fig=fig, xs=[None, None, None, np.cos(0.33), None], color='orange', linestyle='dashed')
# corner.overplot_lines(fig=fig, xs=[None, None, None, np.cos(0.44), None], color='orange', linestyle='dashed')

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#             [("green", None), ("blue", None), ("red", None),
#             ('orange', 'dashed')]]#legend stuff
# ax[1,4].legend(handles = handles, labels = ["Dietrich20 GW", "Kasen2017-only (MW corrected)","GW+Kasen2017 (MW corrected)",
#                                             'VLBI angle constraint'],
#                 fancybox= False, framealpha = 1, fontsize = 20)

# fig.suptitle(r'170817 Analyses ($\sigma_{err} = 1 mag$), MW-corrected LC', fontsize=24)
# fig.savefig(outdir+'Kasen_corrected_cornerplot.png')


####################################

# fig, ax = plt.subplots(5,5, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# corner.corner(Pang24, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# mask = (Pang24['inclination_EM']>0.33)*(Pang24['inclination_EM']<0.42)
# sub24 = Pang24[mask]

# corner.corner(sub24, color='red', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=10, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# fig20, ax20 = plt.subplots(2,2) #generate another fig

# params = ['cos_iota', 'luminosity_distance']
# labels = [r'$cos(\iota)$', r'$D_L$']

# corner.corner(Diet20, color='green', fig=fig20,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3)

# for j, line in enumerate([3,4]): #overplot the axis you want to overplot
#     for k, row in enumerate([3,4]):
#         over_plot(ax[line, row], ax20[j,k])

# for axis in fig.get_axes():
#     axis.tick_params(axis = "both", pad = 0)

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#            [("blue", None), ("red", None)]]#legend stuff
# ax[1,4].legend(handles = handles, labels = ["Pang24 GW+Bu2019",
#                                             'Samples compatible with VLBI angles'],
#                fancybox= False, framealpha = 1, fontsize = 20)
# fig.suptitle(r'GW170817 Analyses (MW-corrected LC)', fontsize=24)

# fig.savefig(outdir+'MWcorrected_anglesubset_cornerplot.png')

# #Kasen anglesubset plot

# fig, ax = plt.subplots(5,5, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# params = ['log10_Xlan', 'log10_mej', 'log10_vej', 'cos_iota','luminosity_distance']
# labels = [r'$\log_{10}X_{lan}$', r'$\log_{10}M_{ej}$',r'$\log_{10}(v_{ej}/c)$',
#           r'$cos(\iota)$', r'$D_L$']

# corner.corner(GWKasen, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# mask = (GWKasen['inclination_EM']>0.33)*(GWKasen['inclination_EM']<0.42)
# sub24 = GWKasen[mask]

# corner.corner(sub24, color='red', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=10, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# fig20, ax20 = plt.subplots(2,2) #generate another fig

# params = ['cos_iota', 'luminosity_distance']
# labels = [r'$cos(\iota)$', r'$D_L$']

# corner.corner(Diet20, color='green', fig=fig20,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3)

# for j, line in enumerate([3,4]): #overplot the axis you want to overplot
#     for k, row in enumerate([3,4]):
#         over_plot(ax[line, row], ax20[j,k])

# for axis in fig.get_axes():
#     axis.tick_params(axis = "both", pad = 0)

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#            [("blue", None), ("red", None)]]#legend stuff
# ax[1,4].legend(handles = handles, labels = ["Pang24 GW+Kasen2017",
#                                             'Samples compatible with VLBI angles'],
#                fancybox= False, framealpha = 1, fontsize = 20)
# fig.suptitle(r'GW170817 Analyses (MW-corrected LC)', fontsize=24)

# fig.savefig(outdir+'MWcorrected_Kasenanglesubset_cornerplot.png')
##############
# fig, ax = plt.subplots(6,6, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# params = ['mej', 'dyn_mej', 'wind_mej', 'm1','m2', 'cos_iota']#lambdatilde
# labels = [r'$M_{ej}$', r'$M_{ej}^{dyn}$',r'$M_{ej}^{wind}$',
#           r'$M_1$', r'$M_2$', r'$cos(\iota)$']#r'$\tilde{\Lambda}$'
# ranges=None

# corner.corner(Andrew, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels, #show_titles=True,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# fig20, ax20 = plt.subplots(3,3) #generate another fig

# params = ['mass_1_source', 'mass_2_source', 'cos_iota']#'lambda_tilde'
# labels = [r'$M_1$', r'$M_2$',r'$cos(\iota)$']

# corner.corner(Diet20, color='green', fig=fig20,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, alpha=0.8)

# for j, line in enumerate([3,4,5]): #overplot the axis you want to overplot
#     for k, row in enumerate([3,4,5]):
#         over_plot(ax[line, row], ax20[j,k])

# for axis in fig.get_axes():
#     axis.tick_params(axis = "both", pad = 0)

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#            [("blue", None), ("green", None)]]#legend stuff
# ax[1,4].legend(handles = handles, labels = ["Andrew",
#                                             'Dietrich20'],
#                fancybox= False, framealpha = 1, fontsize = 20)
# fig.suptitle(r'GW170817 Analyses', fontsize=24)

# fig.savefig(outdir+'Andrew_cornerplot.png')

################

# fig, ax = plt.subplots(5,5, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# params = ['KNphi', 'log10_mej_dyn', 'log10_mej_wind', 'cos_iota', 'luminosity_distance']
# labels = [r'$\phi$', r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
#           r'$cos(\iota)$', r'$D_L$']
# ranges = None#[[40,80], [-2.5, -1.8], [-1.5, -0.9], [0.5, 1], [25, 55]]
# levels = [0.9545] #crediblity levels to plot

# corner.corner(KN24, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(KN24t, color='green', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(KN24tight, color='red', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#            [("blue", None), ('green',None),("red", None)]]#legend stuff
# ax[1,4].legend(handles = handles, labels = ["Full prior", 'Constrained angle',
#                                             'Constrained angle+distance'],
#                fancybox= False, framealpha = 1, fontsize = 20)
# fig.suptitle(r'Bu2019lm KN-only analyses with different prior constraints', fontsize=24)

# fig.savefig(outdir+'Constraint19_cornerplot.png')
# ################
# Bu22 =  pd.read_csv(outdirKN+'Bu2022Ye/KNfreeerr/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
# Bu22['cos_iota'] = np.cos(Bu22['inclination_EM'])
# Bu22t =  pd.read_csv(outdirKN+'Bu2022Ye/KNfreeerr_tightangle/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
# Bu22t['cos_iota'] = np.cos(Bu22t['inclination_EM'])
# Bu22t2 =  pd.read_csv(outdirKN+'AngleDLtight/Bu2022_1mag/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
# Bu22t2['cos_iota'] = np.cos(Bu22t2['inclination_EM'])

# fig, ax = plt.subplots(7,7, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# params = ['log10_mej_dyn', 'vej_dyn', 'Yedyn', 'log10_mej_wind', 'vej_wind','cos_iota', 'luminosity_distance']
# labels = [r'$\log_{10}M_{ej}^{dyn}$',r'$v_{ej}^{dyn}$',r'$Y_e^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',r'$v_{ej}^{wind}$',
#           r'$cos(\iota)$', r'$D_L$']
# ranges = None#[[40,80], [-2.5, -1.8], [-1.5, -0.9], [0.5, 1], [25, 55]]
# levels = [0.9545] #crediblity levels to plot

# corner.corner(Bu22, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(Bu22t, color='green', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(Bu22t2, color='red', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#             [("blue", None), ('green',None),("red", None)]]#legend stuff
# ax[1,6].legend(handles = handles, labels = ["Full prior", 'Constrained angle',
#                                             'Constrained angle+distance'],
#                 fancybox= False, framealpha = 1, fontsize = 20)
# fig.suptitle(r'Bu2022Ye KN-only analyses with different prior constraints', fontsize=24)

# fig.savefig(outdir+'Constraint22_cornerplot.png')

####
# fig, ax = plt.subplots(3,3, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# params = ['log10_mej', 'log10_mej_dyn', 'log10_mej_wind']
# labels = [r'$\log_{10}M_{ej}$',r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$']
# ranges=None

# corner.corner(Andrew, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels, show_titles=True,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# fig.suptitle(r'Andrew extrapolated ejecta from GW170817 Dietrich20 run', fontsize=24)

# fig.savefig(outdir+'Andrew_ejecta_log.png')

#####
# figKasen, axKasen = plt.subplots(4,4, figsize=(15,15))
# params = ['log10_Xlan', 'log10_mej', 'log10_vej', 'luminosity_distance']
# labels = [r'$\log_{10}X_{lan}$', r'$\log_{10}M_{ej}$',r'$\log_{10}(v_{ej}/c)$',
#           r'$D_L$']

# corner.corner(Kasen, color='red', fig=figKasen,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(Kasen1mag, color='blue', fig=figKasen,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(Kasenfree, color='green', fig=figKasen,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(Kasendist, color='black', fig=figKasen,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels, show_titles=True,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#             [("red", None), ("blue", None), ("green", None),("black", None)]]#legend stuff
# axKasen[1,3].legend(handles = handles, labels = [r"Kasen (old) free $\rightarrow 0.75 mag$ ", "Kasen 1 mag",
#                                             r"Kasen free $\rightarrow 0.84 mag$", "Kasen 1 mag tight distance prior"],
#                 fancybox= False, framealpha = 1, fontsize = 20)

# axKasen[0,2].legend(labels=[r"From GW $\log_{10}M_{ej}$ \sim -1.48^{+0.20}_{-0.08}"])

# figKasen.suptitle(r'170817 Analyses Kasen2017-only, MW-corrected LC', fontsize=24)
# figKasen.savefig(outdir+'Kasenjoblib_cornerplot.png')
####################
# figKasen, axKasen = plt.subplots(4,4, figsize=(12,12))
# params = ['log10_Xlan', 'log10_mej', 'log10_vej', 'luminosity_distance']
# labels = [r'$\log_{10}X_{lan}$', r'$\log_{10}M_{ej}$',r'$\log_{10}(v_{ej}/c)$',
#           r'$D_L$']

# corner.corner(GWKasen, color='red', fig=figKasen,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(Kasendist, color='black', fig=figKasen,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})


# fig20, ax20 = plt.subplots(2,2) #generate another fig

# params = ['luminosity_distance','cos_iota']
# labels = [r'$D_L$',r'$cos(\iota)$']

# corner.corner(Diet20, color='green', fig=fig20,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3)

# for j, line in enumerate([3]): #overplot the axis you want to overplot
#     for k, row in enumerate([3]):
#         over_plot(axKasen[line, row], ax20[j,k])

# fig20, ax20 = plt.subplots(2,2) #generate another fig

# params = ['log10_mej', 'log10_mej']
# labels = [r'$\log_{10}M_{ej}$', r'$\log_{10}M_{ej}$']

# corner.corner(Andrew, color='green', fig=fig20,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3)

# for j, line in enumerate([1]): #overplot the axis you want to overplot
#     for k, row in enumerate([1]):
#         over_plot(axKasen[line, row], ax20[j,k])

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#             [("green", None), ("black", None), ("red", None)]]#legend stuff
# axKasen[0,3].legend(handles = handles, labels = ["Dietrich20 GW", "Ka2017-only (Constrained DL)",
#                                             "Pang24 GW+Ka2017 joint analysis"],
#                 fancybox= False, framealpha = 1, fontsize = 20)


# figKasen.suptitle(r'170817 Analyses ($\sigma_{err} = 1 mag$), MW-corrected LC', fontsize=24)
# figKasen.savefig(outdir+'Kasenjoblib_cornerplotNicolas.png')
#######



# dir1 = outdirKN+'Bu2019full_MWcorrected/'
# KNri = pd.read_csv(dir1+'1errtightangle_ri/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
# KNri['cos_iota'] = np.cos(KNri['inclination_EM'])
# KNgriz = pd.read_csv(dir1+'1errtightangle_griz/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
# KNgrizy = pd.read_csv(dir1+'1errtightangle_grizy/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
# KNJHK = pd.read_csv(dir1+'1errtightangle_JHK/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")
# KNall = pd.read_csv(dir1+'1errtightangle_all/outdirBNSBu32cores/AT170817_posterior_samples.dat', header=0, delimiter=" ")


# params = ['KNphi', 'log10_mej_dyn', 'log10_mej_wind', 'luminosity_distance']
# labels = [r'$\phi$', r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
#           r'$D_L$']
# levels = [0.9545] #crediblity levels to plot
# ranges=None

# # params = ['log10_mej_dyn', 'vej_dyn', 'Yedyn', 'log10_mej_wind', 'vej_wind','cos_iota', 'luminosity_distance']
# # labels = [r'$\log_{10}M_{ej}^{dyn}$',r'$v_{ej}^{dyn}$',r'$Y_e^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',r'$v_{ej}^{wind}$',
# #           r'$cos(\iota)$', r'$D_L$']

# # params = ['log10_Xlan', 'log10_mej', 'log10_vej', 'luminosity_distance']
# # labels = [r'$\log_{10}X_{lan}$', r'$\log_{10}M_{ej}$',r'$\log_{10}(v_{ej}/c)$',
# #           r'$D_L$']

# fig, ax = plt.subplots(4,4, figsize = (10,10))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# # corner.corner(KNri, color='blue', fig=fig,
# #               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
# #               levels=levels,
# #               plot_density=False, plot_datapoints=False, fill_contours=False, 
# #               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# # corner.corner(KNgriz, color='green', fig=fig,
# #               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
# #               levels=levels,
# #               plot_density=False, plot_datapoints=False, fill_contours=False, 
# #               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(KNgrizy, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(KNJHK, color='green', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(KNall, color='black', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# # corner.corner(KN24t, color='red', fig=fig,
# #               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
# #               levels=levels,
# #               plot_density=False, plot_datapoints=False, fill_contours=False, 
# #               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# # fig20, ax20 = plt.subplots(2,2) #generate another fig

# # params = ['cos_iota', 'luminosity_distance']
# # labels = [r'$cos(\iota)$', r'$D_L$']

# # corner.corner(Diet20, color='green', fig=fig20,
# #               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
# #               levels=levels,
# #               plot_density=False, plot_datapoints=False, fill_contours=False, 
# #               bins=50, smooth=0.9, max_n_ticks=3)

# # for j, line in enumerate([3,4]): #overplot the axis you want to overplot
# #     for k, row in enumerate([3,4]):
# #         over_plot(ax[line, row], ax20[j,k])

# # for axis in fig.get_axes():
# #     axis.tick_params(axis = "both", pad = 0)

# # #Adding more reference lines
# # corner.overplot_lines(fig=fig, xs=[None, None, None, np.cos(0.33), None], color='orange', linestyle='dashed')
# # corner.overplot_lines(fig=fig, xs=[None, None, None, np.cos(0.44), None], color='orange', linestyle='dashed')

# # handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
# #             [("blue", None),("green", None),("black", None),("red", None)]]#legend stuff
# # ax[1,3].legend(handles = handles, labels = [r"$\sigma_{err}= 1 mag$ grizy bands", r"$\sigma_{err}= 1 mag$ JHK bands",
# #                                             r"$\sigma_{err}= 1 mag$ All filters",r"$\sigma_{err}= 0.5 mag$ All filters"],
# #                 fancybox= False, framealpha = 1, fontsize = 20)
# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#             [("blue", None),("green", None),("black", None)]]#legend stuff
# ax[1,3].legend(handles = handles, labels = [r"grizy", r"JHK",
#                                             r"grizyJHK"],
#                 fancybox= False, framealpha = 1, fontsize = 24)
# # fig.suptitle(r'AT2017gfo Analyses Bu2019lm-only, Tight angle prior', fontsize=20)


# fig.savefig(dir1+'1errtightangleFiltervariation2.pdf',format='pdf')
#################################

# fig, ax = plt.subplots(3,3, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# params = ['log10_mej_dyn', 'log10_mej_wind','cos_iota']
# labels = [r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
#           r'$cos(\iota)$']

# corner.corner(Andrew, color='blue', fig=fig,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#                levels=levels, show_titles=True, title_quantiles=[0.16, 0.5, 0.84], #[0.025, 0.5, 0.975] 95%
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# # Andrewtight = Andrew[(Andrew['cos_iota']>0.906)&(Andrew['cos_iota']<0.946)]

# # corner.corner(Andrewtight, color='green', fig=fig,
# #               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
# #               levels=levels, show_titles=True,
# #               plot_density=False, plot_datapoints=False, fill_contours=False, 
# #               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# #Adding more reference lines
# corner.overplot_lines(fig=fig, xs=[-2.6, -1.9, None], color='orange', linestyle='dashed')
# corner.overplot_lines(fig=fig, xs=[-1.5, -1.2, None], color='orange', linestyle='dashed')


# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#             [("blue", None), ("green", None)]]#legend stuff
# ax[0,2].legend(handles = handles, labels = ["Andrew",
#                                             'Andrew with radio angle'],
#                 fancybox= False, framealpha = 1, fontsize = 20)
# fig.suptitle(r'GW170817 Analyses', fontsize=24)

# fig.savefig(outdir+'Andrew_tightangle68.png')

# fig, ax = plt.subplots(2,2, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# params = ['cos_iota', 'luminosity_distance']
# labels = [r'$cos(\iota)$', r'$D_L$']

# corner.corner(Diet20, color='blue', fig=fig,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels, #show_titles=True,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# Diet20tight = Diet20[(Diet20['cos_iota']>0.906)&(Diet20['cos_iota']<0.946)]

# corner.corner(Diet20tight, color='green', fig=fig,
#               var_names=params, labels = labels, range=None, hist_kwargs={'density':True},
#               levels=levels, show_titles=True,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})


# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#             [("blue", None), ("green", None)]]#legend stuff
# ax[0,1].legend(handles = handles, labels = ["Diet20",
#                                             'Diet20 with radio angle'],
#                 fancybox= False, framealpha = 1, fontsize = 20)
# fig.suptitle(r'GW170817 Analyses', fontsize=24)

# fig.savefig(outdir+'Diet20_tightangle.png')



# #Exploring the AT2017gfo B0.6 bimodality
# Bu19angleA = Bu19angle[Bu19angle['luminosity_distance']<47]
# Bu19angleB = Bu19angle[Bu19angle['luminosity_distance']>47]

# corner.corner(Bu19angleA, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels, 
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(Bu19angleB, color='red', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels, show_titles=True, title_quantiles=[0.025, 0.5, 0.975], #[0.025, 0.5, 0.975] 95%
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# fig.savefig(outdir+'Errsys06Bu19_sklearn_Constraint_cornerplot_bimodality2.png')


# corner.corner(Bu19, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#                 bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.overplot_points(fig=fig, xs=[bfBu19[k] for k in params], color='blue', markersize=10)
# corner.overplot_lines(fig=fig, xs=[bfBu19[k] for k in params], color='blue', linewidth=0.8)

# corner.corner(BuTF19, color='red', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.overplot_points(fig=fig, xs=[bfBuTF19[k] for k in params], color='red', markersize=10)
# corner.overplot_lines(fig=fig, xs=[bfBuTF19[k] for k in params], color='red', linewidth=0.8)

# corner.overplot_lines(fig=fig, xs=[None, None, None, np.cos(0.33), None], color='black', linestyle='dashed')
# corner.overplot_lines(fig=fig, xs=[None, None, None, np.cos(0.42), None], color='black', linestyle='dashed')
# # corner.overplot_lines(fig=fig, xs=[None, None, None, None, 39.4], color='black', linestyle='dashed')
# # corner.overplot_lines(fig=fig, xs=[None, None, None, None, 47.4], color='black', linestyle='dashed')
# # corner.overplot_lines(fig=fig, xs=[None, -2.6, None, None, None], color='black', linestyle='dashed')
# # corner.overplot_lines(fig=fig, xs=[None, -1.7, None, None, None], color='black', linestyle='dashed')
# # corner.overplot_lines(fig=fig, xs=[None, None, -1.9, None, None], color='black', linestyle='dashed')
# # corner.overplot_lines(fig=fig, xs=[None, None, -1.2, None, None], color='black', linestyle='dashed')

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#             [("blue", None), ('red',None), ('black','dashed')]]#legend stuff
# ax[0,4].legend(handles = handles, labels = ['Bu2019lm sklearn', 'Bu2019lm tensorflow'
#                                             ,'Angle constraints (VLBI)'
#                                             ],
#                 fancybox= False, framealpha = 1, fontsize = 18)
# fig.suptitle(r'KN-only analyses of 170817 full priors, $\sigma_{sys} =$ 0.6 mag', fontsize=20)


# fig.savefig(outdir+'Errsys06Bu19_sklearn_tf_cornerplot1.png')

###################################
outdir = '/home/hussenot/H0/kilonovae-H0/170817/Bu2023Ye/'
# Bu23 = pd.read_csv(outdir+'06Allfree/outdirBNSBu32cores/Constraints170817_posterior_samples.dat', header=0, delimiter=" ")
# Bu23angle = pd.read_csv(outdir+'06Angleradio/outdirBNSBu32cores/Constraints170817_posterior_samples.dat', header=0, delimiter=" ")
# Bu23angleGW = pd.read_csv(outdir+'06AngleradioGWdistance/outdirBNSBu32cores/Constraints170817_posterior_samples.dat', header=0, delimiter=" ")
# Bu23angleGWmasses = pd.read_csv(outdir+'06AngleradioGWdistance+masses/outdirBNSBu32cores/Constraints170817_posterior_samples.dat', header=0, delimiter=" ")

# Bu23['cos_iota'] = np.cos(Bu23['inclination_EM'])
# Bu23angle['cos_iota'] = np.cos(Bu23angle['inclination_EM'])
# Bu23angleGW['cos_iota'] = np.cos(Bu23angleGW['inclination_EM'])
# Bu23angleGWmasses['cos_iota'] = np.cos(Bu23angleGWmasses['inclination_EM'])

# bfBu23 = json.load(open(outdir+'06Allfree/outdirBNSBu32cores/Constraints170817_bestfit_params.json','r'))
# bfBu23angle = json.load(open(outdir+'06Angleradio/outdirBNSBu32cores/Constraints170817_bestfit_params.json','r'))
# bfBu23angleGW = json.load(open(outdir+'06AngleradioGWdistance/outdirBNSBu32cores/Constraints170817_bestfit_params.json','r'))
# bfBu23angleGWmasses = json.load(open(outdir+'06AngleradioGWdistance+masses/outdirBNSBu32cores/Constraints170817_bestfit_params.json','r'))
# bfBu23['cos_iota'] = np.cos(bfBu23['inclination_EM'])
# bfBu23angle['cos_iota'] = np.cos(bfBu23angle['inclination_EM'])
# bfBu23angleGW['cos_iota'] = np.cos(bfBu23angleGW['inclination_EM'])
# bfBu23angleGWmasses['cos_iota'] = np.cos(bfBu23angleGWmasses['inclination_EM'])


# params = ['log10_mej_dyn', #'vej_dyn', 'Yedyn', 
#            'log10_mej_wind', #'vej_wind', 'Yewind',
#           'cos_iota', 'luminosity_distance']
# labels = [r'$\log_{10}M_{ej}^{dyn}$', #r'$V_{ej}^{dyn}$', r'$Y_e^{dyn}$',
#           r'$\log_{10}M_{ej}^{wind}$', #r'$V_{ej}^{wind}$', r'$Y_e^{wind}$',
#           r'$cos(\iota)$', r'$D_L$']
# levels = [0.9545] #crediblity levels to plot
# ranges=None

# fig, ax = plt.subplots(4,4, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# corner.corner(Bu23, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})
# corner.overplot_points(fig=fig, xs=[bfBu23[k] for k in params], color='blue', markersize=10)
# corner.overplot_lines(fig=fig, xs=[bfBu23[k] for k in params], color='blue', linewidth=0.8)

# corner.corner(Bu23angle, color='green', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels,
#               plot_density=False, plot_datapoints=False, fill_contours=False, 
#               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})
# corner.overplot_points(fig=fig, xs=[bfBu23angle[k] for k in params], color='green', markersize=10)
# corner.overplot_lines(fig=fig, xs=[bfBu23angle[k] for k in params], color='green', linewidth=0.8)

# # corner.corner(Bu23angleGW, color='red', fig=fig,
# #               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
# #               levels=levels,
# #               plot_density=False, plot_datapoints=False, fill_contours=False, 
# #               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})
# # corner.overplot_points(fig=fig, xs=[bfBu23angleGW[k] for k in params], color='red', markersize=10)
# # corner.overplot_lines(fig=fig, xs=[bfBu23angleGW[k] for k in params], color='red', linewidth=0.8)


# # corner.corner(Bu23angleGWmasses, color='black', fig=fig,
# #               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
# #               levels=levels,
# #               plot_density=False, plot_datapoints=False, fill_contours=False, 
# #               bins=50, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})
# # corner.overplot_points(fig=fig, xs=[bfBu23angleGWmasses[k] for k in params], color='black', markersize=10)
# # corner.overplot_lines(fig=fig, xs=[bfBu23angleGWmasses[k] for k in params], color='black', linewidth=0.8)


# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#             [("blue", None), ('green',None)]]#legend stuff
#             # [("green", None), ('red',None), ('black',None)]]#legend stuff
# ax[0,3].legend(handles = handles, labels = ['Full prior','Constrained angle'
#                                             # ,'Constrained angle+GW distances'
#                                             # ,'Constrained angle+GW distances and ejecta masses'
#                                             ],
#                 fancybox= False, framealpha = 1, fontsize = 20)
# fig.suptitle(r'KN-only analyses of 170817 with Bu2023Ye(tensorflow) + tight priors, $\sigma_{sys} =$ 0.6 mag', fontsize=20)

# fig.savefig(outdir+'Errsys06Bu23_sklearn_Constraint_cornerplot_withbestfit1_cropped.png')

########################
outdir = '/home/hussenot/H0/kilonovae-H0/170817/As2020Bu2019/'
# Bu19 = pd.read_csv(outdir+'Bu2019/outdirBNSBu32cores/170817in14days_posterior_samples.dat', header=0, delimiter=" ")
# Bu19 = pd.read_csv(outdir+'Bu2019distanceasZP/outdirBNSBu32cores/170817in14days_posterior_samples.dat', header=0, delimiter=" ")

# Bu19['KNtheta'] = 180*(Bu19['inclination_EM'])/np.pi

# outdir = '/home/hussenot/170817/Coughlin2020/Bu2019lm/'
# Bu192020 = pd.read_csv(outdir+'u_g_r_i_z_y_J_H_K/0_14/GW170817/1.00/posterior_samples.dat', header=0, delimiter=" ")
# Bu192020['log10_mej_dyn'] = np.log10(Bu192020['mej_dyn'])
# Bu192020['log10_mej_wind'] = np.log10(Bu192020['mej_wind'])
# Bu192020['luminosity_distance'] = 40.7*np.power(10, 0.2*(Bu192020['ZP']))



# params = ['timeshift', 'log10_mej_dyn', 'log10_mej_wind', 'KNphi', 'KNtheta', 'luminosity_distance']
# labels = ['timeshift', r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$', r'$\phi$',
#           r'$\theta [deg]$', r'$D_L$']
# levels = [0.9]
# ranges=None

# fig, ax = plt.subplots(6,6, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# corner.corner(Bu192020, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels, show_titles=True,
#               plot_density=True, plot_datapoints=False, fill_contours=False, 
#               bins=20, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(Bu19, color='green', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels, show_titles=True,
#               plot_density=True, plot_datapoints=False, fill_contours=False, 
#               bins=20, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#             [("blue", None), ('green',None)]]#legend stuff
# ax[0,5].legend(handles = handles, labels = ['Coughlin 2020','Remade with NMMA,same lightcurve same distanceprior'
#                                             ],
#                 fancybox= False, framealpha = 1, fontsize = 20)
# fig.suptitle(r'170817 with Bu2019lm(sklearn) , $\sigma_{sys} =$ 1 mag', fontsize=20)

# fig.savefig(outdir+'As2020test4.png')
# outdir = '/home/hussenot/H0/kilonovae-H0/170817/As2020Kasen/'
# Ka = pd.read_csv(outdir+'Ka2017/outdirBNSKa32cores/170817in14days_posterior_samples.dat', header=0, delimiter=" ")

# outdir = '/home/hussenot/170817/Coughlin2020/Ka2017/'
# Ka1 = pd.read_csv(outdir+'u_g_r_i_z_y_J_H_K/0_14/ejecta/GW170817/1.00/posterior_samples.dat', header=0, delimiter=" ")
# Ka1=Ka1[Ka1['Xlan']!=0]
# Ka1['log10_mej'] = np.log10(Ka1['mej'])
# Ka1['log10_vej'] = np.log10(Ka1['vej'])
# Ka1['log10_Xlan'] = np.log10(Ka1['Xlan'])


# params = ['timeshift', 'log10_mej', 'log10_vej', 'log10_Xlan']
# labels = ['timeshift', r'$\log_{10}M_{ej}$',r'$\log_{10}v_{ej}$', r'$\log_{10}X_{lan}$']
# levels = [0.9]
# ranges=None

# fig, ax = plt.subplots(4,4, figsize = (13,14))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# corner.corner(Ka1, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels, show_titles=True,
#               plot_density=True, plot_datapoints=False, fill_contours=False, 
#               bins=20, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.corner(Ka, color='green', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels, show_titles=True,
#               plot_density=True, plot_datapoints=False, fill_contours=False, 
#               bins=20, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#             [("blue", None), ('green',None)]]#legend stuff
# ax[0,3].legend(handles = handles, labels = ['Coughlin 2020','Remade'
#                                             ],
#                 fancybox= False, framealpha = 1, fontsize = 20)
# fig.suptitle(r'KN-only analyses of 170817 with Bu2019lm(sklearn) , $\sigma_{sys} =$ 1 mag', fontsize=20)

# fig.savefig(outdir+'As2020test2.png')

############
# outdir = '/home/hussenot/H0/kilonovae-H0/Injection_Recovery_IterationsVariation/'
# Bu19 = pd.read_csv(outdir+'InjectionBaseLightcurve1/1perday_1/grizyJHK/outdirBNSBu32cores/InjectionRecoveryIterations_posterior_samples.dat', header=0, delimiter=" ")
# Bu19['cos_iota'] = np.cos(Bu19['inclination_EM'])

# params = ['KNphi', 'log10_mej_dyn', 'log10_mej_wind', 'cos_iota', 'luminosity_distance']
# labels = [r'$\phi$', r'$\log_{10}M_{ej}^{dyn}$',r'$\log_{10}M_{ej}^{wind}$',
#           r'$cos(\iota)$', r'$D_L$']
# levels = [0.9545] #crediblity levels to plot
# ranges=None

# fig, ax = plt.subplots(5,5, figsize = (10,10))
# fig.subplots_adjust(wspace = 0.1, hspace = 0.1)

# corner.corner(Bu19, color='blue', fig=fig,
#               var_names=params, labels = labels, range=ranges, hist_kwargs={'density':True},
#               levels=levels, show_titles=False,
#               plot_density=True, plot_datapoints=False, fill_contours=False, 
#               bins=20, smooth=0.9, max_n_ticks=3, label_kwargs={'fontsize': 16})

# corner.overplot_lines(fig=fig, xs=[60, -2, np.log10(0.05), 0.8, 40], color='red')

# handles = [plt.plot([],[], color = c, linestyle = l)[0] for (c,l) in
#             [("red", None), ('blue',None)]]#legend stuff
# ax[0,4].legend(handles = handles, labels = ['Injected parameters','Recovered posterior'
#                                             ],
#                 fancybox= False, framealpha = 1, fontsize = 24)
# # fig.suptitle(r'Injection Recovery analysis with Bu2019lm(sklearn) , $\sigma_{sys} =$ 1 mag', fontsize=20)

# fig.savefig(outdir+'RecoveryLightcurve1.png')