import matplotlib.pyplot as plt
import numpy as np
import math

#plots the current age of the universe as a function of the density parameter
#for model universes with and without cosmological constant
def agenolambdamlessthan1(omegaz):
    eta = math.acosh((1.0 - omegaz) / omegaz * 2.0 + 1.0)
    return 0.5 * omegaz / ((1 - omegaz)**1.5) * (math.sinh(eta) - eta)

def agenolambdamgreaterthan1(omegaz):
    theta = math.acos(1.0 - 2.0 * (omegaz - 1) / omegaz)
    return 0.5 * omegaz / ((omegaz - 1)**1.5) * (theta - math.sin(theta))

#Hubble constant at time t for mass density parameter omegaz less than 1
def hlambdaomegalessthan1(omegaz, t):
    return (1.0 / t) * 2.0 / (3.0 * math.sqrt(1 - omegaz)) * math.log((math.sqrt(1 - omegaz) + 1) / math.sqrt(omegaz))

#Hubble constant at time t for mass density parameter omegaz for omega_0m greater than 1
def hlambdaomegagreaterthan1(omegaz, t):
    return (1.0 / t) * 2.0 / (3.0 * math.sqrt(omegaz - 1)) * math.asin(math.sqrt((omegaz - 1) / omegaz))

#Age of the universe as a function of density parameter
#in a universe without cosmological constant
def fa(x):
    if x < 1:
        return agenolambdamlessthan1(x)
    if x > 1:
        return agenolambdamgreaterthan1(x)
    return 0.5 * (fa(1.001) + fa(0.999))

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
plt.xlabel("Density parameter", fontsize=30)
plt.ylabel("Age of the Universe", fontsize=30)
plt.title("Age of the Universe vs. Density parameter", fontsize=30)
plt.legend()
plt.show()
