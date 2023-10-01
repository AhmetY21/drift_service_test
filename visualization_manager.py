import matplotlib.pyplot as plt
import os

class VisualizationManager:
    def __init__(self,config):
        self.config = config

    def create_visualization(self, dataframes, monitored_columns, visualization_type='hist',config=None):

        df_keys = list(dataframes.keys())
        df1, df2 = dataframes[df_keys[0]], dataframes[df_keys[1]]
        
        for col in monitored_columns:
            if col in df1.columns and col in df2.columns:
                plt.figure(figsize=(10, 5))
                plt.title(f"{visualization_type.capitalize()} for {col}")

                if visualization_type == 'hist':
                    plt.hist(df1[col], alpha=0.5, label=f"{df_keys[0]}")
                    plt.hist(df2[col], alpha=0.5, label=f"{df_keys[1]}")
                elif visualization_type == 'scatter':
                    plt.scatter(df1[col], df2[col], alpha=0.5)
                elif visualization_type == 'bar':
                    plt.bar(df1[col], height=1, alpha=0.5, label=f"{df_keys[0]}")
                    plt.bar(df2[col], height=1, alpha=0.5, label=f"{df_keys[1]}")
                
                plt.xlabel(col)
                plt.ylabel(visualization_type.capitalize())
                plt.legend(loc='upper right')
                plt.show()
                if self.config.get('SAVE_VISUALIZATIONS', 'False') == 'True':
                    directory = "output/images"
                if not os.path.exists(directory):
                    os.makedirs(directory)
                plt.savefig(f"{directory}/{col}_{visualization_type}.png")