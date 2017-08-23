from sparkxarray.downscale import biascorrect as bc
import numpy as np
import xarray as xr
import numpy as np
import pandas as pd
import seaborn as sns # pandas aware plotting library

np.random.seed(123)

times = pd.date_range('2000-01-01', '2001-12-31', name='time')
annual_cycle = np.sin(2 * np.pi * (times.dayofyear.values / 365.25 - 0.28))

base = 10 + 15 * annual_cycle.reshape(-1, 1)
tmin_values = base + 3 * np.random.randn(annual_cycle.size, 3)
tmax_values = base + 10 + 3 * np.random.randn(annual_cycle.size, 3)

ds = xr.Dataset({'tmin': (('time', 'location'), tmin_values),
                 'tmax': (('time', 'location'), tmax_values)},
                {'time': times, 'location': ['IA', 'IN', 'IL']})



n = 1000

raw_data = np.random.uniform(low=0, high=40, size=(10,))
obs = np.random.uniform(low=0.5, high=13.3, size=(n,))
mod = np.random.uniform(low=1.5, high=19.3, size=(n,))



a = bc.Biascorrect(obs_data=obs, model_data=mod, raw_data=raw_data)

print("Fake observed data: \n{} \n".format(a.obs_data))
print("Fake model data: \n{} \n".format(a.model_data))
bc_data =  a.qpqm()
print(bc_data.shape)
assert(raw_data.shape == bc_data.shape)
#assert raw_data == bc_data




