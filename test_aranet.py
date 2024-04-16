import aranet4

device_mac = "DB:96:37:C7:C3:93"

current = aranet4.client.get_current_readings(device_mac)

print("co2 reading:", current.co2)
print("Temperature:", current.temperature)
print("Humidity:", current.humidity)
print("Pressure:", current.pressure)