import streamlit as st
import time
from PIL import Image
import pandas as pd
pd.set_option('display.max_colwidth', -1)

st.title("強さスカウター")
"""
## あなたの強さ
"""
image = Image.open("fukkin_man.png")
st.image(image,caption="あなたのイマの強さを出してみよう！",use_column_width =False)
annual_income = st.number_input("年収（万円）",0,10000000,0)
"あなたの年収:",annual_income,"万円"
follower = st.number_input("総SNSフォロワー数（人）",0,10000000000,0)
"あなたのSNSフォロワー数:",follower,"人"
grip_strength = st.number_input("握力合計(Kg)",0,300,0)
"あなたの握力合計（kg）:",grip_strength,"kg"
"""
## あなたの属性
"""

sex_options = ["男性","女性"]
sex=st.selectbox("あなたの性別",sex_options)
#age_options = ["10代","20代","30代","40代","50代","60代","70代~"]
age=st.number_input("年齢",0,200,0)
work = st.text_input("あなたの職業")

if annual_income is not None and follower is not None and grip_strength is not None: 
    your_power = int(annual_income)*int(follower)*int(grip_strength)
    "あなたの力：",str(your_power)
    user_data_dict = {
        "年収":annual_income,
        "SNSフォロワー":follower,
        "握力":grip_strength,
        "性別":sex,
        "年齢":age,
        "職業":work,
        "強さ":your_power
    }
    data_dict_list = []
    data_dict_list.append(user_data_dict)
    user_data_pdf = pd.DataFrame(data_dict_list)
    st.dataframe(user_data_pdf.style.hide_index())
    #width=1000,height=100)
else:
    pass