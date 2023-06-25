# Stock Prediction Web App

## Table of Contents
  * [Overview](#overview)
  * [Description](#description)
  * [Project Structure](#project-structure)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Technologies Used](#technologies-used)
  * [License](#license)

## Overview
# Important: Please see the demonstration video to see how the Stock Prediction Web App works.
This project is a web application that predicts stock prices using LSTM model. It provides users with the ability to input a stock name and view the predicted stock prices based on historical data. The application utilizes the Yahoo Finance API to fetch stock data, performs data preprocessing and scaling, and employs a pre-trained deep learning model for prediction.

## Description
The Stock Prediction Web App allows users to enter the name of a stock and view descriptive statistics of the stock's historical data. It also provides the option to visualize the stock's trendlines, including the moving average trendline. Additionally, the app utilizes a deep learning model called LSTM to predict future stock prices based on the input data.

## Project Structure
The project consists of the following main files:
- `stock_prediction_webapp.py`: This file contains the code for the Streamlit web application, including fetching stock data, data preprocessing, visualization, and prediction.
- `stock_price_model.ipynb`: This Jupyter Notebook file contains the code for training the deep learning model to predict stock prices.

## Installation
To run the Stock Prediction Web App locally, follow these steps:
1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Make sure you have Python 3.7 or higher installed.
4. Run the command `streamlit run stock_prediction_webapp.py` to start the web application.

## Usage
1. Enter the name of a valid stock in the provided text input field.
2. The application will fetch the stock's historical data and display descriptive statistics.
3. Choose a trendline option from the dropdown menu to visualize the stock's trendline.
4. Enable the moving average checkbox to overlay the moving average trendline on the stock's data plot.
5. The application also shows the predicted stock prices using the pre-trained deep learning model.

## Technologies Used
- Python
- Pandas
- Pandas DataReader
- NumPy
- Matplotlib
- Seaborn
- Plotly Express
- Scikit-learn
- TensorFlow
- Streamlit

## License
This project is licensed under the [MIT License](LICENSE).
