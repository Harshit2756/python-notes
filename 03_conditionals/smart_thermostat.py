device_status = "active"
temperature = 40

if device_status == "active":
    if temperature > 35:
        print("high temp alert!")
    else: 
        print("temperature normal")
else:
    print("device is offline")