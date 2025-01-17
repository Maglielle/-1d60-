import streamlit as st
import random
import time

# ����Ƒ����̃��X�g
weapons = [
    "�G�N�X�J���o�[", "�w���N���X", "�Q�C�{���O", "�_�}�X�J�X�i�C�t",
    "�J�h�D�P�E�X", "�~�����j��", "�t���C�N�[�Q��", "���V�持",
    "�E�����N���~", "�V�H�X�a"
]

elements = ["��", "��", "�y", "��", "��", "��"]

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
    st.subheader("?? �T�C�R�����ʈꗗ")
    for num, (elem, weap) in mapping.items():
        if num == final_roll:
            st.markdown(f"**?? {num}: {elem} {weap}**")
        else:
            st.markdown(f"{num}: {elem} {weap}")

# Streamlit�A�v���̐ݒ�
st.title("�X�y���I���V���[�Y���탉���_�����I")
st.write("**�����_���ŕ���Ƒ�����I�т܂��I**")

if st.button("���I����I"):
    roll_mapping = generate_roll_mapping()
    final_roll = roll_animation(roll_mapping)
    final_element, final_weapon = roll_mapping[final_roll]
    display_results(roll_mapping, final_roll)
    st.success(f"�ŏI�I�ɑI�΂ꂽ�̂� **{final_roll}** �� **{final_element} {final_weapon}** �ł��I")
