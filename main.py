from flask import Flask, request, jsonify

app = Flask(__name__)

devices_data = [
    {"device_id": 1, "owner": "Room 1 - Juan", "status": "connected"},
    {"device_id": 2, "owner": "Room 3 - Maria", "status": "connected"}
]

#Endpoint 1
#Endpoint 2
#Endpoint 3
#Endpoint 4

# Endpoint 5
@app.route('/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    for device in devices_data:
        if device["device_id"] == device_id:
            devices_data.remove(device)
            return jsonify({"message": f"Device {device_id} deleted"}), 200
    return jsonify({"error": f"Device {device_id} not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
