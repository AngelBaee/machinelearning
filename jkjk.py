import numpy

ll = int(input("Enter the range of ur values: "))
arr = []

for i in range(ll):
    ff = int(input("Enter the value: "))
    arr.append(ff)

ee = numpy.median(arr)

print(ee)
#22,22,33,33,44,55,66,77