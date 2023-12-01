import streamlit as st

def app():

    st.markdown("""
    <div style="text-align:center">
        <h1>PREDIKSI DIABETES DILAYANAN KESEHATAN PRIMER WILAYAH TERPENCIL</h1>
    </div>
""", unsafe_allow_html=True)

    st.write("##")
    st.write("---")
    st.sidebar.success("Pilih Menu di atas.")

    # Tautan untuk logo 
    logo_url_1 = "https://d3q0fpse3wbo5h.cloudfront.net/production/uploads/innovations/OFA-Logo-01.jpg"

    # Menampilkan logo
    st.image(logo_url_1, use_column_width=True)

    st.write("---")
    st.write("##")
    st.markdown("""
    <div style="text-align:center">
        <h2>About</h2>
    </div>
""", unsafe_allow_html=True)

    text = """
    <div style="text-align: justify;">
    Lebih baik mencegah daripada mengobati. Rangkaian kata yang sering didengar bagi seseorang dengan garis keturunan yang memiliki riwayat penyakit diabetes, resiko terpapar penyakit tersebut pun lebih besar. Namun tidak semua orang beruntung dalam menghadapi hal itu. Seperti contohnya pada wilayah terpencil yang mungkin saja hanya mendapat sedikit edukasi mengenai diabetes.Oleh karena itu, kami menawarkan solusi dengan Aplikasi Prediksi Diabetes terhadap Pelayanan Kesehatan di Wilayah Terpencil. Aplikasi kami akan melakukan prediksi berdasarkan data pasien seperti kadar gula dan insulin yang ada pada tubuh pasien. Setelah pengguna memasukkan datanya, aplikasi akan melakukan proses prediksi dan mengeluarkan hasil dalam waktu kurang dari 3 detik. Tidak hanya itu, kami menyediakan playlist bagi pengguna yang ingin mengetahui informasi terkait penyakit diabetes. Teknologi ini kami bawa untuk meningkatkan angka kehidupan pada wilayah terpencil. Dengan aplikasi Prediksi Diabetes terhadap Pelayanan Kesehatan di Wilayah Terpencil, deteksi dini bukan lagi sekadar impian.
    </div>
    """
    st.markdown(text, unsafe_allow_html=True)

    st.write("##")
    st.write("##")
    
    gif_url = "https://www.bing.com/th/id/OGC.486c321c24737d07f121538d346ddd7c?pid=1.7&rurl=https%3a%2f%2f1.bp.blogspot.com%2f-x7vHwA9cxi8%2fT5CVr5ftAII%2fAAAAAAAAABE%2fmb4MBrNVkfo%2fs1600%2ffemale_pharmacist_fill_perscription_bottle_hg_clr.gif&ehk=V4TthMK8X92puvAPVbJPdB1C8F7VEt1sUUL3ZAgEAA4%3d"
    st.write('<img src="%s" width="200" />' % gif_url, unsafe_allow_html=True)

    st.write("##")
    st.write(
        """
        Cara Menggunakan Web Prediksi Diabetes  :
        - Klik tanda panah [ > ] dibagian kiri atas
        - Pada Bagian Menu, Pilih Prediksi
        - Masukkan data Identitas anda
        - Masukkan data pasien anda
        - ketikkan data pasien anda atau dengan klik tanda [ + ]
        - apa bila ada beberapa data pasien yang tidak ada seperti Number of Pregnancies, kosongkan saja
        - lalu klik Tes diabetes
        - Maka hasil Prediksi anda akan Muncul apabila terkena atau tidak terkena diabetes.
        - Anda dapat menghubungi kami melalui Menu Contact
        """
    )

    st.write("##")
    st.write("##")
    st.write("##")
    st.markdown("""
    <div style="text-align:center">
        <h1>Playlist Diabetes</h1>
    </div>
    """, unsafe_allow_html=True)
    st.write("---")
    st.markdown("""
    <div style="text-align:center">
        <h4>Berikut beberapa video referensi yang dapat dilihat untuk mengetahui terkait diabetes itu sendiri</h4>
    </div>
    """, unsafe_allow_html=True)
    # Daftar video beserta judul
    videos = [
        {"url": 'https://youtu.be/vseMC2kWIAE?si=I1RcUYmeLmpF-TIR', "title": "Bahaya Komplikasi Penyakit Akibat Diabetes"},
        {"url": 'https://youtu.be/TP1gsrtPEhM?si=YWFrR9FSNszpvUmg', "title": "Gejala-gejala Diabetes"},
        {"url": 'https://youtu.be/fL581YBsCk0?si=ffNZBWF_OIqkpUxe', "title": "Cara Pencegahan Diabetes"},
        {"url": 'https://www.youtube.com/watch?v=VJP7pQoi8wY&pp=ygUIZGlhYmV0ZXM%3D', "title": "Makanan yang harus Dihindari"}
    ]

    # Untuk menampilkan video yang dipilih
    selected_video = st.selectbox("Pilih Video", videos, format_func=lambda video: video["title"])
    st.video(selected_video["url"])

    # Deskripsi setiap video
    st.markdown(f'<p style="font-size:25px;">Deskripsi: {selected_video["title"]}</p>', unsafe_allow_html=True)

    st.write("---")
    st.write("##")
    st.write("##")
    st.header("Ulasan Pengguna")

    def show_reviews(reviews_data):
        for review in reviews_data:
            st.write("---")
            st.write(f"**Nama:** {review['nama_pengguna']}")
            st.write(f"**Peringkat Penilaian:** {'⭐️' * review['peringkat']}")
            st.write(f"**Ulasan:** {review['ulasan']}")

    # Untuk ulasan
    user_name = st.text_input("Nama Anda", key="user_name")  #Nama

    # Komentar
    user_review = st.text_area("Berikan Komentar Anda", key="user_review")

    # Bintang
    user_rating = st.selectbox("Beri Peringkat Bintang (1-5)", [1, 2, 3, 4, 5], key="user_rating")

    # Tombol untuk mengirim ulasan
    if st.button("Kirim Ulasan", key="submit_review"):

        # Untuk menyimpanulasan, peringkat, dan nama dalam struktur data
        review = {
            "nama_pengguna": user_name,  # Menambahkan nama pengguna ke ulasan
            "ulasan": user_review,
            "peringkat": user_rating
        }
        # Memuat data ulasan yang ada
        reviews_data = st.session_state.get("reviews_data", [])

        # Menambahkan ulasan baru ke daftar ulasan
        reviews_data.append(review)

        # Menyimpan data ulasan kembali ke session state
        st.session_state.reviews_data = reviews_data

        # Menampilkan pesan sukses dengan warna berbeda
        st.success("Terima kasih atas ulasan Anda!🫡")

    # Memuat data ulasan yang ada dari session state
    reviews_data = st.session_state.get("reviews_data", [])

    # Menampilkan ulasan yang sudah ada
    show_reviews(reviews_data)

if __name__ == "__main__":
    app()
