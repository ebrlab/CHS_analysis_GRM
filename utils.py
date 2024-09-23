from scipy.special import expit
import numpy as np 

def pordlog(a):
    pa = expit(a)
    p_cum = np.concatenate(([0.], pa, [1.]))
    return p_cum[1:] - p_cum[:-1]