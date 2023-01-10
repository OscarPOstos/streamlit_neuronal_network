import streamlit as st
from components import *
from PIL import Image

image = Image.open('logo.jpg')

st.image(image)

st.title("!Hola neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    show_components_tab1()

with tab2:
    show_components_tab2()

with tab3:
    show_components_tab3()
    
