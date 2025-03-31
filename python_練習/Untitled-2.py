#first = input("請輸入第一個值: ")

#if first.isdigit():
#    second = input("請輸入第二個值: ")
#    if second.isdigit():
#        print("兩個值都是數字")
#    else:
#        print("請重新輸入第二個數字")
#else:
#    print("請重新輸入第一個數字")

if input("請輸入第一個值: ").isdigit() and input("請輸入第二個值: ").isdigit():
    print("兩個值都是數字")
else:
    print("請重新輸入數字")
