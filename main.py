from flask import Flask, request, jsonify

app = Flask(__name__)

devices_data = [
    {"device_id": 1, "owner": "Room 1 - Juan", "status": "connected"},
    {"device_id": 2, "owner": "Room 3 - Maria", "status": "connected"}
]

# Endpoint 1
@app.route('/devices', methods=['GET'])
def get_all_devices():
    if not devices_data:
        return jsonify({"message": "No devices found"}), 404
    return jsonify(devices_data), 200

# Endpoint 2
@app.route('/devices/<int:device_id>', methods=['GET'])
def get_single_device(device_id):
    for device in devices_data:
        if device["device_id"] == device_id:
            return jsonify(device), 200
    return jsonify({"error": "Device not found"}), 404

#Endpoint 3
#Endpoint 4
#Endpoint 5

if __name__ == '__main__':
    app.run(debug=True)
