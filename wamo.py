# predictor
import pandas_datareader.data as web
from datetime import datetime

start = datetime(2019, 4, 18)
end = datetime(2019, 4, 18)
f = web.DataReader('FIT', 'iex', start, end)
f.to_csv(index=False, path_or_buf='training_data.csv')
