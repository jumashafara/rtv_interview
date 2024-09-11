from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

data_ = pd.read_csv('data_without_missing_values.csv')

# Assuming df is your DataFrame
label_encoder = LabelEncoder()

# List of categorical columns to encode
categorical_columns = data_.select_dtypes(include=['object']).columns
print(categorical_columns)

# Apply Label Encoding
all_classes_ = []
for column in categorical_columns:
    data_[column] = label_encoder.fit_transform(data_[column])
    all_classes_.append(label_encoder.classes_)

print(all_classes_)

data_.to_csv(path_or_buf='categorized_data.csv', index=False)