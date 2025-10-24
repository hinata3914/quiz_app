from flask import Flask, render_template, request
import random
import pandas as pd
import os
from utils.read_csv import get_dish_data, get_dish_data_by_id

app = Flask(__name__)


@app.route("/")
def index():
    dish_data = get_dish_data(app)

    # 正解＋ダミーの選択肢を作成
    choices = [dish_data["calorie"], 400, 700, 900]
    random.shuffle(choices)
    return render_template("index.html", dish=dish_data, choices=choices)


@app.route("/check/<int:dish_id>", methods=["POST"])
def check(dish_id):
    dish_data = get_dish_data_by_id(app, dish_id)
    
    selected = int(request.form["answer"])
    
    if selected == dish_data["calorie"]:
        result = "🎉 正解！"
    else:
        result = f"❌ 不正解… 正解は {dish_data['calorie']} kcal でした！"

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
