from scipy import stats

kk = [5,7,8,7,2,17,2,9,4,11,12,9,6]
ll = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r , p , std_err = stats.linregress(kk,ll)

def lala(kk):
    return slope* kk + intercept

speed = lala(10)

print(speed)