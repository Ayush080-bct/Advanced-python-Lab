def fact(n,a):
    if(n==0 or n==1):
        return a
    else:
        return fact(n-1,n*a)
result=fact(5,1)
print(result)