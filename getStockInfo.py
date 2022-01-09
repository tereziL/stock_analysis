import yfinance as yf  
import matplotlib.pyplot as plt
import pandas as pd

def getStorePrices(stock_shortcut):
    return yf.download(stock_shortcut,'2021-01-01','2021-12-31')

# data["Close"].plot()
# plt.show()
