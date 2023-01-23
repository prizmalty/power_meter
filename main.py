import streamlit as st
import time

st.title(" 強さスカウター")



#annual_income = st.text_input("年収（万円）")
annual_income = st.number_input("年収（万円）",0,10000000,0)
"あなたの年収:",annual_income,"万円"
#follower = st.text_input("最も多いSNSフォロワー数（人）")
follower = st.number_input("総SNSフォロワー数（人）",0,10000000000,0)
"あなたのSNSフォロワー数:",follower,"人"
#big_3 = st.text_input("BIG3合計(Kg)")
grip_strength = st.number_input("握力合計(Kg)",0,300,0)
"あなたの握力合計（kg）:",grip_strength,"kg"


if annual_income is not None and follower is not None and grip_strength is not None: 
    your_power = int(annual_income)*int(follower)*int(grip_strength)
    "あなたの力：",str(your_power)
else:
    pass