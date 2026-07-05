# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」

# 強制結束 ctrl + c

# 報錯時 提示使用者 "請輸入數字 而不是文字"

# 猜錯三次 失敗 就結束整個程式
# 猜對了 可以詢問使用者是否再一次

answer = 60
wrong_count = 0  # 記錄猜錯次數

while True:
    try:
        user_input = int(input("請輸入 1-100 數字: "))

        # 超出範圍要顯示「超出範圍請重新輸入」
        if user_input > 100 or user_input < 1:
            print("超出範圍請重新輸入")

        # 使用者猜對要回傳「恭喜中獎」
        elif user_input == answer:
            print("恭喜中獎!")
            # 猜對了 可以詢問使用者是否再一次
            again = input("是否要再玩一次？(y/n): ")
            if again == "y":
                wrong_count = 0  # 重設猜錯次數
            else:
                break

        # 數字太大 要提示「請輸入更小的數字」
        elif user_input > answer:
            print("請輸入更小的數字")
            wrong_count += 1

        # 數字太小 要提示「請輸入更大的數字」
        elif user_input < answer:
            print("請輸入更大的數字")
            wrong_count += 1

        # 猜錯三次 失敗 就結束整個程式
        if wrong_count >= 3:
            print("猜錯三次，遊戲結束！")
            break

    # 報錯時 提示使用者 "請輸入數字 而不是文字"
    except ValueError:
        print("請輸入數字 而不是文字")

    # 強制結束 ctrl + c
    except KeyboardInterrupt:
        print("\n已強制結束遊戲。")
        break
