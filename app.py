from flask import Flask # 匯入工具  從flask 工具箱，拿出Flask(類別)

app = Flask(__name__) # 建立名為 app 的 Flask 網頁應用程式。__name__ 是 Python 自動提供的特殊變數名稱，
                      # 用來告訴 Flask 這個應用程式來自目前的 Python 檔案。

@app.route("/") # 設定「首頁有人來時，要找下面這段涵式。
def home(): # 定義一個叫 home 的函式；有人開首頁時就執行它。
    return "人生養成模擬器" # 把這段文字回傳給瀏覽器。

if __name__ == "__main__": # 如果目前檔案是直接被執行，就啟動 Flask 網頁伺服器。
    app.run(debug=True) # 以開發模式啟動；儲存程式後會自動重新載入。
