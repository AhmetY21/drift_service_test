from service.data_manager import DataManager
from service.data_drift import DriftMetrics
from service.utils import load_config  
from service.alert_manager import AlertManager  
from service.visualization_manager import VisualizationManager  



class DataDriftService:
    def __init__(self):
        self.data_manager = DataManager()
        self.drift_metrics = DriftMetrics()
        self.alert_manager = AlertManager()  # Initialize the new AlertManager class
        self.config = load_config(file_path='config/config.txt')
        self.visualization_manager = VisualizationManager(self.config)  # Initialize the new VisualizationManager class

    def run(self):
        monitored_columns = self.config.get('MONITORED_COLUMNS', [])
        dataframes = self.data_manager.load_dataframes(self.config['DATA_SOURCES'])
        
        results = self.drift_metrics.run(dataframes, self.data_manager.df_metadata, monitored_columns)
        self.alert_manager.alert_on_threshold(results, self.config['THRESHOLDS'])
        
        if self.config.get('SAVE_VISUALIZATIONS', 'False') == 'True':
            visualized_columns = self.config.get('VISUALIZED_COLUMNS', [])
            self.visualization_manager.create_visualization(dataframes, visualized_columns, visualization_type='hist')

        self.data_manager.export_results(results, self.config['OUTPUT_FORMAT'])
