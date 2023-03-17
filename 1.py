import math
import scipy.stats as stats
t1 = stats.t.ppf (0.975, 255)
print(80 - t1 * (16 / math.sqrt(256)), ";", 80 + t1 * (16 / math.sqrt(256)))
