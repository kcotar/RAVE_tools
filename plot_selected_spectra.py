import matplotlib.pyplot as plt
from helper_functions import *


data_main_dir = '/home/gregor/Projects/IJS_classification/DR/'
rave_obs_ids = ['20070814_0020m31_038', '20080623_2353m28_137']


for r_id in rave_obs_ids:
    wvl, flx = get_spectrum(r_id, path=data_main_dir)
    plt.plot(wvl, flx)

plt.ylim((0.4, 1.2))
plt.show()
plt.close()