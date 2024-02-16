from flask import Flask, render_template, jsonify
import subprocess
from Sensor import get_flow_value, distance
import RPi.GPIO as GPIO

app = Flask(__name__)



@app.route('/get_distance')
def get_distance():
    try:
        dist = measure_distance()
        return jsonify({'distance': dist}),200

    except Exception as e:
        return jsonify({'error': str(e)}),500

@app.route('/get_flow')
def get_flow():
    try:
        flow = get_flow_value()
        return jsonify({'flow': flow})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/')
def dashboard():
    return render_template('dashboard.html')
@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)


