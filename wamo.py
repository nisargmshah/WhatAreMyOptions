# predictor
import pandas_datareader.data as web
from datetime import datetime
import numpy as np

year_array = np.array([2015, 2016, 2017, 2018, 2019])
month_array = np.array(range(1,13))

start = datetime(2019, 4, 18)
end = datetime(2019, 4, 18)
f = web.DataReader('COF', 'iex', start, end)
f.to_csv(index=False, path_or_buf='training_data.csv')
