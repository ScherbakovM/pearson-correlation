from scipy.stats import linregress

def pearson(arr_x, arr_y):
    result = linregress(arr_x, arr_y)
    return result

a = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
b = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
print(pearson(a, b))
