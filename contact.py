import streamlit as st

def app():
    st.header(":mailbox: Hubungi Kami!")

    contact_form = """
    <form action="https://formsubmit.co/alrendoaja@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Nama Anda" required>
         <input type="email" name="email" placeholder="Email Anda..." required>
         <textarea name="message" placeholder="Pesan Anda"></textarea>
         <button type="submit">Kirim</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")


if __name__ == "__main__":
    app()
