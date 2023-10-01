from scipy.stats import ttest_ind, chisquare, ks_2samp
import pandas as pd
from scipy.stats import chi2_contingency

class DriftMetrics:
    def __init__(self):
        print("Initializing the correct DriftMetrics class")
        self.metrics = {
            "numerical": {
                "t_test": self.t_test,
                "ks_test": self.ks_test
            },
            "categorical": {
                "chi_square": self.chi_square
            }
        }
        
    def run(self, dataframes, df_metadata, monitored_columns):
        results = {}
        df_keys = list(dataframes.keys())
        df1, df2 = dataframes[df_keys[0]], dataframes[df_keys[1]]
        
        for col in monitored_columns:  # Only assess provided columns in monitored_columns
            if col not in df1.columns or col not in df2.columns:
                print(f"Skipping {col} as it is not present in both dataframes")
                continue
                
            dtype1, dtype2 = df_metadata[df_keys[0]].get(col, None), df_metadata[df_keys[1]].get(col, None)
            if dtype1 is None or dtype2 is None:
                print(f"Skipping {col} due to missing metadata: dtype1={dtype1}, dtype2={dtype2}")
                continue
            if dtype1 != dtype2:
                print(f"Skipping {col} due to dtype mismatch: {dtype1} != {dtype2}")
                continue

            dtype_group = "numerical" if "float" in dtype1 or "int" in dtype1 else "categorical"
            col_results = {}
            for test_name, test_func in self.metrics[dtype_group].items():
                col_results[test_name] = test_func(df1[col], df2[col])
            results[col] = col_results
        return results

    def t_test(self, series1, series2):
        return ttest_ind(series1, series2).pvalue

    def ks_test(self, series1, series2):
        return ks_2samp(series1, series2).pvalue

    from scipy.stats import chi2_contingency

    def chi_square(self, series1, series2):
        # Get unique values from both series
        all_categories = set(series1.unique()).union(set(series2.unique()))

        # Construct a contingency table
        table = pd.DataFrame({series1.name: series1.value_counts(), series2.name: series2.value_counts()}).fillna(0)
        table = table.reindex(all_categories, fill_value=0)
        
        # Calculate chi2 contingency
        chi2, p, _, _ = chi2_contingency(table)
        return p
