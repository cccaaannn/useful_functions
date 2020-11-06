# https://numba.pydata.org/
# pip install numba


import numpy as np
import numba
from numba import jit
import time



@jit(nopython=True)
def gaussians(x, means, widths):
    '''Return the value of gaussian kernels.
    
    x - location of evaluation
    means - array of kernel means
    widths - array of kernel widths
    '''
    n = means.shape[0]
    result = np.exp( -0.5 * ((x - means) / widths)**2 ) / widths
    return result / np.sqrt(2 * np.pi) / n

def gaussians_python(x, means, widths):
    '''Return the value of gaussian kernels.
    
    x - location of evaluation
    means - array of kernel means
    widths - array of kernel widths
    '''
    n = means.shape[0]
    result = np.exp( -0.5 * ((x - means) / widths)**2 ) / widths
    return result / np.sqrt(2 * np.pi) / n

def time_function(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    total = end - start
    print(total)


means = np.random.uniform(-1, 1, size=1000000)
widths = np.random.uniform(0.1, 0.3, size=1000000)


# gaussians(0.4, means, widths)
# gaussians.py_func(0.4, means, widths)



time_function(gaussians, 0.4, means, widths)
time_function(gaussians_python, 0.4, means, widths)
