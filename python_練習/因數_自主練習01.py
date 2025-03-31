def factors(n):
    factors=[]
    for i in range(1,n+1):
        if n%i==0:
            factors.append(i)
    return factors
num=int(input(factors))
print("因數",factors(num))