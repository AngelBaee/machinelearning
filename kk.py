import numpy

kk = int(input("Enter the number: "))
arr = []
for i in range(kk):
    ll = int(input("Enter the value: "))
    arr.append(ll)

numbs = numpy.mean(arr)

print(numbs)
