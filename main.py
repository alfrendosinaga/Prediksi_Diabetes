import streamlit as st
from streamlit_option_menu import option_menu
import home, prediksi, contact

st.set_page_config(
    page_title="Prediksi Diabetes",
    page_icon=':bar_chart:',
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title="Main Menu",
                options=["Home", "Prediksi", "Contact"],
                icons=["house", "book", "envelope"],
                menu_icon="cast",
                default_index=0,
            )
        for item in self.apps:
            if app == item['title']:
                item['function']()

if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.add_app("Home", home.app)
    multi_app.add_app("Prediksi", prediksi.app)
    multi_app.add_app("Contact", contact.app)
    multi_app.run()
