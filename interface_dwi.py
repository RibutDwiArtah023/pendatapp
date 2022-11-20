import streamlit as st
import re
import pandas as pd 
import numpy as np

st.title("""
Harga Rumah
""")

#Fractional Knapsack Problem
#Getting input from user
harga=int(st.number_input("Masukkan Harga : ",0))
luas=int(st.number_input("Masukkan Luas : ",0))
kasur=int(st.number_input("Masukkan Banyak Kasur : ",0))

submit = st.button("submit")


if submit:
    st.info("Jadi,Km nya adalah : ")


