# Extract AgricultureLand values

def getLowerAndUpperBounds(data=None, column=None):
    # Calculate Q1, Q3, and IQR
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1

    # Calculate outlier bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    return lower_bound, upper_bound

def getColumnsWithMissingData(data=None):
    # columns with missing values
    missing_values = data.isna().sum()

    # where missing values are greater than 0
    columns_with_missing_values = missing_values[missing_values > 0].index

    return columns_with_missing_values