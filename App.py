from flask import Flask, render_template, jsonify
import random
import datetime

app = Flask(__name__)

# Sample data generation for demonstration
def generate_data():
    return {
        'altitude': [(datetime.datetime.now().strftime("%H:%M:%S"), random.randint(100, 1000)) for _ in range(10)],
        'tilt_x': [(datetime.datetime.now().strftime("%H:%M:%S"), random.uniform(-30, 30)) for _ in range(10)],
        'tilt_y': [(datetime.datetime.now().strftime("%H:%M:%S"), random.uniform(-30, 30)) for _ in range(10)],
        'rot_z': [(datetime.datetime.now().strftime("%H:%M:%S"), random.uniform(-180, 180)) for _ in range(10)],
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify(generate_data())

@app.route('/current_time')
def current_time():
    now = datetime.datetime.now()
    return jsonify(time=now.strftime("%H:%M:%S"), date=now.strftime("%Y-%m-%d"))

if __name__ == '__main__':
    app.run(debug=True)
