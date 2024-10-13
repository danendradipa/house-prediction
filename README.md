# House Price Prediction using Linear Regression 🏡
## Project Overview:
This project aims to predict house prices based on various features such as building area, land area, number of bedrooms, bathrooms, and garages using Multiple Linear Regression. 

## Key Features:
- 🏠 House Price Prediction: Using Multiple Linear Regression to predict house prices.
- 🧮 Algorithm Used: Linear Regression implemented with Scikit-learn
- 🛠 Tools and Technologies:
  - Scikit-learn for linear regression modeling.
  - Pandas and Numpy for data manipulation and processing.
  - Matplotlib/Seaborn for data visualization.
  - Streamlit for building an interactive web app (if applicable).
    
## Dataset:

The dataset contains detailed information about house listings, including features that affect the price. The dataset can be accessed from Kaggle at the following link: [Kaggle](https://www.kaggle.com/datasets/wisnuanggara/daftar-harga-rumah).

- Features:
  - Luas Bangunan: Building area in square meters.
  - Luas Tanah: Land area in square meters.
  - Kamar Tidur: Number of bedrooms.
  - Kamar Mandi: Number of bathrooms.
  - Garasi: Number of garages.
- Target:
  - Harga: The price of the house in Rupiah.

## Installation:

1. Clone the repository:
    ```bash
    https://github.com/danendradipa/house-prediction.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## How to run:

1. Run the Streamlit app using the command:

    ```bash
    streamlit run house_predict.py
    ```
