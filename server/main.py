import time
import argparse
import RPi.GPIO as GPIO
from light import Tower
import database
from flask import Flask, jsonify, request

# Pins configuration (order: green, orange, red)
GPIO_PINS = [{'name': 'green', 'pin': 22},
             {'name': 'orange', 'pin': 17},
             {'name': 'red', 'pin': 27}]

# Create a Flask app
app = Flask(__name__)

# Initialize the database
database.ensure_database()

# Initialize the tower (lights)
tower = Tower(GPIO_PINS)


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


@app.route('/api/state/set', methods=['POST'])
def set_state():
    data = request.data.decode('utf-8')
    state = [int(n.strip()) for n in data.split(',') if n.strip().isdigit()]
    """Endpoint to get the current state of all lights."""
    tower.green.on() if state[0] else tower.green.off()
    tower.orange.on() if state[1] else tower.orange.off()
    tower.red.on() if state[2] else tower.red.off()

    return jsonify(state)


@app.route('/api/state', methods=['GET'])
def get_state():
    """Endpoint to get the current state of all lights."""
    state = database.get_all_states()
    return jsonify(state)


@app.route('/api/toggle/<color>', methods=['POST'])
def toggle_light(color):
    """Endpoint to toggle the state of a specified light."""
    if color not in ['green', 'orange', 'red']:
        return jsonify({'error': 'Invalid color'}), 404

    # Get the light object based on the color
    light = getattr(tower, color)

    # Toggle light state (on/off)
    new_state = GPIO.LOW if light.state == GPIO.HIGH else GPIO.HIGH
    light._set(new_state)  # Update the light state in the system

    return jsonify({color: new_state})


def run(tower):
    """Run the tower with manual light control."""
    try:
        time.sleep(0.5)
        while True:
            print('on')
            tower.green.on()
            tower.red.off()
            tower.orange.off()

            time.sleep(10)
    except KeyboardInterrupt:
        print("\nInterrupted by user. Cleaning up...")
    finally:
        GPIO.cleanup()


def main():
    parser = argparse.ArgumentParser(
        description="Control lights or run server.")
    parser.add_argument('--server', action='store_true',
                        help='Run the Flask server to control lights via API')

    args = parser.parse_args()

    if args.server:
        print("Starting Flask server...")
        app.run(host='0.0.0.0', port=5000)
    else:
        print("Running tower control manually...")
        run(tower)


if __name__ == '__main__':
    main()
