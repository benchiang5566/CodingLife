def factors(n):
    factors=[]                  #

    for i in range(2,n):        #迴圈設定，因數的範圍2~n-1

        if n % i == 0:          #條件n/i...0
            factors.append(i)   #因為要陳列出因數值，回傳到[]
    
    return factors              #讓for迴圈可以持續順利運作
   
num=int(input())
print(factors(num))
