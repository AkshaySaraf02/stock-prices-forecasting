import pandas as pd
import pandas_datareader as data
import numpy as np

from PIL import Image

import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

import streamlit as st

import warnings
warnings.filterwarnings("ignore")


iconImage = Image.open("Stocks icon.png")

st.set_page_config(page_title="Stocks Guru", page_icon=iconImage)
st.markdown(""" 
            <style>
            footer {visibility: hidden;}
            </style>
            """, unsafe_allow_html=True)

st.title("Stock Prediction Web App")
userInputTicker = st.text_input("Enter Stock Name: ", "")

if userInputTicker:
    try:
        df = data.DataReader(userInputTicker.upper(), "yahoo",
                             start="2015-01-01", end="2022-10-09")

    except:
        st.write("Please Enter a Valid Ticker")
    st.write(df.describe()[1:])

    st.subheader("Choose trendline: ")
    colSelection = st.selectbox(
        options=["", "Open", "Low", "High", "Close ", "Adj Close", "Volume"],
        label="")

    if colSelection in df.columns:
        movingAvg = st.checkbox("Moving Average")
        if movingAvg:
            lengthMA = st.text_input("Enter period of Moving  Average")
            if lengthMA:
                st.subheader(f"{colSelection} Trendline")
                trend = plt.figure(figsize=(14, 6))
                plt.plot(df[colSelection], "b")
                plt.plot(df[colSelection].rolling(int(lengthMA)).mean(), "r")
                st.pyplot(trend)
        else:
            st.subheader(f"{colSelection} Trendline")
            trend = plt.figure(figsize=(14, 6))
            plt.plot(df[colSelection], "b")
            st.pyplot(trend)

        testSplit = int(len(df) * 0.7)
        trainData = pd.DataFrame(df["Open"][:testSplit])
        testData = pd.DataFrame(df["Open"][:testSplit])

        # Taking last 100 days to predict the first testing value and then so on.
        past_100_days = trainData.tail(100)
        inputDf = past_100_days.append(testData, ignore_index=True)

        scaler = MinMaxScaler()
        # Transforming the new input data.
        inputDf = scaler.fit_transform(inputDf)

        # Splitting into x and y (For Testing set)
        xTest = []
        yTest = []

        for i in range(100, inputDf.shape[0]):
            xTest.append(inputDf[i-100:i])
            yTest.append(inputDf[i, 0])

        # Converting testing data into numpy arrays
        xTest, yTest = np.array(xTest), np.array(yTest)

        model = load_model("stockPred.h5")
        prediction = model.predict(xTest)

        scalingFactor = scaler.scale_
        prediction = prediction * (1/scalingFactor)
        yTest = yTest * (1/scalingFactor)

        st.subheader("Prediction of the Model vs Actual Data")
        predFig = plt.figure(figsize=(14, 6))
        plt.plot(yTest, "black", label="Actual Open price of Stock")
        plt.plot(prediction, "green", label="Predicted Price")
        plt.legend()
        st.pyplot(predFig)


else:
    pass
