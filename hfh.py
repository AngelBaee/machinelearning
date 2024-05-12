import numpy as np

kk = int(input("Enter the range: "))

arr = []

for i in range(kk):
    jj = int(input("Enter the number: "))
    arr.append(jj)

hh = np.var(arr)

print(hh)