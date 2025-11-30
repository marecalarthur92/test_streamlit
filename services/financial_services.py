import yfinance as yf
import pandas as pd

class FinancialServices:
    """
    Classe financials services pour gérer les téléchargements yahoofinance.
    """
    def __init__(self, ticker: str | list[str]):
        # Initialisation des variables
        self.ticker = ticker
    
    def download_quotes(self,start_date: str, end_date: str, period: str) -> pd.DataFrame:
        # Téléchargement des données financières
        data = yf.download(self.ticker,start_date,end_date,period)
        return data
