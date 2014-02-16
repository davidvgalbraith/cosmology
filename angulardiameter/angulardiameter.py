#Plots the angular diameter of a Milky Way (MW)-sized
#galaxy as a function of redshift

import matplotlib.pyplot as plt
import numpy as np
import math

#angular diameter at redshift z for a size-kpc galaxy
#in a universe with density parameter in matter omegaz

def angdi(z, size, omegaz):
    return 25 * size * omegaz**2 * (1 + z)**2 / ((4 * 3.0 * 10**8) * (z * omegaz / 2 + (omegaz / 2 - 1) * (math.sqrt(omegaz * z + 1) - 1)))


x = np.arange(.01, 10, .001)

y1 = [angdi(z, 20, 0.27) for z in x]
y2 = [angdi(z, 20, 1.0) for z in x]
y3 = [angdi(z, 20, 2.7) for z in x]

plt.plot(x, y1, label="Omega_0 = 0.27")
plt.plot(x, y2, label="Omega_0 = 1.0")
plt.plot(x, y3, label="Omega_0 = 2.7")

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Redshift z", fontsize=30)
plt.ylabel("Angular diameter, kPc", fontsize=30)
plt.title("Angular Diameter vs. Redshift for a 20kPc galaxy in Various Universes", fontsize=30) 
plt.legend()
plt.show()
