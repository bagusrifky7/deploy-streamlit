# import libraries
import streamlit as st
import pandas as pd
import eda
import prediction

# Sidebar navigation
page = st.sidebar.selectbox(
    label='Select Page',
    options=['Introduction', 'Exploratory Data Analysis', 'Model Prediction']
)

if page == 'Introduction':
    # Introduction Page
    st.title('Graded Challenge 7')
    st.write('**Name:** Bagus Rifky Riyanto')
    st.write('**Batch:** HCK-27')

    # later belakang
    with st.expander('Latar Belakang'):
        st.caption(
            "Review pelanggan merupakan salah satu hal yang penting dalam mengembangkan produk agar menjadi lebih berkualitas dan unggul. " \
            "Untuk meningkatkan kualitas produk, kita bisa melihat bagaimana pelanggan merespon setelah menggunakan produk yang dibuat. " \
            "Setiap review sangat berguna dalam meningkatkan kualitas produk. " \
            "Dari review tersebut dapat menjadi indikasi apa saja yang bisa dipertahankan dari kualitas produk dan pelayanan kepada pelanggan. " \
            "Review negatif dapat menjadi indikasi apa saja yang dapat ditingkatkan dari kualitas produk."
        )

    # deskripsi dataset
    with st.expander('Deskripsi Dataset'):
        st.caption(
            "Dataset ini berisi informasi tentang informasi review pelanggan terhadap produk Sephora. Kolom dari dataset ini terdiri dari author_id, " \
            "rating, is_recommended, helpfulness, total_feedback_count, total_neg_feedback_count, total_pos_feedback_count, submission_time, " \
            "review_text, review_title, skin_tone, eye_color, skin_type, hair_color, product_id, product_name, brand_name, dan price_usd."
        )

    # Pernyataaan masalah
    with st.expander('Pernyataan Masalah'):
        st.caption(
            " Menganalisis review pelanggan merupakan hal yang krusial dalam menentukan bagaimana respon pelanggan terhadap produk yang dijual. " \
            "Kita bisa mengetahui bagaimana komplain atau pujian pelanggan melalui wordcloud yang menghasilkan frekuensi kata-kata " \
            "terbanyak pada pelanggan yang merekomendasikan dan tidak merekomendasikan. Tidak hanya itu, kita bisa memprediksi apakah " \
            "pelanggan akan merekomendasikan produk tersebut atau tidak, sehingga kita dapat mengetahui bagaimana performa produk di pasaran. " \
            "Analisis tersebut akan berguna dalam membantu tim produk untuk meningkatkan kualitas produk dan pelayanan kepada pelanggan. " \
            "Metrik yang digunakan adalah precision untuk mengetahui bagaimana model dalam memprediksi apakah suatu pelanggan benar-benar merekomendasikan atau tidak."
        )

    # Tujuan
    with st.expander('Tujuan'):
        st.caption(
            " Tujuan dari analisis ini adalah menganalisis review pelanggan produk Sephora, " \
            "dan membantu tim produk dalam menentukan apakah pelanggan akan merekomendasikan produk tersebut atau tidak."
        )

    # Kesimpulan
    with st.expander('Kesimpulan'):
        st.caption(
            "Berdasarkan analisis yang sudah dilakukan, kita bisa simpulkan bahwa hasil bagus yang didapatkan dari proses inference " \
            "kemungkinan hanya kebetulan semata. Ini dikarenakan model overfit dari kurva loss vs val loss, sehingga saat diberikan " \
            "data yang berbeda belum tentu dapat memprediksi pelanggan dengan baik."
        )

    # Rekomendasi
    with st.expander('Rekomendasi'):
        st.caption(
            "Kedepannya disarankan untuk memperkecil nilai patience pada regularisasi early stopping misalnya 3 agar tidak terlalu " \
            "lama dalam memonitor semakin besarnya nilai loss. Data yang digunakan bisa dengan data dengan kelas yang lebih seimbang, " \
            "agar prediksi lebih akurat dan tidak menimbulkan bias yang besar pada kelas mayoritas, serta mengurangi kecenderungan overfitting. " \
            "Struktur dengan tipe functionial bisa diterapkan kedepannya agar model punya modifikasi yang lebih baik lagi dengan kebebasan " \
            "yang tersedia pada struktur functional."
        )

elif page == 'Exploratory Data Analysis':
    eda.run()

elif page == 'Model Prediction':
    prediction.run()
    
