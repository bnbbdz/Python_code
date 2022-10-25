import streamlit as st
import pandas as pd
import numpy as np
# from st_aggrid import GridOptionsBuilder, GridUpdateMode, DataReturnMode, JsCode , AgGrid
import time
import datetime

st.set_page_config(
page_title="TRA CUU DU LIEU",
page_icon="y",
layout="wide",
initial_sidebar_state="expanded",
)

today = datetime.datetime.today().strftime('%d/%m/%Y')

st.title('TRA CUU DU LIEU')

#Display the grid
st.header("Du lieu diem thi dai hoc nam 2020")

st.markdown("""
    Du lieu cap nhat den {}
""".format(today))

# url = r'D:\Python + SQL + R\Python_dunglai\clean_data_2.csv'
# data = pd.read_csv(url)
# uppercase = lambda x: str(x).upper()
# data.rename(uppercase, axis='columns', inplace=True)

st.sidebar.image('data:image/jpeg;base64,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')
#Example controlers
st.sidebar.subheader("Control tab")

# form = st.sidebar.form("my_form")
# form.form_submit_button("Import file")

# ten_hs = st.sidebar.text_input('Ten thi sinh',value='Nguyễn Mạnh Cường')
# sbd = st.sidebar.number_input('So bao danh', min_value=1955, max_value=2005, value=2002)
# nam_sinh = st.sidebar.number_input('Nam sinh', min_value=1955, max_value=2074718, value=2000001)

# st.markdown("""
#     Du lieu filter
# """)

# if ten_hs == 'Nguyễn Mạnh Cường' or ten_hs is None :
#     st.write(data)
# else:
#     st.write(data[data.TÊN == ten_hs])     


st.markdown("""
    Du lieu full
""")
# AgGrid(data)