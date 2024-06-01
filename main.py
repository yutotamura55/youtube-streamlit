import streamlit as st
import time

st.title('Streamlit 入門')

st.write('プログレスバーの表示')
'Start!!'
latest_iteration = st.empty()

bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = []
for idx in range(0,4):
    expander.append(st.expander(f'問い合わせ{idx}'))
    expander[idx].write(f'問い合わせ{idx}の回答')
# text = st.text_input('アナタの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの趣味：', text
# 'コンディション：', condition

# if st.checkbox('ShowImage'):
#     img = Image.open('image01.jpg')
#     st.image(img, caption='sample', use_column_width=True)



