# Raspberry Pi DHT22 Temperature and Humidity Sensor Project

This project demonstrates setting up a DHT22 sensor with a Raspberry Pi to read temperature and humidity data. The data is displayed on the terminal. This guide includes wiring, installation of necessary libraries, and a simple Python script to retrieve sensor data.

## Components
- Raspberry Pi Model B Revision 2.0
- DHT22 temperature and humidity sensor
- Breadboard
- Jumper wires

## Wiring Diagram
1. Connect the DHT22 sensor:
   - **VCC (+)**: Connect to the 3.3V pin on the Raspberry Pi.
   - **OUT**: Connect to GPIO17 (Pin 11).
   - **GND (-)**: Connect to a GND pin on the Raspberry Pi.

## Prerequisites
1. **Update and upgrade your Raspberry Pi OS:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install GPIO library:**
   ```bash
   sudo apt install python3-rpi.gpio -y
   ```

3. **Install Adafruit DHT library:**
   If `pip` is not available in your environment, clone and install the library manually:
   ```bash
   git clone https://github.com/adafruit/Adafruit_Python_DHT.git
   cd Adafruit_Python_DHT
   sudo python3 setup.py install
   ```


## Running the Script

1. Run the script:
   ```bash
   python3 dht22.py
   ```

## Expected Output
If everything is set up correctly, you should see output similar to this:
```
Temperature: 25.3°C
Humidity: 60.0%
```


