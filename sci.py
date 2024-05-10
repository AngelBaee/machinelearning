from scipy import stats

ll = [33,44,67,43,23,57,44,99,35]

kk = stats.mode(ll)

print(kk)