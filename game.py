# 01工具與函式定義

import random # 輸入亂數工具
import json # 輸入json工具
import os # 輸入讀取資料工具

# 定義函式
def say_hello(name): # 歡迎玩家
    print()
    print("=================================")
    print(f"歡迎{name}來到人生養成模擬器！")
    print("=================================")
    print()


def show_player(name, age, player): # 顯示玩家初始能力值
    print(f"玩家姓名：{name}")
    print(f"玩家年齡：{age}")
    print(f"健康：{player['health']}")
    print(f"智力：{player['intelligence']}")
    print(f"社交：{player['social']}")
    print(f"體力：{player['energy']}")
    print(f"存款：NT$ {player['money']:,}")

def increase_stat(player, stat): # 能力值增加
    player[stat] += 10
    player[stat] = min(player[stat], 100) # 限制值最高為100

def decrease_stat(player, stat): # 能力值減少
    player[stat] -= 10
    player[stat] = max(player[stat], 0) # 限制值最低為0


def show_stat(label, value): # 顯示每日能力值總結
    filled = value // 10
    print(f"│{label:<4}{'█' * filled + '░' * (10 - filled)}{value:>3}/100{' ' * 11} │")


def earn_money(money, salary): # 定義工作賺錢的計算
    return money + salary

def death_rate(age, health, energy): # 計算每年死亡的機率
    rate = min(age * 0.1 + (100 - health) * 0.05 + (100 - energy) * 0.05, 30)
    return rate

def natural_death_rate(age): # 確定死後，再來計算自然死亡的機率
    if age <= 20:
        natural_rate = 1
    elif age > 20 and age <= 30:
        natural_rate = (age - 20) * 0.4 + 1
    elif age > 30 and age <= 40:
        natural_rate = (age - 30) * 1 + 5
    elif age > 40 and age <= 50:
        natural_rate = (age - 40) * 1 + 15
    elif age > 50 and age <= 60:
        natural_rate = (age - 50) * 2 + 25
    elif age > 60 and age <= 70:
        natural_rate = (age - 60) * 2 + 45
    elif age > 70 and age <= 80:
        natural_rate = (age - 70) * 2 + 65
    elif age > 80 and age <= 90:
        natural_rate = (age - 80) * 1 + 85
    else:
        natural_rate = 95
    return natural_rate 

def save_game(name, age, year, player, life_story, is_finished, past_lives): # 存取遊戲進度
    # 所需重要資料 玩家姓名、年齡、第幾年、基本數值、人生故事
    save_data = {
    "name"  : name,
    "age"   : age,
    "year"  : year,
    "player": player,
    "life_story"  : life_story,
    "is_finished" : is_finished,
    "past_lives" : past_lives
}
    json_data = json.dumps(save_data, ensure_ascii=False) # 把python的字典轉換成json字串
                                                          # 開啟一個檔案叫做save.json 使用寫入模式 w 
                                                          # 幫她取一個代號叫做file
                                                          # save.json和file視同個東西
                                                          # save.json是檔案名稱，後面會有副檔名.json
                                                          # file是變數名稱 後面沒有附檔名 
    with open("save.json", "w", encoding="utf-8") as file:  #encoding是轉成中文
        file.write(json_data) # 把json_data這個資料寫入file裡面

print()
# 02建立玩家資料

age = 0 # 基本資料，設定每個玩家都從0歲開始玩
year = 1
life_story = []  # 建立一個人生回顧清單
is_finished = False
past_lives = [] #時光機清單，存放過去人生的資料

player = { # 設定玩家初始能力值(變數) 以字典來整理
    "health" : 50,
    "intelligence" : 30,
    "social" : 20,
    "energy" : 40,
    "money" : 8000
}
# 03讀取存檔
if os.path.exists("save.json"):# 如果有儲存檔，打開並讀取
    with open("save.json", "r", encoding="utf-8") as file:
        load_data = json.load(file)
        name = load_data["name"]
        age = load_data["age"]
        year = load_data["year"]
        player = load_data["player"]
        life_story = load_data["life_story"]
        is_finished = load_data["is_finished"]
        past_lives = load_data.get("past_lives", []) # 讀取過去人生清單
else:
        name = input("請輸入姓名：") or "無名氏" # 請玩家輸入


