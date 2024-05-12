import numpy as np

numb = int(input("Enter the number of ages: "))

arr = []

for i in range(numb):
    ages = int(input("Define the ages: "))
    arr.append(ages)

result = np.percentile(arr, 50)

print(result)