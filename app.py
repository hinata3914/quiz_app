from flask import Flask, render_template, request
import random
import pandas as pd
import os

app = Flask(__name__)


@app.route("/")
def index():
    csv_path = os.path.join(app.root_path, "static", "data.csv")
    quiz_df = pd.read_csv(csv_path)

    quiz_df.columns = quiz_df.columns.str.strip()  # カラム名の空白を削除
    quiz_df["imagepath"] = quiz_df["imagepath"].str.strip()  # 値の空白も削除

    dish = quiz_df.sample(n=1).iloc[0]
    
     # 辞書化してテンプレートで使いやすくする
    dish_data = {
        "name": dish["name"],
        "image": dish["imagepath"],
        "calorie": dish["calorie"]
    }

    # 正解＋ダミーの選択肢を作成
    choices = [dish["calorie"], 400, 700, 900]
    random.shuffle(choices)
    return render_template("index.html", dish=dish_data, choices=choices)


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
