import xarray as xr
import numpy as np 
import scipy.stats


class Biascorrect(object):
    def __init__(self, obs_data, model_data, raw_data=None, newdata=None, cdfn=10, precipitation=False, method=None, cross_val=None, 
                 folds=None, window=None, scaling_type=None, wet_threshold=None, n_quantiles=None,
                 extrapolation=None, theta=None, join_members=None):
        self.obs_data = np.sort(obs_data)
        self.model_data = np.sort(model_data)
        self.raw_data = raw_data
        self.newdata = newdata
        self.precipitation = precipitation
        self.method = method
        self.cross_val = cross_val
        self.folds = folds
        self.window = window
        self.scaling_type = scaling_type
        self.wet_threshold = wet_threshold
        self.n_quantiles = n_quantiles
        self.extrapolation = extrapolation
        self.theta = theta
        self.join_members = join_members
        self.xbins = None
        self.cdfobs = None
        self.cdfmodel = None
        self.n = obs_data.size
        self.cdfn = cdfn
        

    def qpqm(self):
        """ quantile(CDF) mapping bias correction. 
        
        - CDF mapping for bias correction
        - Note that the values exceeding the range of the training set
         are set to -999 at the moment. -possibly could leave unchanged?
         
        """
        
        print("Computing pdf cdf ....")
        self.compute_pdf_cdf()
 
        # Calculate exact CDF values using linear interpolation
        cdf1 = np.interp(self.raw_data, self.xbins, self.cdfmodel, left=0.0, right=999.0)
        
        # Now use interpol again to invert the obsCDF, hence reversed model_data, obs_data
        corrected = np.interp(cdf1, self.cdfobs, self.xbins, left=0.0, right=-999.0)
     
        return corrected 
    
    
    def calc_bins(self):
        global_max = max(np.amax(self.obs_data), np.amax(self.model_data))
        wide = global_max / self.cdfn
        bins = np.arange(0.0, global_max+wide, wide)
        return bins
    
    def compute_pdf_cdf(self):
        """Compute PDF adn CDF """
        if self.xbins is None:
            self.xbins = self.calc_bins()
            
        # create PDF
        pdfobs, bins = np.histogram(self.obs_data, bins=self.xbins)
        pdfmodel, bins = np.histogram(self.model_data, bins=self.xbins)
        
        # create CDF with zero in first entry
        self.cdfobs = np.insert(np.cumsum(pdfobs), 0, 0.0)
        self.cdfmodel = np.insert(np.cumsum(pdfmodel), 0, 0.0)
        
        
        
        
        


