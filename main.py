from flask import Flask, jsonify
from service.app import DataDriftService
from dummy_data_appender import DummyDataAppender

app = Flask(__name__)

drift_service = DataDriftService()

append_path = 'data/dummy_data_1.csv'
unique_values = ['A', 'B', 'C', 'D', 'E']
batch = 10
data_append_service = DummyDataAppender(append_path, unique_values, batch)


@app.route('/run_drift_service', methods=['GET'])
def run_drift_service():
    try:
        drift_service.run()
        return jsonify({"status": "success", "message": "Drift service ran successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/run_data_append_service', methods=['GET'])
def run_data_append_service():
    try:
        data_append_service.run()
        return jsonify({"status": "success", "message": "Data append service ran successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/run_services', methods=['GET'])
def run_services():
    try:
        data_append_service.run()
        drift_service.run()
        return jsonify({"status": "success", "message": "Both services ran successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
