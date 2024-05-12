import numpy as np

k = int(input("Enter the size of the array: "))
arr = []
for i in range(k):
    g = int(input("Enter the number: "))
    arr.append(g)

l = np.std(arr)

print(l)