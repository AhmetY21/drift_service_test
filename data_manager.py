import pandas as pd
import openpyxl  

class DataManager:
    def __init__(self):
        self.dataframes = {}
        self.df_metadata = {}
        
    def load_dataframes(self, sources):
        for source in sources:
            
            try:
                df = pd.read_csv(source)
                self.dataframes[source] = df
                # Store column metadata
                self.df_metadata[source] = {col: str(dtype) for col, dtype in df.dtypes.items()}
            except Exception as e:
                print(f"Error loading dataframe from {source}: {e}")
                continue
        return self.dataframes
    
    def export_results(self, results, output_format='excel', output_path='output/results'):
        if output_format.lower() == 'excel':
            # Initialize a new DataFrame to consolidate all results.
            consolidated_df = pd.DataFrame()

            for col, col_results in results.items():
                # Convert the results dictionary for each column to a DataFrame and concatenate it to the consolidated DataFrame.
                col_df = pd.DataFrame.from_dict(col_results, orient='index', columns=[col])
                consolidated_df = pd.concat([consolidated_df, col_df], axis=1)

            # Write the consolidated DataFrame to a single sheet in the Excel file.
            with pd.ExcelWriter(f'{output_path}.xlsx', engine='openpyxl') as writer:
                consolidated_df.to_excel(writer, sheet_name='Consolidated Results')
        else:
            print("Unsupported output format.")

