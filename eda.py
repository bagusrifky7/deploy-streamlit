# import libraries
import streamlit as st
import pandas as pd
from PIL import Image

def run():
    # judul
    st.title('Exploratory Data Analysis')

    # eda pertama
    st.subheader("Wordcloud Keseluruhan Pelanggan")
    Image_d1 = Image.open('images/eda_1.png')
    st.image(Image_d1)
    with st.expander("Penjelasan"):
        st.caption("Berdasarkan wordcloud diatas, kata-kata seperti , 'skin', 'moisturizer', dan 'serum' merupakan kata-kata yang sering muncul pada " \
        "review produk Sephora. Kata-kata yang sering muncul tersebut merupakan kategori produk yang dijual oleh Sephora yang mempunyai fokus pada produk " \
        "perawatan kulit. Kata-kata seperti 'good' dan 'great' juga sering muncul pada review produk mengindikasikan sentimen ke arah positif. Kata 'not' " \
        "yang muncul pada review pelanggan yang merekomendasikan produk ini belum tentu selalu berkonotasi negatif, bisa jadi kalimatnya seperti 'not disappointed'. " \
        "Kita bisa simpulkan kata-kata yang sering muncul mengarah ke sentimen positif dan pelanggan merekomendasikan produk Sephora.")

    # eda kedua
    st.subheader("Wordcloud Pelanggan Yang Merekomendasikan")
    Image_d2 = Image.open('images/eda_2.png')
    st.image(Image_d2)
    with st.expander("Penjelasan"):
        st.caption("Wordcloud diatas merupakan isi kata-kata dari review pelanggan yang merekomendasikan produk. Kata-kata yang sering muncul seperti 'moisturizer', " \
        "'serum', dan 'cleanser' pada review produk pelanggan yang merekomendasikan merupakan indikasi jenis-jenis produk Sephora yang paling sering dibeli oleh " \
        "pelanggan. Kita bisa melihat kata 'smell' dan 'smooth' paling sering muncul di review pelanggan, mengindikasikan bahwa pelanggan yang merekomendasikan " \
        "produk suka dengan bau dan kelembutan produk-produk Sephora pada kulit.")

    # eda ketiga
    st.subheader("Wordcloud Pelanggan Yang Tidak Merekomendasikan")
    Image_d3 = Image.open('images/eda_3.png')
    st.image(Image_d3)
    with st.expander("Penjelasan"):
        st.caption("Berdasarkan wordcloud diatas, kata-kata seperti 'smell', 'not, dan 'price' sering muncul pada review pelanggan yang tidak merekomendasikan. " \
        "Ini mengindikasikan produk yang tidak merekomendasikan produk Sephora kurang cocok dengan bau dan harga dari produk Sephora. Kata 'moisturizer' juga " \
        "sering muncul, mengindikasikan produk dengan kontribusi tidak direkomendasikan terbanyak. Ini terjadi karena moisturizer merupakan barang yang paling " \
        "umum dibeli dari produk-produk Sephora.")

    # eda keempat
    st.subheader("Top 10 Kata Dengan Frekuensi Terbanyak")
    Image_d4 = Image.open('images/eda_4.png')
    st.image(Image_d4)
    with st.expander("Penjelasan"):
        st.caption("Berdasarkan bar chart diatas, kata-kata seperti 'love', 'like, dan 'great' berada di top 10 frekuensi kata yang muncul pada " \
        "review pelanggan keseluruhan. Kata-kata seperti 'skin', 'product', dan 'face' berada di top 10 kata yang paling sering muncul, " \
        "mengindikasikan bahwa review tersebut berhubungan dengan produk Sephora yang memang berhubungan dengan skincare. " \
        "Kita bisa simpulkan berdasarkan bar chart ini, pelanggan mempunyai sentimen yang positif terhadap produk skincare Sephora.")
        
    # eda kelima
    st.subheader("Top 10 Kata Dengan Frekuensi Kemunculan Terbanyak dari Review Pelanggan Yang Merekomendasikan")
    Image_d5 = Image.open('images/eda_5.png')
    st.image(Image_d5)
    with st.expander("Penjelasan"):
        st.caption("Bar chart diatas berisi top 10 kata-kata yang paling sering muncul pada review pelanggan yang merekomendasikan produk Sephora. " \
        "Kita bisa melihat sentimen ke arah positif dengan adanya kata-kata seperti 'great', 'love', dan 'like'. Pada bar chart ini juga " \
        "terdapat kata-kata seperti 'skin', 'face', dan 'product' yang mengarah kepada produk-produk Sephora yang mempunyai fokus pada perawatan " \
        "kulit dan wajah. Kata 'not' yang seharusnya merupakan stopwords tidak mengindikasikan sentimen negatif, contohnya 'not disappointed'. " \
        "Kita bisa simpulkan pelanggan yang merekomendasikan produk skincare Sephora sangat menyukai produk-produk perawatan kulit terutama perawatan wajah.")

    # eda keenam
    st.subheader("Top 10 Kata Dengan Frekuensi Kemunculan Terbanyak dari Review Pelanggan Yang Merekomendasikan")
    Image_d6 = Image.open('images/eda_6.png')
    st.image(Image_d6)
    with st.expander("Penjelasan"):
        st.caption("Chart diatas merupakan bar chart dari top 10 Frekuensi kemunculan kata dari pelanggan yang tidak merekomendasikan produk Sephora. " \
        "Kita dapat melihat kata-kata seperti 'didnt' dan 'not' seharusnya masuk ke dalam stopwords, tetapi dalam kasus ini kata ketiga kata tersebut " \
        "dapat mengindikasikan sentimen produk ke arah negatif. Kata 'like' yang sering muncul pada chart ini juga mendukung statement sebelumnya, dimana kata " \
        "stopwords 'didnt' dan 'not' jika digabungkan dengan kata 'like' mengindikasikan sentimen mengarah ke negatif. Kita bisa simpulkan bahwa pelanggan yang " \
        "tidak merekomendasikan mengarah ke produk skincare Sephora, utamanya untuk kulit. Jumlah kemunculan kata pada pelanggan tipe ini lebih sedikit " \
        "dibandingkan dengan sentimen positif, menunjukkan bahwa kebanyakan dari pengguna produk Sephora menyukai produk-produknya.")    