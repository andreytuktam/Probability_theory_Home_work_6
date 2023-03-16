import numpy as np 
import scipy.stats as stats
m = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
d = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])

x_1 = np.mean(m)
x_2 = np.mean(d)
delta = x_1 - x_2

D1 = np.var(m, ddof=1)
D2 = np.var(d, ddof=1)
D = (D1 + D2) / 2

SE = np.sqrt (D / 10 + D / 10)
t = stats.t.ppf(0.975, 18)

print(delta - t * SE, ";", delta + t * SE)


