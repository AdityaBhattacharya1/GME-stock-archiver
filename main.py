import matplotlib.pyplot as plt
import pandas_datareader as pdr
import mplfinance as mpf
import datetime as dt
from datetime import timedelta

end_date = dt.datetime.now()

graph_types = ['candle', 'line', 'ohlc', 'renko', 'pnf']

stock_name = input('Enter the name of the stock\n')
graph_type = input(
    'Enter type of graph\n [Options available: candle, line, ohlc, renko, pnf]\n')

if not graph_type in graph_types:
    print('Invalid graph type, defaulted to candlestick')

try:
    start_year = int(
        input('Enter the year from which the value should be counted \n'))
    start_month = int(
        input('Enter the month from which the value should be counted \n'))
    start_day = int(
        input('Enter the date of the day from which the value should be counted \n'))
except:
    print('Since numeric value was not entered for either the date, month or year, defaulted to that of 31 days ago')
    start_date = dt.datetime.today() - timedelta(days=31)
else:
    start_date = dt.datetime(start_year, start_month, start_day)


# Uses the Yahoo stocks API for remote data collection.
# You can substitute that attribute with the path to a CSV file containing the data. (You would need to import pandas for that.)
data = pdr.DataReader(stock_name, 'yahoo', start_date, end_date)

# Print the data (optional):
# print(data)

colours = mpf.make_marketcolors(
    up="g",  # green
    down="r",  # red
    wick={'up': 'lime', 'down': 'orange'},
    edge="inherit",
    volume="in",
    ohlc='in')

mpf_style = mpf.make_mpf_style(
    base_mpf_style="nightclouds", marketcolors=colours)

# The double new-line escapes because the title would stick to the option bar.
# The new lines act as psuedo-styles as there is no option available for styling the titles (yet).
# What is this 'mav', you ask? Here's an ELI5 link: https://www.reddit.com/r/explainlikeimfive/comments/a7pbys/eli5_what_is_a_moving_average_how_is_it_different/
# tl;dr it is the average of the most recent values. The value of the mav determines how many days are counted in the average.
# The show_nontrading boolean includes the non-trading days (holidays, etc.) in the graph.


mpf.plot(data, title=f"\n\n {stock_name} stock value",
         type=f"{graph_type if graph_type in graph_types else 'candlestick'}",
         style=mpf_style, volume=True, mav=2, show_nontrading=False)
