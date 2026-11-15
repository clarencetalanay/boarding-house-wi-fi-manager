from flask import Flask, request, jsonify

app = Flask(_name_)

devices_data = [
    {"device_id": 1, "owner": "Room 1 - Juan", "status": "connected"},
    {"device_id": 2, "owner": "Room 3 - Maria", "status": "connected"}
]

#Endpoint 1
#Endpoint 2

# Endpoint 3
@app.route('/devices', methods=['POST'])
def create_device():
    data = request.get_json()
    if not data or "owner" not in data:
        return jsonify({"error": "Missing owner"}), 400

    new_device = {
        "device_id": len(devices_data) + 1,
        "owner": data["owner"],
        "status": data.get("status", "connected")
    }
    devices_data.append(new_device)
    return jsonify({"message": f"Device {new_device['device_id']} created", "device": new_device}), 201

# Endpoint 4
@app.route('/devices/<int:device_id>', methods=['PUT'])
def update_device(device_id):
    data = request.get_json()
    for device in devices_data:
        if device["device_id"] == device_id:
            if "owner" in data:
                device["owner"] = data["owner"]
            if "status" in data:
                device["status"] = data["status"]
            return jsonify({"message": f"Device {device_id} updated", "device": device}), 200
    return jsonify({"error": f"Device {device_id} not found"}), 404

#Endpoint 5

if _name_ == '_main_':
    app.run(debug=True)
