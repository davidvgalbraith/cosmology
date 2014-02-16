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

#part b for omega_0m less than 1
def agelambdaomegalessthan1(omegaz):
    return 2.0 / (3.0 * math.sqrt(1 - omegaz)) * math.log((math.sqrt(1 - omegaz) + 1) / math.sqrt(omegaz))

#part b for omega_0m greater than 1
def agelambdaomegagreaterthan1(omegaz):
    return 2.0 / (3.0 * math.sqrt(omegaz - 1)) * math.asin(math.sqrt((omegaz - 1) / omegaz))

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
def fb(x):
    if x < 1:
        return agelambdaomegalessthan1(x)
    if x > 1:
        return agelambdaomegagreaterthan1(x)
    return 0.5 * (fb(1.001) + fb(0.999))

x = np.arange(0.001, 3.0, 0.001)
y1 = [fa(y) for y in x]
y2 = [fb(y) for y in x]


plt.plot(x, y1, label="Lambda = 0")
plt.plot(x, y2, label="Lambda + m = 1")
plt.xlabel("Density parameter", fontsize=30)
plt.ylabel("Age of the Universe", fontsize=30)
plt.title("Age of the Universe vs. Density parameter", fontsize=30)
plt.legend()
plt.show()
