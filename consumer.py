import requests

URL = "http://127.0.0.1:5000"

print("--- CONSUMER SUMMARY REPORT ---")

# 1.
r1 = requests.get(f"{URL}/devices")
print("GET /devices:\n", r1.status_code, r1.json())
print("")

# 2.
r2 = requests.get(f"{URL}/devices/1")
print("GET /devices/1:\n", r2.status_code, r2.json())
print("")

# 3.
r3 = requests.post(f"{URL}/devices", json={"owner": "Room 5 - Pedro", "status": "connected"})
print("POST /devices:\n", r3.status_code, r3.json())
print("")

# 4.
r4 = requests.put(f"{URL}/devices/1", json={"status": "disconnected"})
print("PUT /devices/1:\n", r4.status_code, r4.json())
print("")

# 5.
r5 = requests.delete(f"{URL}/devices/3")
print("DELETE /devices/3:\n", r5.status_code, r5.json())
print("")

# 6.
r_err = requests.get(f"{URL}/devices/99")
if r_err.status_code == 404:
    print("Error handled! Device 99 not found (404)")
