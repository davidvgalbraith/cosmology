import matplotlib.pyplot as plt
import numpy as np
import math

#Hubble constant at time t for mass density parameter omegaz less than 1
def hlambdaomegalessthan1(omegaz, t):
    return 1000 * (1.0 / t) * 2.0 / (3.0 * math.sqrt(1 - omegaz)) * math.log((math.sqrt(1 - omegaz) + 1) / math.sqrt(omegaz))

#Hubble constant at time t for mass density parameter omegaz for omega_0m greater than 1
def hlambdaomegagreaterthan1(omegaz, t):
    return 1000 * (1.0 / t) * 2.0 / (3.0 * math.sqrt(omegaz - 1)) * math.asin(math.sqrt((omegaz - 1) / omegaz))

#Age of the universe as a function of matter density parameter in 
#a universe with cosmological constant constrained by
#matter density parameter + lambda density parameter = 1
def fb(x, t):
    if x < 1:
        return hlambdaomegalessthan1(x, t)
    if x > 1:
        return hlambdaomegagreaterthan1(x, t)
    return 0.5 * (fb(1.001, t) + fb(0.999, t))

x = np.arange(0.001, 3.0, 0.001)
y1 = [fb(y, 11.5) for y in x]
y2 = [fb(y, 13.8) for y in x]
y3 = [fb(y, 18.0) for y in x]
plt.plot(x, y1, label="t0 = 11.5")
plt.plot(x, y2, label="t0 = 13.8")
plt.plot(x, y3, label="t0 = 18")
plt.plot(x, [72 for y in x])
plt.xlabel("Density Parameter in Matter", fontsize=30)
plt.ylabel("Hubble constant, km/s/Mpc", fontsize=30)
plt.title("Hubble constant vs Matter Density Parameter", fontsize=30)
plt.legend()
plt.show()
