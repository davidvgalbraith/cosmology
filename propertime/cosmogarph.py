import matplotlib.pyplot as plt
import numpy as np

#gives the proper time as a function of matter density parameter,
#cosmological constant density parameter, and scale factor a
def proptime(matter, lamda, a):
    t = matter + lamda
    return (1 - t) / (1 - t + l * a * a + m / a)
a = .001

t = np.arange(.001, .01, .001)
x = np.arange(.001, .01, .05)

#Example model universes to graph
def f1(a):
    return 1-f(0.27, 0.0, a)
def f2(a):
    return 1-f(0.27, 0.73, a)
def f3(a):
    return 1-f(1.0, 0, a)
def f4(a):
    return 1-f(2.7, 0, a)

y1 = f1(t)
y2 = f2(t)
y3 = f3(x)
y4 = f4(t)

plt.plot(t, y1, label="(.27, 0)")
plt.plot(t, y2, label="(.27, .73)")
plt.plot(x, y3, "ro", label="(1.0, 0)")
plt.plot(t, y4, label="(2.7, 0)")
plt.axis([.001, .01, .99, 1.01])
plt.xscale("log")
plt.yscale("log")
plt.title("Density Paramter vs. Scale length for Various Universes") 
plt.legend()
plt.show()
