# 輸入發票號碼
num = input('輸入你的發票號碼：')

# 獎項設定
ns = '05701942'          # 特別獎
n1 = '97718570'          # 特獎
n2 = ['88400675', '73475574', '53038222']  # 頭獎

# 特別獎和特獎的判斷
if num == ns:
    print("恭喜！中特別獎！")
elif num == n1:
    print("恭喜！中特獎！")
else:
    # 頭獎及二到六獎判斷
    prize_matched = False
    for prize_num in n2:
        if num == prize_num:
            print("恭喜！中頭獎！")
            prize_matched = True
            break
        elif num[-7:] == prize_num[-7:]:  # 二獎判斷
            print("恭喜！中二獎！")
            prize_matched = True
            break
        elif num[-6:] == prize_num[-6:]:  # 三獎判斷
            print("恭喜！中三獎！")
            prize_matched = True
            break
        elif num[-5:] == prize_num[-5:]:  # 四獎判斷
            print("恭喜！中四獎！")
            prize_matched = True
            break
        elif num[-4:] == prize_num[-4:]:  # 五獎判斷
            print("恭喜！中五獎！")
            prize_matched = True
            break
        elif num[-3:] == prize_num[-3:]:  # 六獎判斷
            print("恭喜！中六獎！")
            prize_matched = True
            break
    
    if not prize_matched:
        print("很遺憾，沒有中獎。")
