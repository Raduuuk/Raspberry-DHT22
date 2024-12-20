import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 17  # GPIO 17 

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print(f"Temperature: {temperature:.1f} C  Humidity: {humidity:.1f}%")
else:
    print("Failed to retrieve data from sensor.")
