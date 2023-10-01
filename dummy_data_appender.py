import pandas as pd
import numpy as np
import random
import time

class DummyDataAppender:
    def __init__(self, append_path, unique_values, batch):
        self.append_path = append_path
        self.df = pd.read_csv(append_path)
        self.unique_values = unique_values
        self.batch = batch
        

    def generate_new_rows(self):
        rows = {}
        for col, dtype in self.df.dtypes.items():
            if np.issubdtype(dtype, np.number):
                rows[col] = np.random.randint(0, 100, self.batch).tolist()
            else:
                rows[col] = np.random.choice(self.unique_values, self.batch).tolist()
        return pd.DataFrame(rows)

    def append_rows_to_csv(self):
        new_rows_df = self.generate_new_rows()
        self.df = pd.concat([self.df, new_rows_df], ignore_index=True)
        self.df.to_csv(self.append_path, index=False)
        print(f"Appended {self.batch} new rows to {self.append_path}.csv at {time.ctime()}")

    def run(self):
        print('Dummy Data Appender is Running')
        print(f'Shape of the File {self.df.shape}')
        self.append_rows_to_csv()


