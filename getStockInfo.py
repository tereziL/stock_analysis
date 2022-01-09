import yfinance as yf  
import matplotlib.pyplot as plt
import pandas as pd

def getStockPrices(stock_shortcut):
    return yf.download(stock_shortcut,'2021-01-01','2021-12-31')

getStockPrices("NIO")
# data["Close"].plot()
# plt.show()
