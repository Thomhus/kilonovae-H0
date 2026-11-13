## kilonovae-H0
KN analyses of AT2017gfo and simulated events
(initial project focused on distance posteriors, with the eventual goal of estimating H0 from a sample of kilonovae; expanded to benchmarking parameter estimation on all KN parameters)

# Data for **Benchmarking the expected performance of Bayesian parameter inference on Kilonovae** [arXiv](https://arxiv.org/abs/2505.21392)

## Datasets and corresponding parameter inference results

* **AT2017gfo** Lightcurve at 170817/AT2017gfoMWcorrected.dat, resulting from extinction correction in 170817/extinction170817.py
	Results with prior sets:
	* **A1** 170817/Bu2019full_MWcorrected/1err
	* **B1** 170817/Bu2019full_MWcorrected/1errtightangle_all
	* **C1** 170817/Errsys+constraints/1AngleradioGWdistance
	* **D1** 170817/Errsys+constraints/1AngleradioGWdistance+masses
	* **A0.6** 170817/Errsys+constraints/06Allfree
	* **B0.6** 170817/Errsys+constraints/06Angleradio
	* **C0.6** 170817/Errsys+constraints/06AngleradioGWdistance
	* **D0.6** 170817/Errsys+constraints/06AngleradioGWdistance+masses
	
	* **A'1** 170817/Bu2025MLP/1Default
	* **B'1** 170817/Bu2025MLP/1Angleradio
	* **C'1** 170817/Bu2025MLP/1AngleradioGWdistance
	* **D'1** 170817/Bu2025MLP/1AngleradioGWdistance+masses
	* **A'06** 170817/Bu2025MLP/06Default
	* **B'06** 170817/Bu2025MLP/06Angleradio
	* **C'06** 170817/Bu2025MLP/06AngleradioGWdistance
	* **D'06** 170817/Bu2025MLP/06AngleradioGWdistance+masses
	
* **sim17** Lightcurves and results with different cadences and filter sets in section lcsimu/

* **toymodel** Lightcurve and results in lcsimu/varying_sigma_sus_truecadence_0.5noise

* **ManySims** Lightcurves and results (22 different injections, each declined in 20 resampled lightcurves) in section Injection_Recovery_IterationsVariation/

See scramble.py for the generation of resampled lightcurves

* **25MLPSims** Lightcurves and results (100 different injections) in section Bu2025study/

See scramble.py for the generation of resampled lightcurves

## Scripts for plots generation

See the following scripts to reproduce the figures from the article:
* 170817/ErrorHisto.py --> Figure 1
* RecoveryPlots.py --> Figs 4, 5, 6, 8, 11, 19
* InjectionRecovery21plots.py --> Fig 10
* reanalysis_lightcurve_grid.py --> Figs 12, 13
* cornerplotcombine.py --> Fig 3, 14
* 170817/ConstraintBestfitLCs.py --> Figs 15, 16
* ParameterWiseGains.py --> Figs 20, 21, 22

