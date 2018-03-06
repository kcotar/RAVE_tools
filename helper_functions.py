import numpy as np

def get_spectrum(identifier, path=''):
    # sample RAVE_OBS_ID is 20070814_0020m31_038 (string value)
    # sample txt file name with spectrum 1030m24.rvsun.125.cont.vrcor.txt
    id_split = identifier.split('_')
    date_dir = id_split[0] + '/'
    txt_file = id_split[1]+'.rvsun.'+id_split[2]+'.cont.vrcor.txt'

    # load file
    data = np.loadtxt(path + date_dir +txt_file)
    return data[:, 0], data[:, 1]