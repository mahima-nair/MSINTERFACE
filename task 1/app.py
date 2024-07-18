import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

model = pk.load(open('model.pkl','rb'))

# Function to read the CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Apply the CSS from the file
local_css("style.css")

st.header(':violet[Iris Species Classification]', divider='violet')

input_sepal_len = st.number_input("Sepal Length (cm)", min_value=0.0, value=10.0, step=0.1)
input_sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, value=10.0, step=0.1)
input_petal_len = st.number_input("Petal Length (cm)", min_value=0.0, value=15.0, step=0.1)
input_petal_width = st.number_input("Petal Width (cm)", min_value=0.0, value=15.0, step=0.1)

def predict_species(sepal_len,sepal_width,petal_len,petal_width):
    spec = model.predict([[sepal_len,sepal_width,petal_len,petal_width]])
    if(spec==0):
        return("Setosa")
    elif spec==1:
        return("Versicolor")
    else:
        return("Virginica")
    
    





if st.button("Classify Iris"):
  
    species = predict_species(input_sepal_len,input_sepal_width,input_petal_len,input_petal_width)    
    #html_code = f""" <div style="background-color:#D4EDDA; color:#40754C;padding:20px;border-radius:5px;width:95%;text-align:center;font-size:1.5rem;font-weight:700"<strong>Predicted Species : {species}</strong></div>"""
    html_code = f""" <div style="background-color: rgb(64, 0, 128);; color:white;padding:20px;border-radius:5px;width:95%;text-align:center;font-size:1.5rem;font-weight:700"<strong>Classified Species : {species}</strong></div>"""
    st.markdown(html_code, unsafe_allow_html=True)
    #st.markdown('Predicted Car Price : Rs: '+str(car_price[0]))
    



# to run this file type "streamlit run app.py"