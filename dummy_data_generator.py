import pandas as pd
import numpy as np

# Number of rows and columns
num_rows = 10000
num_numeric_columns = 50
num_categorical_columns = 20

# For reproducibility
np.random.seed(0)

# Generate numerical columns
numeric_data = {}
for i in range(num_numeric_columns):
    col_name = f"num_col_{i}"
    numeric_data[col_name] = np.random.randn(num_rows)

# Generate categorical columns
categorical_data = {}
categories = ['A', 'B', 'C', 'D', 'E']
for i in range(num_categorical_columns):
    col_name = f"cat_col_{i}"
    categorical_data[col_name] = np.random.choice(categories, num_rows)

# Combine numerical and categorical columns and create two DataFrames
df1_data = {**numeric_data, **categorical_data}
df1 = pd.DataFrame(df1_data)

# Introduce some "drift" by modifying the second DataFrame
df2_data = {col: data * (1 + 0.1 * (np.random.rand() - 0.5)) if col.startswith('num') else data
            for col, data in df1_data.items()}
df2 = pd.DataFrame(df2_data)

# Save DataFrames to CSV files
df1.to_csv('data/dummy_data_1.csv', index=False)
df2.to_csv('data/dummy_data_2.csv', index=False)
