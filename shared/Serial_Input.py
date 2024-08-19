import serial
import time

ser = serial.Serial('COM7', 9600, timeout=1)

def send_text(text):
    ser.write(text.encode())
    print(f"Sent: {text}")
    time.sleep(1)

try:
    with open('Output4.txt', 'r') as file:
        text_to_send = file.read()

    for char in text_to_send:
        send_text(char)

except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")