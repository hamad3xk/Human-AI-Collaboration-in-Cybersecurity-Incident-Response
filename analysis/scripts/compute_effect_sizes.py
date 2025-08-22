import numpy as np

def cohens_d(x, y):
    x = np.asarray(x); y = np.asarray(y)
    s_p = np.sqrt(((len(x)-1)*x.var(ddof=1) + (len(y)-1)*y.var(ddof=1)) / (len(x)+len(y)-2))
    return (x.mean() - y.mean()) / s_p

def rank_biserial_r(u_stat, n1, n2):
    return 1 - (2*u_stat)/(n1*n2)
