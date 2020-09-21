import yfinance as yf
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr
from datetime import date
import matplotlib.pyplot as plt
import mpld3
import plotly.graph_objects as go
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure


def stock_info(symb):
    yraw = yf.Ticker(symb)
    rinfo = yraw.info
    insymb = rinfo.get("symbol")
    inname = rinfo.get("longName")
    incity = rinfo.get("city")
    incoun = rinfo.get("country")
    incurr = rinfo.get("currency")
    insxch = rinfo.get("exchange")
    inurl = rinfo.get("website")
    indhigh = rinfo.get("dayHigh")
    indlow = rinfo.get("dayLow")
    return insymb, inname, incity, incoun, incurr, insxch, inurl, indhigh, indlow


def table_info(symb):
    yf.pdr_override()
    today = date.today()
    pdraw = pdr.get_data_yahoo(symb, start="2010-01-01", end=today)
    pdrawr = pdraw.reset_index()
    pdrawr = pdrawr.sort_values(by='Date', ascending=False)
    pd.options.display.float_format = '{:.2f}'.format
    pdrawr = pdrawr.head(10)
    return pdrawr


def schart(symb):
    yf.pdr_override()
    today = date.today()
    pdraw = pdr.get_data_yahoo(symb, start="2010-01-01", end=today)
    old2 = pdraw.reset_index()
    fig = plt.figure()
    dates = old2['Date']
    dates = [pd.to_datetime(d) for d in dates]
    stock_prices = old2['Close']
    # plt.scatter(dates, stock_prices)
    plt.title('Past 10 Years Stock Price', fontsize=22)
    plt.plot(dates, stock_prices)
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Stock Price', fontsize=18)
    html_graph = mpld3.fig_to_html(fig, template_type="simple")
    return html_graph


def boxplot(symb):
    yf.pdr_override()
    today = date.today()
    pdraw = pdr.get_data_yahoo(symb, start="2010-01-01", end=today)
    old2 = pdraw.reset_index()
    fig = plt.figure()
    plt.boxplot(old2['Close'].transpose())
    plt.title('Boxplot', fontsize=22)
    plt.xlabel('Company', fontsize=18)
    plt.ylabel('Stock Prices', fontsize=18)
    ticks = range(1)
    labels = ""
    plt.xticks(ticks, labels)
    html_graph = mpld3.fig_to_html(fig, template_type="simple")
    return html_graph
