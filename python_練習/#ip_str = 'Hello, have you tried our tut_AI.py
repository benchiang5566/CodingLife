
#def count_vowels(ip_str): 
#    return {v: ip_str.count(v) for v in 'aeiou'}

# 測試範例
#ip_str = '7rstmMhm1cyOGWNS8KnFjg7tfHZmJDpI4gdBuOn7NzAPaBb06c7kIqozI1IE5haIPIy'
#result = count_vowels(ip_str)
#print(result)

def count_vowels(ip_str):
    vowels= {'a':0,'e':0,'i':0,'o':0,'u':0}
    for char in  ip_str.lower():
        if char in 'aeiou':
            vowels[char]+=1
    return vowels

ip_str='7rstmMhm1cyOGWNS8KnFjg7tfHZmJDpI4gdBuOn7NzAPaBb06c7kIqozI1IE5haIPIy'
result = count_vowels(ip_str)
print(result)

def count_vowels(ip_str):
    vowels={'a':0,'e':0,'i':0,'o':0,'u':0}
    for char in ip_str.lower():
        if char in 'aeiou':
            vowels[char]+=1
    return vowels
ip_str='hm1cyOGWNS8KnFjg7tfHZmJDpI4gdB'
result = count_vowels(ip_str)
print(result)