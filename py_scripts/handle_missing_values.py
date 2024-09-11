import pandas as pd
from helper_functions import getColumnsWithMissingData

# load data
data = pd.read_csv('DataScientist_01_Assessment.csv')

# data info
print(data.info())

# find missing data
columns_with_missing_data = getColumnsWithMissingData(data=data)
print(columns_with_missing_data)

# drop loan from and organic_pesticide_expenditure 
# because the missingness is way to large
data.drop(columns=['Loan_from', 'organic_pesticide_expenditure'], 
          inplace=True)

# Fill AgricultureLand with mean
agriculture_land = data['AgricultureLand']
agriculture_land.fillna(value=agriculture_land.mean(), 
                        inplace=True)
data['AgricultureLand'] = agriculture_land

# Fill business number with mode
data['business_number'].value_counts()
business_number = data['business_number']
business_number.fillna(value=3069,
                       inplace=True)
data['business_number'] = business_number

# drop food_banana_wilt_diseases
data.drop(labels='food_banana_wilt_diseases', 
          axis=1,
          inplace=True)

# save a copy
data.to_csv('data_without_missing_values.csv', index=False)
