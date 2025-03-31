# 郵遞區號資料
zipcode = {
    "台北市": {"中正區": 100, "大同區": 103, "中山區": 104, "松山區": 105, "大安區": 106, "萬華區": 108, "信義區": 110, "士林區": 111, "北投區": 112, "內湖區": 114, "南港區": 115, "文山區": 116},
    "基隆市": {"仁愛區": 200, "信義區": 201, "中正區": 202, "中山區": 203, "安樂區": 204, "暖暖區": 205, "七堵區": 206},
    "新北市": {"萬里區": 207, "金山區": 208, "板橋區": 220, "汐止區": 221, "深坑區": 222, "石碇區": 223, "瑞芳區": 224, "平溪區": 226, "雙溪區": 227, "貢寮區": 228, "新店區": 231, "坪林區": 232, "烏來區": 233, "永和區": 234, "中和區": 235, "土城區": 236, "三峽區": 237, "樹林區": 238, "鶯歌區": 239, "三重區": 241, "新莊區": 242, "泰山區": 243, "林口區": 244, "蘆洲區": 247, "五股區": 248, "八里區": 249, "淡水區": 251, "三芝區": 252, "石門區": 253}
}

# 查詢功能
def query_zipcode(city=None, area=None, z=None):
    results = [
        f"[{c}, {a}, {z_code}]"
        for c, areas in zipcode.items()
        for a, z_code in areas.items()
        if (not city or city == c) and (not area or area == a) and (not z or z == z_code)
    ]
    print("\n".join(results) or "查無匹配的結果")

# for c, areas in zipcode.items()：對於每個城市 c 和其對應的地區字典 areas。
# for a, z_code in areas.items()：對於每個地區 a 和其對應的郵遞區號 z_code。
# if (not city or city == c) and (not area or area == a) and (not z or z == z_code)：判斷條件。
# not city or city == c：如果 city 是 None 或等於目前的城市 c，則條件成立。
# not area or area == a：如果 area 是 None 或等於目前的地區 a，則條件成立。
# not z or z == z_code：如果 z 是 None 或等於目前的郵遞區號 z_code，則條件成立。
# f"[{c}, {a}, {z_code}]"：將符合條件的城市、地區和郵遞區號格式化成字串加入 results。


# 獲取用戶輸入並查詢
query_zipcode(
    input("請輸入城市名稱 (若無則按 Enter): ").strip() or None,
    input("請輸入地區名稱 (若無則按 Enter): ").strip() or None,
    int(z) if (z := input("請輸入郵遞區號 (若無則按 Enter): ").strip()).isdigit() else None
)

#input() 函式用來獲取用戶輸入。.strip() 是用來去除輸入中的前後空白字符。
#or None 用來處理空輸入，如果用戶直接按下 Enter，則會得到 None。
#z := input("...").strip() 是 Python 3.8+ 的walrus 運算符，可以在一行中同時進行賦值和條件檢查。
#int(z) if z.isdigit() else None：如果輸入的 z 是數字，則轉換為整數，否則為 None。