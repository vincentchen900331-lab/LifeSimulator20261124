"""
任務：建立一個玩家資料字典。

請完成以下要求：
1. 建立一個叫做 player 的字典。
2. 放入三筆初始資料：
   - "name"："Alex"
   - "health"：50
   - "money"：8000
3. 將健康值增加 20。
4. 新增 "intelligence"，數值為 60。
5. 刪除 "money" 這筆資料。
6. 使用 print() 印出整個字典。
7. 使用 print(len(player)) 印出目前有幾筆資料。
"""

player = {
    "name" : "Alex",
    "health": 50,
    "money": 8000
}
player["health"] += 20
player["intelligence"] = 60
del player["money"]

print(len(player))

"""
操作	語法
建立	player = {}
取得	player["health"]
修改	player["health"] = 80
新增	player["social"] = 40
運算	player["health"] += 10
刪除	del player["money"]
計算數量	len(player)

"""