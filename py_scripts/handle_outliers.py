import pandas as pd
from helper_functions import getLowerAndUpperBounds

data_ = pd.read_csv('data_without_missing_values.csv')
print(data_)

agriculture_land_bounds = getLowerAndUpperBounds(data=data_,
                                                 column='AgricultureLand')
print(agriculture_land_bounds)

data_ = data_[data_['AgricultureLand'] < agriculture_land_bounds[1]]

data_.to_csv(path_or_buf='data_without_outliers.csv', index=False)

