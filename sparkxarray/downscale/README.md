# Monthly Bias Correction
- Follows the [Brekke et al (2013) methodology](http://gdo-dcp.ucllnl.org/downscaled_cmip_projections/techmemo/downscaled_climate.pdf)

- The approach is a quantile mapping technique operated on monthly and location-specific basis as outline below:

**1. Gather Data**
  - Start with three datasets
    - Observed historical data (OBS)
    - Simulated historical data from given global climate model (GCM)
    - The GCM's simulated future climate data (PROJ)
    
**2. Identify Bias**
  - The bias-correction basis is identified by focusing on OBS and GCM datasets.
  - This basis is then used to guide bias-correction of GCM and PROJ datasets.
  - Identifying this basis requires adopting a bias-identification period of common overlap in OBS and GCM datasets.
  - Bias-identification proceeds on a variable-, month- and -location specific basis
  - For values in each grid cell, month, and variable, construct cumulative distibution functions (CDFs) of conditions from GCM dataset and conditions from OBS dataset.
  - The paired CDFs combine to form a **quantile map** where at each rank of probability, or percentile, one can assess the bias between GCM ad OBS (at that location, for that variable, and during that month).
  - Repeat this procedure for all projections, producing a quantile map for every projection
  - NOTE: The number of unique quantile maps equals the number of unique historical simulations initializing the future projections, which is typically fewer than the number of future projections because one historical simulation can initialize multiple future projections.
  
**3. Correct Bias**
  - Adjust values of Both GCM and PROJ datasets uding the quantile maps produced in **step 2** using the adjustment procedure below
  - ![](https://i.imgur.com/Kqb5Uqp.png)
  - Proceed on a location- and timestep-specific basis, first moving sequentially through GCM dataset and then through PROJ dataset.
  - At  any timestep, the adjustment involves:
    - identifying the GCM value at that timestep, 
    - looking up the associated rank probability (p) from the GCM's historical **quantile map** (step 2), 
    - identifying corresponding OBS value at this rank probability in the **quantile map**
    - accepting that OBS value as the adjusted GCM value.
    
    
 Notes:
- Before applying bias-correction to Tavg, Tmin, and
Tmax projections, the GCM trend is removed, and then
bias-correction is applied to the residual magnitudes to create adjusted
GCM. Afterwards, the trend is added back to adjusted GCM (Maurer,
2007). As discussed by Wood et al. (2004), this is important during the
temperature bias-correction step to prevent rising future temperatures from
falling disproportionately on the extreme tail of the OBS CDF.

- When applying bias-correction to Precipitation projections, there is no
trend removal prior to bias-correction. As a result, the “raw” (i.e., biased)
and bias-corrected Precipitation projections are not constrained to have the same trend 

