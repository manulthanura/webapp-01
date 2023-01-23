import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# find the path to the icon
st.set_page_config(page_title="My App", page_icon=":computer:", layout="wide", initial_sidebar_state="expanded")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("./style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")


# ---- HEADER ----
with st.container():
    st.subheader("Hi, I'm Manul :wave:")
    st.title("Undergraduate Student and Developer")
    st.write("I am an Information and Communication Engineering (ICE) undergraduate student at SLTC Research University. My studies provide me with broad proficiency in computer engineering methods, tools, software packages, and techniques. Alongside this, I am developing hard skills as well as soft skills. As such, I am confident that I can make an instant impact in engineering roles. I love collaborating and making connections, and eager to hear about new updates and opportunities in IT and engineering topics.")
    st.write("[learn more >](https://lk.linkedin.com/in/manulthanura)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    # LEFT COLUMN
    with left_column:
        st.header("Education")
        st.write("SLTC Research University")
        st.write("BSc in Information and Communication Engineering")
        st.write("2021 - Present")
    # RIGHT COLUMN
    with right_column:
        st_lottie(lottie_coding, height=300, key="Coding")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
