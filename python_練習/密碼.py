import string
import random
chs = string.ascii_letters + string.digits
num_passwords=random.randint(1,4)

for i in range(num_passwords):
    pwd = ''.join(random.choice(chs) for x in range(random.randint(8,12)))
    print(f'{i+1} {pwd}')
#import string
#import random
#chs = string.ascii_letters + string.digits
#pwd=""

#for i in range(random(1,4)):
#    for x in range(random.randint(8,12)):
#        pwd+=random.choice(chs)
#    print(pwd)




#import string
#import random

