import streamlit as st
import random
import time

# 武器と属性のリスト
weapons = [
    "エクスカリバー", "ヘラクレス", "ゲイボルグ", "ダマスカスナイフ",
    "カドゥケウス", "ミョルニル", "フライクーゲル", "方天画戟",
    "ウルリクムミ", "天羽々斬"
]

elements = ["火", "水", "土", "風", "光", "闇"]

def generate_roll_mapping():
    return {i: (random.choice(elements), random.choice(weapons)) for i in range(1, 61)}

def roll_animation(mapping):
    roll_placeholder = st.empty()
    for i in range(30):
        dice_roll = random.randint(1, 60)
        elem, weap = mapping[dice_roll]
        roll_placeholder.markdown(f"?? **{dice_roll}** : {elem} {weap}")
        time.sleep(0.05 + i * 0.002)
    return random.randint(1, 60)

def display_results(mapping, final_roll):
    st.subheader("?? サイコロ結果一覧")
    for num, (elem, weap) in mapping.items():
        if num == final_roll:
            st.markdown(f"**?? {num}: {elem} {weap}**")
        else:
            st.markdown(f"{num}: {elem} {weap}")

# Streamlitアプリの設定
st.title("スペリオルシリーズ武器ランダム抽選")
st.write("**ランダムで武器と属性を選びます！**")

if st.button("抽選する！"):
    roll_mapping = generate_roll_mapping()
    final_roll = roll_animation(roll_mapping)
    final_element, final_weapon = roll_mapping[final_roll]
    display_results(roll_mapping, final_roll)
    st.success(f"最終的に選ばれたのは **{final_roll}** → **{final_element} {final_weapon}** です！")
