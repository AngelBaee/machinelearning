# to calculate the variance need to do as follows:
### (32+111+138+28+59+77+97) / 7 = 77.4 - find the mean
### 32 - 77.4 = -45.4
# 111 - 77.4 =  33.6
# 138 - 77.4 =  60.6
# 28 - 77.4 = -49.4
# 59 - 77.4 = -18.4
# 77 - 77.4 = - 0.4
# 97 - 77.4 =  19.6 find each value: find the difference from the mean
###(-45.4)2 = 2061.16
# (33.6)2 = 1128.96
# (60.6)2 = 3672.36
#(-49.4)2 = 2440.36
#(-18.4)2 =  338.56
#(- 0.4)2 =    0.16
# (19.6)2 =  384.16-  For each difference: find the square value:
###(2061.16+1128.96+3672.36+2440.36+338.56+0.16+384.16) / 7 = 1432.2-4. The variance is the average number of these squared differences:
#This is how it's calculated manually without using NUMPY!!!!!!!

import numpy

speed = [32,111,138,28,59,77,97]

ll = numpy.var(speed)

print(ll)

