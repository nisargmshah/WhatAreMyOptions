# predictor
import pandas_datareader.data as web
from datetime import datetime

start = datetime(2015, 2, 9)
end = datetime(2019, 4, 19)
f = web.DataReader('COF', 'iex', start, end)
