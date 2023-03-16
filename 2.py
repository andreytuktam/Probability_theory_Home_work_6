import numpy as np
import scipy.stats as stats
a = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
x_1 = np.mean(a)
D1 = np.var(a, ddof=1)
t1 = stats.t.ppf (0.975, 9)
print(x_1 - t1 * np.sqrt (D1/10), ";", x_1 + t1 * np.sqrt (D1/10))
