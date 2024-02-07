import streamlit as st
from datetime import datetime
import yfinance as yf 
import matplotlib.pyplot as plt

favorites = ['TUPRS', 'MIATK', 'ALFAS']

manualSelect = st.sidebar.selectbox('Keremin Sevdiği Hisseler', favorites + ['Kendim seçecem ihtiyar'])

if manualSelect == 'Kendim seçecem ihtiyar':
    symbol = st.sidebar.text_input("Hisse senedi sembolü", value='TUPRS')
else:
    symbol = manualSelect

st.title(symbol+' Hissesinin grafiği')

startDate = st.sidebar.date_input('Başlangıç tarihi',value=datetime(2020,3,26))
endDate = st.sidebar.date_input('Başlangıç tarihi',value=datetime.now())

getStocks = yf.download(symbol+'.IS',start=startDate,end=endDate)
st.subheader("Trend Grafiği")
st.line_chart(getStocks['Close'])

st.subheader('Hisse tablosu')
st.write(getStocks)
