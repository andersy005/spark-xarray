from sparkxarray.downscale import biascorrect as bc
import numpy as np

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




