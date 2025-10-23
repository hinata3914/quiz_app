from flask import Flask, render_template, request
import random

app = Flask(__name__)

# クイズに使う料理データ
foods = [
    {"name": "カレー", "image": "curry.jpg", "calorie": 800},
    {"name": "ラーメン", "image": "ramen.jpg", "calorie": 600},
    {"name": "サラダ", "image": "salad.jpg", "calorie": 150},
]

@app.route("/")
def index():
    dish = random.choice(foods)
    # 正解＋ダミーの選択肢を作成
    choices = [dish["calorie"], 400, 700, 900]
    random.shuffle(choices)
    return render_template("index.html", dish=dish, choices=choices)

@app.route("/check", methods=["POST"])
def check():
    selected = request.form["answer"]
    correct = request.form["correct"]

    if selected == correct:
        result = "🎉 正解！"
    else:
        result = f"❌ 不正解… 正解は {correct} kcal でした！"

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
