import random

# 生成6个1到49之间的唯一随机数
lottery_numbers = sorted(random.sample(range(1, 50), 6))

print(lottery_numbers)