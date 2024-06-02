import numpy
import matplotlib.pyplot as plt

kk = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
ll = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

lol = numpy.poly1d(numpy.polyfit(kk,ll,3))

line = numpy.linspace(1,22,100)

plt.scatter(kk,ll)
plt.plot(line,lol(line))
plt.show()
