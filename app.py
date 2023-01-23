annual_income = st.selectbox(
    "あなたの年収を教えて下さい",
    list(range(1,100000))
)
"年収", annual_income,"です。"


follower = st.selectbox(
    "あなたが好きな数字を教えて下さい",
    list(range(1,1000000000))
)
"フォロワー数", follower,"です。"

big3 = st.selectbox(
    "あなたが好きな数字を教えて下さい",
    list(range(1,1000))
)
"big3", big3,"です。"


power = int(annual_income)*int(follower)*int(big3)/1000000

#"あなたの強さ:",int(annual_income)*int(follower)*int(big_3)/1000000
"あなたの強さ:",power

#if annual_income is not None and follower is not None and big_3 is not None:
#if annual_income is not None and follower is not None and big_3 is not None:
if annual_income is not None:
    st.write("## 3つとも値を入れてください")
else:
    power = int(annual_income)*int(follower)*int(big_3)
    "あなたの力：",str(power)