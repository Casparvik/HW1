lim_old= [-10, 25]
lim_new = [-1, 1]

from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

def mapping_limits(x, lim_new, lim_old):
    mapped = interp1d(lim_new, lim_old)
    return float(mapped(x))

if __name__ == '__main__':

    print(mapping_limits(0,lim_new,lim_old))