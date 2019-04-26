<<<<<<< HEAD
# predictor
import pandas_datareader.data as web
from datetime import datetime

start = datetime(2019, 4, 18)
end = datetime(2019, 4, 18)
f = web.DataReader('FIT', 'iex', start, end)
f.to_csv(index=False, path_or_buf='training_data.csv')
=======
# predictor
import pandas_datareader.data as web
from datetime import datetime
import numpy as np

year_array = np.array([2015, 2016, 2017, 2018, 2019])
month_array = np.array(range(1,13))
day_array = np.array(range(1, 32))

f = None

for year in year_array:

    for month in month_array:
        month_data = np.array()
        for day in day_array:
            try:
                start = datetime(year, month, day)
                end = datetime(year, month, day)
                day_data = web.DataReader('COF', 'iex', start, end)
                month_data.add(day_data)
            except:
                print("no data to write")



if f is not None:
    f.to_csv(index=False, path_or_buf='training_data.csv')
>>>>>>> 0f0085d2aa9a3ff6ce0ef4a31d3fa7676ea2d3e8
