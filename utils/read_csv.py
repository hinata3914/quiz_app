import pandas as pd
import os


def read_csv(app, file_name="data.csv"):
    path = os.path.join(app.root_path, "static", file_name)
    df = pd.read_csv(path)
    return df


def get_dish_data(app):
    quiz_df = read_csv(app)

    quiz_df.columns = quiz_df.columns.str.strip()  # カラム名の空白を削除
    quiz_df["imagepath"] = quiz_df["imagepath"].str.strip()  # 値の空白も削除

    dish = quiz_df.sample(n=1).iloc[0]

    # 辞書化してテンプレートで使いやすくする
    dish_data = {
        "id": dish["id"],
        "name": dish["name"],
        "image": dish["imagepath"],
        "calorie": dish["calorie"],
    }
    return dish_data

def get_dish_data_by_id(app, dish_id):
    quiz_df = read_csv(app)
    
    quiz_df.columns = quiz_df.columns.str.strip()  # カラム名の空白を削除
    quiz_df["imagepath"] = quiz_df["imagepath"].str.strip()  # 値の空白も削除

    dish = quiz_df[quiz_df["id"] == dish_id].iloc[0]
    return {
        "id": dish["id"],
        "name": dish["name"],
        "image": dish["imagepath"],
        "calorie": dish["calorie"]
    }
