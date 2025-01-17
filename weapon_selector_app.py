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
    # 属性のリストを武器の数に合わせて繰り返す
    extended_elements = (elements * ((len(weapons) // len(elements)) + 1))[:len(weapons)]
    
    # 武器と属性をシャッフルして1対1で割り当て
    shuffled_elements = random.sample(extended_elements, len(weapons))
    shuffled_weapons = random.sample(weapons, len(weapons))
    
    # シャッフルされたリストを使って、1対1でマッピング
    return {i: (shuffled_elements[i], shuffled_weapons[i]) for i in range(1, len(weapons) + 1)}

def roll_animation(mapping):
    roll_placeholder = st.empty()
    final_roll = None
    for i in range(30):
        dice_roll = random.randint(1, len(mapping))  # 武器と属性の数を基にロール
        elem, weap = mapping[dice_roll]
        roll_placeholder.markdown(f"{dice_roll} : {elem} {weap}")
        time.sleep(0.05 + i * 0.002)
        final_roll = dice_roll  # 最後に表示されたロールを保存
    return final_roll

def display_results(mapping, final_roll):
    st.subheader("?? サイコロ結果一覧")
    final_element, final_weapon = mapping[final_roll]
    for num, (elem, weap) in mapping.items():
        if num == final_roll:
            st.markdown(f"**?? {num}: {elem} {weap}**")
        else:
            st.markdown(f"{num}: {elem} {weap}")

# Streamlitアプリの設定
st.title("おすすめスペ武器は1D60!!")
st.write("**迷ったらコレ！**")

if st.button("抽選する！"):
    roll_mapping = generate_roll_mapping()
    final_roll = roll_animation(roll_mapping)
    final_element, final_weapon = roll_mapping[final_roll]
    st.success(f"あなたにピッタリの一本はコレ!! → **{final_element} {final_weapon}**")
    display_results(roll_mapping, final_roll)
