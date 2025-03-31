zipcode = {"台北市":{"中正區": 100, "大同區": 103, "中山區": 104, "松山區": 105, "大安區": 106, "萬華區": 108, "信義區": 110, "士林區": 111, "北投區": 112, "內湖區": 114, "南港區": 115, "文山區": 116}, "基隆市":{"仁愛區": 200, "信義區": 201, "中正區": 202, "中山區": 203, "安樂區": 204, "暖暖區": 205, "七堵區": 206},"新北市": {"萬里區": 207, "金山區": 208, "板橋區": 220, "汐止區": 221, "深坑區": 222, "石碇區": 223, "瑞芳區": 224, "平溪區": 226, "雙溪區": 227, "貢寮區": 228, "新店區": 231, "坪林區": 232, "烏來區": 233, "永和區": 234, "中和區": 235, "土城區": 236, "三峽區": 237, "樹林區": 238, "鶯歌區": 239, "三重區": 241, "新莊區": 242, "泰山區": 243, "林口區": 244, "蘆洲區": 247, "五股區": 248, "八里區": 249, "淡水區": 251, "三芝區": 252, "石門區": 253}}

# 查詢郵遞區號、地區與城市之間的對應關係
def query_zipcode(city=None, area=None, z=None):
    results = []

    for city_name, areas in zipcode.items():
        for area_name, zip_code in areas.items():
            # 判斷輸入條件，若符合則加入結果
            if (city == city_name or not city) and (area == area_name or not area) and (z == zip_code or not z):
                results.append(f"[{city_name}, {area_name}, {zip_code}]")

    # 輸出結果或顯示找不到結果的訊息
    if results:
        print("\n".join(results))
    else:
        print("No matching results found.")

# 資料範例，儲存每個城市及其對應地區的郵遞區號。


# 根據使用者輸入進行查詢

city = input("請輸入城市名稱 (若無則按 Enter): ").strip()
area = input("請輸入地區名稱 (若無則按 Enter): ").strip()
z = input("請輸入郵遞區號 (若無則按 Enter): ").strip()

# 將郵遞區號轉換為整數，若有輸入
z = int(z) if z.isdigit() else None

# 執行查詢
query_zipcode(city if city else None, area if area else None, z)
