import streamlit as st
import pandas as pd
from services.financial_services import FinancialServices

# Initialisation des variables financières
ticker = ["AAPL","GOOG","MSFT","AMZN","TSLA"]
start_date = "2020-01-01"
end_date = "2025-01-01"
period = "1d"


st.title("Test APP : Quotes Download")
header = st.subheader('Données financières:')
loading_state = st.text(f"Loading {ticker} quotes...")

financial_services = FinancialServices(ticker)
data = financial_services.download_quotes(start_date,end_date,period)

loading_state.text = f"Quotes downloaded for {ticker}"