if is_finished == True: # 如果遊戲結束狀態為True，代表玩家已經玩過這個遊戲，詢問是否轉生
    reborn = input("是否要轉生？(輸入y轉生，其他任意鍵離開)")
    if reborn == "y":
        last_life = {
        "name": name,
        "age": age,
        "year": year,
        "player": player,
        "life_story": life_story,
        "is_finished": is_finished
        }
        past_lives.append(last_life) # 將上一世的資料加入過去人生清單
        age = 0
        year = 1
        life_story = []
        is_finished = False
        player = {
            "health" : 50,
            "intelligence" : 30,
            "social" : 20,
            "energy" : 40,
            "money" : 8000
        }
        name = input("請輸入姓名：") or "無名氏" # 請玩家輸入
        save_game(name, age, year, player, life_story, is_finished, past_lives) # 儲存最新一世的初始資料和歷代資料
    else:
        print("感謝遊玩，遊戲結束！")
        exit() # 結束程式

#呼叫函式
say_hello(name)
show_player(name, age, player)


print()
print("=================================")
print("你的人生冒險正式開始！")# 起始語
print("=================================")
print()
is_saved = False # 設定一個變數 叫儲存狀態 設定一開始是沒儲存False




# 04遊戲主迴圈
while is_finished ==False: # 當遊戲結束狀態為False時，進入遊戲主迴圈:
    print("╔══════════════════════════════╗")
    print(f"   🌅 人生冒險 第 {year} 年")
    print("╚══════════════════════════════╝")

    print()
    print("今年想做些什麼呢？") # 選擇行動
    print()
    print("🏃 1. 運動(健康 +10)")
    print("📚 2. 學習(智力 +10)")
    print("☕ 3. 社交(社交 +10)")
    print("🛌 4. 休息(體力 +10)")
    print("💼 5. 工作(存款 +1000)")
    print("💀 6. 結束此生")
    print("💾 7. 儲存並離開")
    print()

    
    choice = input("請選擇你的行動：")
    #判斷行動
    if choice == "1":
        increase_stat(player, "health") # 呼叫函式 健康增加10
        print("你選擇了運動，今年讓健康有所提升！")
        life_story.append(f"第{year}年：運動") # 將行動加入人生故事

    elif choice == "2":
        increase_stat(player, "intelligence")
        print("你選擇了學習，變聰明了一點！")
        life_story.append(f"第{year}年：學習")

    elif choice == "3":
        increase_stat(player, "social")
        print("你選擇了社交，人際加分！")
        life_story.append(f"第{year}年：社交")

    elif choice == "4":
        increase_stat(player, "energy")
        print("你選擇了休息，體力恢復中！")
        life_story.append(f"第{year}年：休息")    
    
    elif choice == "5":
        if player["energy"] < 10: # 體力需大於10才能工作
            print("你太累了，沒有體力工作，先休息吧！")
            continue
        player["money"] = earn_money(player["money"], 1000) # 每次賺1000
        player["money"] = min(player["money"], 20000) # 限制存款上限為20000
        decrease_stat(player, "energy") # 減少體力
        print("你選擇了工作，存款增加！")
        life_story.append(f"第{year}年：工作")
    
    elif choice == "6":
        print("你決定結束這段人生")
        break

    elif choice == "7":
        save_game(name, age, year, player, life_story, is_finished, past_lives) # 呼叫函式:儲存遊戲
        is_saved = True # 儲存狀態改為save
        print("💾紀錄已儲存")
        break

    else:
        print("無效的選項，請重新選擇！") # 如玩家輸入錯誤請重新選擇
        continue # 重新回到這個迴圈開頭

    # 05設定隨機事件、能力值更新與死亡判定
    event = random.randint(1, 10) # 產生事件
    print()
    print("===========突發事件！=============")
    if event == 1:
        print("下班途中撿到500元！(存款+500)")
        player["money"] = min(player["money"] + 500, 20000) # 賺500，限制存款上限為20000
        life_story.append(f"第{year}年，撿到500元！") # 將隨機事件加入人生故事

    elif event == 2:
        print("錢包被偷(存款-1000)")
        player["money"] -= 1000
        life_story.append(f"第{year}年，錢包被偷...")

    elif event == 3:
        print("讀到一本好書(智力+10)")
        increase_stat(player, "intelligence")
        life_story.append(f"第{year}年，讀到一本好書")

    elif event == 4:
        print("熬夜打遊戲，腦袋昏沉(智力-10)")
        decrease_stat(player, "intelligence")
        life_story.append(f"第{year}年，熬夜打遊戲，腦袋昏沉")

    elif event == 5:
        print("偶遇老朋友(社交+10)")
        increase_stat(player, "social")
        life_story.append(f"第{year}年，偶遇老朋友")

    elif event == 6:
        print("訊息被已讀不回(社交-10)")
        decrease_stat(player, "social")
        life_story.append(f"第{year}年，訊息被已讀不回")

    elif event == 7:
        print("泡溫泉放鬆身心(健康+10)")
        increase_stat(player, "health")
        life_story.append(f"第{year}年，泡溫泉")

    elif event == 8:
        print("感冒了...(健康-10)")
        decrease_stat(player, "health")
        life_story.append(f"第{year}年，感冒了")

    elif event == 9:
        print("午睡30分鐘 充電成功！(體力+10)")
        increase_stat(player, "energy")
        life_story.append(f"第{year}年，午睡30分鐘")

    elif event == 10:
        print("踩到狗大便 幹(體力-10)")
        decrease_stat(player, "energy")
        life_story.append(f"第{year}年，踩到狗屎")


    
    print("=================================")
    print("今日行動完成！目前能力值") # 顯示能力值
    print()
    print(f"╭────────── 🌿 第{year}年生活狀態 ──────────╮")
    show_stat("❤️  健康：", player["health"])
    show_stat("📚 智力：", player["intelligence"])
    show_stat("☕ 社交：", player["social"])
    show_stat("⚡ 體力：", player["energy"])
    filled = max(player["money"] // 2000, 0) # 計算存款的進度條長度，存款金額除以2000，進度條"方格"最小值為0格
    print(f"{'│💰 存款：':<4}{'█' * filled + '░' * (10 - filled)} NT$ {player['money']:>6,}/20,000 │")
    print("╰──────────────────────────────────────╯")
    print()

    chance_1 = death_rate(age, player["health"], player["energy"]) # 一年結束，計算目前的死亡機率
    roll_1 = random.randint(1, 100) # 產生一個1~100的亂數，來判斷玩家是否死亡
    if roll_1 <= chance_1: # 先判斷玩家是否死亡
        chance_2 = natural_death_rate(age) # 死亡了那就開始計算自然死亡的機率
        roll_2 = random.randint(1, 100) # 產生一個1~100的亂數，來判斷是自然死亡還是意外死亡
        if roll_2 <= chance_2: # 自然死亡
            disease = ["中風", "器官衰竭", "心肌梗塞"] # 設定自然死亡的死因 (產生一個死因清單)
            cause_1 = random.choice(disease) # 隨機選擇一個死因 (設定cause_1這個變數來隨機選擇disease這個清單裡的死因)
            print(f"你已死亡，死因為：{cause_1}")  
            life_story.append(f"於{age}歲因{cause_1}死亡")
        else: # 意外死亡
            accident = ["車禍", "遭仇人謀殺", "火災受困"]
            cause_2 = random.choice(accident)
            print(f"你已死亡，死因為：{cause_2}")
            life_story.append(f"於{age}歲因{cause_2}死亡")
  

        break

    year = year + 1
    age  = age + 1
print("=================================")
#06遊戲結算與最終存檔

if is_saved == False:
    print("人生旅程結束，遊戲結算！")
    if player["energy"] >= 70:
        ending = "人生結局：御宅族" # 設定一個ending變數，來存放玩家的結局
        print("你的人生結局：御宅族")

    elif player["money"] >= 11000:
        ending = "人生結局：工作狂"
        print("你的人生結局：工作狂")

    elif player["health"] >= 80:
        ending = "人生結局：健身達人"
        print("你的人生結局：健身達人")


    elif player["intelligence"] >= 60:
        ending = "人生結局：學霸線"
        print("你的人生結局：學霸線")

    elif player["social"] >= 50:
        ending = "人生結局：社交牛逼症"
        print("你的人生結局：社交牛逼症")

    else:
        ending = "人生結局：平平無奇的人"
        print("你的人生結局是：平平無奇的人")
    life_story.append(ending) # 把結局放進人生故事清單裡
    print()
    print(f"{name}的故事回顧")
    print()
    for item in life_story: # 用迴圈的方式把人生故事清單裡的每一個項目都印出來
        print(item)
    is_finished = True # 設定遊戲結束狀態為True
    save_game(name, age, year, player, life_story, is_finished, past_lives) # 呼叫函式:儲存遊戲

