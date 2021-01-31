import matplotlib.pyplot as plt
import pandas_datareader as pdr
import mplfinance as mpf
import datetime as dt

start_date = dt.datetime(2021, 1, 1)
end_date = dt.datetime.now()

# Uses the Yahoo stocks API for remote data collection.
# You can substitute that attribute with the path to a CSV file containing the data. (You would need to import pandas for that.)
data = pdr.DataReader('GME', 'yahoo', start_date, end_date)

# Print the data (optional):
# print(data)

colours = mpf.make_marketcolors(
    up="g",  # green
    down="r",  # red
    wick={'up': 'lime', 'down': 'orange'},
    edge="inherit",
    volume="in")

mpf_style = mpf.make_mpf_style(
    base_mpf_style="nightclouds", marketcolors=colours)

# The double new-line escapes because the title would stick to the option bar.
# The new lines act as psuedo-styles as there is no option available for styling the titles (yet).
# What is this 'mav', you ask? Here's an ELI5 link: https://www.reddit.com/r/explainlikeimfive/comments/a7pbys/eli5_what_is_a_moving_average_how_is_it_different/
# tl;dr it is the average of the most recent values. The value of the mav determines how many days are counted in the average.
# The show_nontrading boolean includes the non-trading days (holidays, etc.) in the graph.
mpf.plot(data, title="\n\n GameStop (GME) stock value", type="candle",
         style=mpf_style, volume=True, mav=2, show_nontrading=False)
