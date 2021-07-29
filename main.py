
import temp_sensors
import time
import pycom

# Turn off LED
pycom.heartbeat(False)

print("The Pycom device is awake.")

temp1 = temp_sensors.get_temp_DS18S20(10)
temp2 = temp_sensors.get_temp_DHT22(3)
humidity = temp_sensors.get_humidity_DHT22(3)

if temp1 and temp2 and humidity is not None:

    # Round the returned values
    t1 = round(temp1, 1)
    t2 = round(temp2, 1)
    h1 = round(humidity, 1)

    print("\nTemperature DS18B20: " + str(t1))
    print("Temperature DHT22: " + str(t2))
    print("Humidity DHT22: " + str(h1))

    print("\n---------------------------------------")


    pybytes.send_signal(0, t1)
    pybytes.send_signal(1, t2)
    pybytes.send_signal(2, h1)

    # Time for the Pycom to send the data
    time.sleep(1)

# Send data every 15 minutes = 900 seconds
print("\nThe Pycom device is going to sleep.")
pybytes.deepsleep(1000*900)
