import streamlit as st
import pandas as pd

df = pd.read_csv("./recipe_df_10E_ingredients_add.csv")

# 選択可能なタグを抽出
tags = []
for words in df["word"].values:
    for word in eval(words):
        if word not in tags:
            tags.append(word)

# タグを選択
selected_tags = st.multiselect("タグを選択してください", tags)
#st.write("選択されたタグ:", selected_tags)

# 選択されたタグが全て入っている料理の行を表示
filtered_df = df[df["word"].apply(lambda x: all(tag in eval(x) for tag in selected_tags))]

use_columns = ["料理名","URL","時間(分)"]
# URLをリンクとして表示する関数
st.dataframe(
    filtered_df[use_columns],
    column_config={
        "URL": st.column_config.LinkColumn(
            # 表示するカラム名
            "URL",
            # 表示データのテキスト
            display_text="https://(.*?)\.streamlit\.app"
        )
    },
)

