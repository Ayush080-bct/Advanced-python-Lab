def mean(lst):
    return sum(lst)/len(lst)
def max_values(lst):
    return max(lst)
def min_values(lst):
    return min(lst)
def range(lst):
    return max(lst)-min(lst)
def variance(lst):
    n=len(lst)
    return (sum(x**2 for x in lst)/n)-sum(lst)/n
def std(lst):
    return variance**0.5

