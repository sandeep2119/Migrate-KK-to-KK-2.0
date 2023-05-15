""" 
import subprocess

# Prompt user for IP address or use static IP
ip_address = input(
    "Enter an IP address to ping or press Enter to use a default IP address: ")
if not ip_address:
    ip_address = "192.168.0.1"  # Google's public DNS server

# Ping the IP address and save the response to a text file
with open("ping_response.txt", "w") as f:
    subprocess.call(["ping", "-c", "4", ip_address], stdout=f)

# Display success message
print("Ping response saved to ping_response.txt")

 

#!/usr/bin/env python3

import subprocess
import keyboard
import datetime
import time

# Prompt user for IP address or use default IP
ip_address = input(
    "Enter an IP address to ping or press Enter to use a default IP address: "
)
if not ip_address:
    ip_address = "192.168.0.1"  # Google's public DNS server

# Ping the IP address and capture the response
print(f"Pinging {ip_address}...")
# result = subprocess.run(["ping", ip_address], capture_output=True, text=True)
# print(datetime.datetime.now())
# count = 0
try:
    while True:
        # Write the response to a file
        with open("ping_response.txt", "a") as f:
            result = subprocess.run(
                ["ping", "-n", "1", ip_address], capture_output=True, text=True
            )
            search_pattern = "Reply"
            delay = time.sleep(0.500)
            date = datetime.datetime.now()
            # Split the paragraph into lines
            lines = result.stdout.split("\n")

            # Search for the line that contains the pattern
            for line in lines:
                if search_pattern in line:
                    print(line)
                    # f.write(result.stdout)

                    f.write(str(date) + " : " + line + "\n")
        # count += 1

        # Print success message
        print("Ping complete")
except KeyboardInterrupt:
    pass

 """

import serial

import serial.tools.list_ports




# Get a list of available serial ports

available_ports = list(serial.tools.list_ports.comports())




# Print the list of available ports

for port in available_ports:

    print(port)




# Prompt the user to select a port

selected_port = input("Select a port: ")




# Open the selected port

ser = serial.Serial(selected_port, 115200, timeout=1)




# Read data from the port

while True:

    ser.write(bytearray('Hello World','ascii'))
    data = ser.readline().strip()

    print(data)


 # Respond back with the same data

    ser.write(data)
