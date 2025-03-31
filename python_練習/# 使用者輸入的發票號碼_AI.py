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
    prizes = [7, 6, 5, 4, 3]
    messages = ["頭獎", "二獎", "三獎", "四獎", "五獎", "六獎"]
    for prize_num in n2:
        if num == prize_num:
            print("恭喜！中頭獎！")
            break
        for i, digits in enumerate(prizes):
            if num[-digits:] == prize_num[-digits:]:
                print(f"恭喜！中{messages[i+1]}！")
                break
        else:
            continue
        break
    else:
        print("很遺憾，沒有中獎。")
