import streamlit as st
import requests
import datetime
import pandas as pd

st.markdown(
'''
# TaxiFareModel - How much will it cost?
''')

st.markdown('''## Tell me about yourself''')

key = '2013-07-06 17:18:00.000000119'
pickup_date = st.date_input('Date of travel:', datetime.date(2013,7,6))
pickup_time = st.time_input('Time of travel:', datetime.time(17,20))
pickup_datetime = ' '.join([str(pickup_date), str(pickup_time)])
# st.write(pickup_datetime)
pickup_longitude = st.number_input('Enter pickup longitude', -73.950655)
pickup_latitude = st.number_input('Enter pickup latitude', 40.783282)
dropoff_longitude = st.number_input('Enter dropoff longitude', -73.984365)
dropoff_latitude = st.number_input('Enter dropoff latitude', 40.769802)
passenger_count = st.number_input('How many people travelling?', 1)


def get_map_data():
    return pd.DataFrame({'lat': [pickup_latitude, dropoff_latitude],
                         'lon': [pickup_longitude, dropoff_longitude]})

st.map(get_map_data())

# Return prediction

url = 'https://api-zby5e6zv3q-ew.a.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

params = {'key' : ['2013-07-06 17:18:00.000000119'],
          'pickup_datetime': pickup_datetime,
          'pickup_longitude': pickup_longitude,
          'pickup_latitude': pickup_latitude,
          'dropoff_longitude': dropoff_longitude,
          'dropoff_latitude': dropoff_latitude,
          'passenger_count': passenger_count}

make_prediction = st.button('Calculate fare!')
if make_prediction:
    response = requests.get(url, params).json()

    fare = str(round(response['prediction'], 2))

    st.markdown(f'## Fare cost: ${fare}')

else:
    st.markdown('''## Click Calculate fare!''')
