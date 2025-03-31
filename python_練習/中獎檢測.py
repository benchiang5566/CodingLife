num = input()
ns = '05701942'         # 特別獎 
n1 = '97718570'         # 特獎 
n2 = ['88400675', '73475574', '53038222']  # 頭獎清單
if num==ns:
    print('A')
elif num == n1:
    print('B')
else:
    for prize_num in n2:
        for i in range(3,9):
            if num[-i:] == prize_num[-i:]:
                print({9 - i})
                break
        else:
            continue
        break
    else:
        print("0")
