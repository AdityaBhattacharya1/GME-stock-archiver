import matplotlib.pyplot as plt
import pandas_datareader as pdr
import mplfinance as mpf
import datetime as dt
from datetime import timedelta


def date_setter(str_value, phonetic):
    return int(input(f'Enter the {str_value} {phonetic} which the stock value should be counted \n'))


# Setting empty values of the start and end date or else it throws an error
start_date = None
end_date = None


def date_validator():
    global start_date
    global end_date
    try:
        start_year = date_setter('year', 'from')
        start_month = date_setter('month', 'from')
        start_day = date_setter('date of day', 'from')

        end_year = date_setter('year', 'till')
        end_month = date_setter('month', 'till')
        end_day = date_setter('date of day', 'till')
    except:
        print('Since numeric value was not entered for either the date, month or year, defaulted to that of 31 days ago')
        start_date = dt.datetime.today() - timedelta(days=31)
        end_date = dt.datetime.now()
    else:
        start_date = dt.datetime(start_year, start_month, start_day)
        end_date = dt.datetime(end_year, end_month, end_day)

    if start_year < 1900 or end_date < start_date:
        print(
            "Invalid year value. Set to default value(s) [Defaults: start date is that of 31 days ago, end date is today's date]")
        start_date = dt.datetime.today() - timedelta(days=31)
        end_date = dt.datetime.now()

    return start_date, end_date


graph_types = ['candle', 'line', 'ohlc', 'renko', 'pnf']

stock_name = input('Enter the name of the stock\n')
graph_type = input(
    'Enter type of graph\n [Options available: candle, line, ohlc, renko, pnf]\n')
mav_val = int(input(
    'Enter the moving average value\n'))

if not graph_type in graph_types:
    print('Invalid graph type, defaulted to candlestick')

date_validator()


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
# What is this 'mav', you ask? Here's an ELI5 link:
# https://www.reddit.com/r/explainlikeimfive/comments/a7pbys/eli5_what_is_a_moving_average_how_is_it_different/
# tl;dr it is the average of the most recent values.
# The value of the mav determines how many days are counted in the average.
# The show_nontrading boolean includes the non-trading days (holidays, etc.) in the graph.


mpf.plot(data, title=f"\n\n {stock_name} stock value\n",
         type=f"{graph_type if graph_type in graph_types else 'candlestick'}",
         style=mpf_style, volume=True, mav=mav_val, show_nontrading=False)
