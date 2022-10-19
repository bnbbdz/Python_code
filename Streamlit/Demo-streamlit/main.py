import streamlit as st
from utils import display_text, input_data, predict_income
from model import IncomePrediction

model_ip = IncomePrediction()

if __name__ == "__main__":

    rad = st.sidebar.radio("Navigation", (
        'Display text',
        'Input data',
        'Income-prediction model'
    ), index=0)

    if rad == "Display text":
        display_text()
    elif rad == "Input data":
        input_data()
    elif rad == "Income-prediction model":
        predict_income(model_ip)
