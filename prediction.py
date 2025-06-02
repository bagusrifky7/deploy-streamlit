# import libraries
import numpy as np
import pandas as pd
import streamlit as st
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model

def run():

    # import model
    best_model = load_model('best_model.keras')
    # variabel untuk review pelanggan
    text = st.text_area(label = "Masukkan contoh review pelanggan")

    # membuat variabel untuk dataframe
    text = [text]
    data = pd.Series([text], name = 'review_text') 
    df = data.copy()
    
    # casting tipe data dan jadikan list
    df = df.astype(str).to_list()

    # ubah tf constant jadi tf.string
    df = tf.constant(df, dtype = tf.string)

    #fungsi untuk prediksi
    def predict_inf(df):
        y_pred = best_model.predict(df) # prediksi probabilitas
        y_pred = np.argmax(y_pred, axis = 1) # ambil yang terbaik
        
        # deklarasi if dan elif
        if y_pred == 1:
            return st.write('Pelanggan merekomendasikan produk')
        else:
            return st.write('Pelanggan tidak merekomendasikan produk')

    # deklarasi if untuk prediksi
    if st.button(label = 'predict'):
        predict_inf(df)