from scipy import stats

ll = int(input("Enter the range of values: "))

arr = []

for i in range(ll):
    ff = int(input("Enter the value: "))
    arr.append(ff)

kk = stats.mode(arr)

print(kk)


#The mode() method returns a ModeResult object that contains the mode number (11), and count (how many times the mode number appeared (3)).
