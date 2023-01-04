from turtle import color
from xmlrpc.client import DateTime
import pandas as pd 
import altair as alt
import streamlit as st
import connectdb
import numpy as np
from streamlit_autorefresh import st_autorefresh



def auto_refresh():
    count = st_autorefresh(interval=5000, limit=100, key="fizzbuzzcounter")
    
def temperature(df):
    st.header('Temperature Graph')
    base = alt.Chart(df).properties(width=550)
    # st.table(df)
    line = base.mark_line().encode(
        x='local_time',
        y='data',
    )
    rule = base.mark_rule().encode(
        y='average(data)',
        size=alt.value(2)
    )

    st.altair_chart(line + rule)
def humidity(df):
    st.header('Humidity Graph')
    base = alt.Chart(df).properties(width=550)
    # st.table(df)
    line = base.mark_line().encode(
        x='local_time',
        y='data',
    )
    rule = base.mark_rule().encode(
        y='average(data)',
        size=alt.value(2)
    )

    st.altair_chart(line + rule)
def vibration(df):
    pass
def alcohol(df):
    pass



if __name__=='__main__':

    sql='SELECT * FROM tem_data order by serial_num desc limit 50'
    auto_refresh()
    st.title('Sensor Visualizer')
    df=pd.DataFrame(connectdb.runquery(sql),columns=['serial_no','data','local_time'])
    # # print(df.info())


    st.sidebar.title('Sensors')
    temp=st.sidebar.checkbox('Temperature')
    if temp:
        temperature(df)

    vib=st.sidebar.checkbox('Vibration')
    if vib:
        vibration(df)
    hum=st.sidebar.checkbox('Humidity')
    if hum:
        humidity(df)
    al=st.sidebar.checkbox('Alcohol')
    if al:
        alcohol(df)
