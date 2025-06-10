from flask import Flask, request, jsonify, send_from_directory
import time
import os
from datetime import datetime

app = Flask(__name__, static_folder='../frontend')

race_data = {
    'start_time': None,
    'finish_times': [] # list of participant {'name': str, 'finish_time': float}
}

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/start_race', methods=['POST'])
def start_race():
    race_data['Start_time'] = time.time()
    race_data['finsh_times'] = []
    return jsonify({'message': 'Race Started', 'start_time': race_data['Start_time']})

@app.route('/submit_finish', methods=['POST'])
def submit_finish():
    data = request.get_json()
    participant = data.get('participant')
    finish_time = time.time()
    race_data['finsh_times'].append({
        'participant': participant,
        'finish_time': finish_time
    })
    return jsonify({'message': "Finish recorded", 'participant': participant, 'finish_time': finish_time})

@app.route('/results', methods=['GET'])
def get_results():
    start = race_data.get('start_time')
    results = [
        {
        'participant': r['participant'],
        'elapsed_time': round(r['finish_time'] - start, 3)
        }
        for r in race_data['finish_times']
    ]
    results.sort(key=lambda x: x['elapsed_time'])
    return jsonify(results)

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)