import streamlit as st
import time

st.title(" 強さスカウター")



annual_income = st.text_input("年収（万円）")
"あなたの年収:",annual_income,"万円"
follower = st.text_input("最も多いSNSフォロワー数（人）")
"あなたのSNSフォロワー数:",follower,"人"
big_3 = st.text_input("BIG3合計(Kg)")
"あなたのBIG3（kg）:",big_3,"kg"

power = int(annual_income)*int(follower)*int(big_3)

"あなたの力：",str(power)