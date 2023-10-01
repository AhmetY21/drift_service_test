import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

class AlertManager:
    def __init__(self):
        pass

    def alert_on_threshold(self, results, threshold_dict):
        """
        :param results: Dictionary containing the results of the statistical tests.
        :param threshold_dict: Dictionary containing the thresholds for regular, warning, and critical alerts.
        """
        for col, metrics in results.items():
            for test, value in metrics.items():
                if value > threshold_dict.get('critical', 0.2):
                    logging.error(f"Critical Alert: {col} - {test}. Value: {value}")
                elif value > threshold_dict.get('warning', 0.1):
                    logging.warning(f"Warning: {col} - {test}. Value: {value}")
                elif value > threshold_dict.get('regular', 0.05):
                    logging.info(f"Regular Alert: {col} - {test}. Value: {value}")
