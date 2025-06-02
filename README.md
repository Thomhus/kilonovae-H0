## kilonovae-H0
KN analyses of AT2017gfo and simulated events, looking at distance posteriors, with the eventual goal of estimating H0 from a sample of kilonovae

# Data for **Kilonova modelling and parameter inference: Understanding uncertainties and evaluating compatibility between observations and models** [arXiv](https://arxiv.org/abs/2505.21392)

## Datasets and corresponding parameter inference results

* **AT2017gfo** Lightcurve at 170817/AT2017gfoMWcorrected.dat
	Results with prior sets:
	* **A1** 170817/Bu2019full_MWcorrected/1err
	* **B1** 170817/Bu2019full_MWcorrected/1errtightangle_all
	* **C1** 170817/Errsys+constraints/1AngleradioGWdistance
	* **D1** 170817/Errsys+constraints/1AngleradioGWdistance+masses
	* **A0.6** 170817/Errsys+constraints/06Allfree
	* **B0.6** 170817/Errsys+constraints/06Angleradio
	* **C0.6** 170817/Errsys+constraints/06AngleradioGWdistance
	* **D0.6** 170817/Errsys+constraints/06AngleradioGWdistance+masses
	
* **sim17** Lightcurves and results with different cadences and filter sets in section lcsimu/

* **toymodel** Lightcurve and results in lcsimu/varying_sigma_sus_truecadence_0.5noise

* **ManySims** Lightcurves and results (22 different injections, each declined in 20 resampled lightcurves) in section Injection_Recovery_IterationsVariation/

See scramble.py for the generation of resampled lightcurves

## Scripts for plots generation

See RecoveryPlots.py, InjectionRecovery21plots.py, analysis_lightcurve_grid.py and 170817/ErrorHisto.py to reproduce figures from the article
