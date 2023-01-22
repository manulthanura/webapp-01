import streamlit as st

# find the path to the icon
st.set_page_config(page_title="My App", page_icon=":computer:", layout="wide", initial_sidebar_state="expanded")

# ---- Header ----
with st.container():
    st.subheader("Hi, I'm Manul :wave:")
    st.title("Undergraduate Student and Developer")
    st.write("I am an Information and Communication Engineering (ICE) undergraduate student at SLTC Research University. My studies provide me with broad proficiency in computer engineering methods, tools, software packages, and techniques. Alongside this, I am developing hard skills as well as soft skills. As such, I am confident that I can make an instant impact in engineering roles. I love collaborating and making connections, and eager to hear about new updates and opportunities in IT and engineering topics.")
    st.write("[learn more >](https://lk.linkedin.com/in/manulthanura)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Education")
        st.write("SLTC Research University")
        st.write("BSc in Information and Communication Engineering")
        st.write("2021 - Present")

