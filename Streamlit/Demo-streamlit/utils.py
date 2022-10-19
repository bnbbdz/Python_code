import pandas as pd
import streamlit as st

def display_text():
    st.title("Cỡ chữ của title")
    st.header("Cỡ chữ của header")
    st.subheader("Cỡ chữ của subheader")
    st.text("Cỡ chữ của text")
    st.markdown(""" # markdown: h1 tag
    ## markdown: h2 tag
    ### markdown: h3 tag
    
    markdown :sunglasses:

    **markdown: chữ in đậm**

    _markdown: chữ in nghiêng_
    """, True)

def input_data():
    st.title("Data")
    st.subheader("Nhập free text")
    name = st.text_input("Mời bạn nhận tên")
    st.write(f"Tên của bạn là: {name}")
    st.write("\n")

    st.subheader("Nhập text ở dạng ngày")
    date = st.date_input("Mời bạn chọn ngày")
    st.write(f"Hôm nay là ngày: {date}")
    st.write("\n")

    st.subheader("Nhập text ở dạng giờ")
    time = st.time_input("Mời bạn chọn giờ")
    st.write(f"Bây giờ là: {time}")
    st.write("\n")

    st.subheader("Lựa chọn text ở dạng radio")
    color = st.radio("Lựa chọn màu sắc yêu thích", ["xanh", "đỏ", "vàng"], index=1)
    st.write(f"Màu sắc yêu thích của bạn là: {color}")
    st.write("\n")

    st.subheader("Lựa chọn text ở dạng select-box")
    color = st.selectbox("Lựa chọn màu sắc yêu thích", ["xanh", "đỏ", "vàng"], index=0)
    st.write(f"Màu sắc yêu thích của bạn là: {color}")
    st.write("\n")

    st.subheader("Lựa chọn text ở dạng multi-select")
    color = st.multiselect("Lựa chọn màu sắc yêu thích", ["xanh", "đỏ", "vàng"])
    st.write(f"Màu sắc yêu thích của bạn là: {color}")
    st.write("\n")
    
    st.subheader("Lựa chọn text ở dạng slider")
    age = st.slider("Mời bạn nhập tuổi", min_value=18, max_value=60, value=30, step=2)
    st.write(f"Tuổi của bạn là: {age}")
    st.write("\n")

    st.subheader("Lựa chọn number")
    number = st.number_input("Mời bạn nhập số yêu thích", min_value=18.0, max_value=60.0, value=30.0, step=1.0)
    st.write(f"Con số yêu thích của bạn là: {number}")
    st.write("\n")

    st.subheader("Upload a file")
    try:
        file_upload = st.file_uploader("Mời bạn tải lên file xlsx")
        content = pd.read_excel(file_upload)
        st.write("File của bạn có nội dung là:")
        st.dataframe(content)
        st.write("\n")
    except:
        pass

def predict_income(model):
    st.title("Income Prediction")
    col1, col2, col3 = st.columns(3)
    with col1:
        name = st.text_input("Mời bạn nhập tên")
    with col2:
        age = st.number_input("Mời bạn nhập tuổi", min_value=18, max_value=60, value=25, step=1)
    with col3:
        occupation = st.selectbox("Mời bạn chọn nghề nghiệp", ["Data Scientist", "Data Engineer", "Data Analyst", "AI Engineer"], index=0)
    
    if name and age and occupation:
        income_predicted = model.predict(name, age, occupation)
        st.write(f"Bạn tên là **{name}**.")
        st.write(f"Bạn **{age}** tuổi.")
        st.write(f"Bạn làm nghề **{occupation}**.")
        st.write(f"Thu nhập của bạn được dự đoán là **{income_predicted}** dolars.")
