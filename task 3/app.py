import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

model = pk.load(open('model.pkl','rb'))

st.header('Car Price Prediction ML Model')

cars_data = pd.read_csv('Cardetails.csv')

cars_data.drop(columns=['seller_type','km_driven'], axis=1, inplace=True)


def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]
    return car_name.strip(' ')
    
#Index(['name', 'year', 'fuel', 'transmission', 'owner', 'mileage', 'engine',
      # 'max_power', 'seats'],
       #"""
cars_data['name'] = cars_data['name'].apply(get_brand_name)

input_name = st.selectbox('Select Car Brand', cars_data['name'].unique())
input_year = st.slider('Car Manufactured Year',1994,2024)
input_fuel = st.selectbox('Fuel Type', cars_data['fuel'].unique())
input_transmission = st.selectbox('Transmission Type', cars_data['transmission'].unique())
input_owner = st.selectbox('Owner', cars_data['owner'].unique())
input_mileage = st.number_input("Mileage", min_value=0, value=0, step=1)
input_engine_cc = st.number_input("Engine CC", min_value=700,max_value=5000, value=700, step=1)
input_max_power = st.number_input("Max Power(bhp)", min_value=0,max_value=200, value=0, step=1)
input_seats = st.slider('No. of Seats',5,10)


def change_type(val):
    val = val.split(' ')[0]
    val = val.strip()
    if val == '':
        val = 0
    return float(val)
#df['mileage'] = df['mileage'].apply(change_type)

if st.button("Predict"):
    input_data_model = pd.DataFrame(
    [[input_name,input_year,input_fuel,input_transmission,input_owner,input_mileage,input_engine_cc,input_max_power,input_seats]],columns=['name', 'year', 'fuel', 'transmission','owner', 'mileage', 'engine',
       'max_power', 'seats'])
    
    input_data_model['name'] = input_data_model['name'].replace(['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
       'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
       'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
       'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
       'Ambassador', 'Ashok', 'Isuzu', 'Opel'],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31])
    input_data_model['fuel'] = input_data_model['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'],[1,2,3,4])
    input_data_model['transmission'] = input_data_model['transmission'].replace(['Manual', 'Automatic'],[1,2])
    input_data_model['owner'] = input_data_model['owner'].replace(['First Owner', 'Second Owner', 'Third Owner',
       'Fourth & Above Owner', 'Test Drive Car'],[1,2,3,4,5])
    #st.write(input_data_model)
    car_price = model.predict(input_data_model)
    formatted_car_price = f"{car_price[0]:,.2f}"
    
    html_code = f""" <div style="background-color:#D4EDDA; color:#40754C;padding:20px;border-radius:5px;width:95%;text-align:center;font-size:1.5rem;font-weight:700"<strong>Predicted Car Price: Rs {formatted_car_price}</strong></div>"""

    st.markdown(html_code, unsafe_allow_html=True)
    #st.markdown('Predicted Car Price : Rs: '+str(car_price[0]))
    



# to run this file type "streamlit run app.py"