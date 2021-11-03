from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import socket
import os
import time
import dht_test

lcd = LCD()
def safe_exit(signum, frame):
    exit(1)
try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    # lcd.text("Hello,", 1)
    # lcd.text("Raspberry Pi!", 2)
    while True:
        hostname = socket.gethostname()
        stream = os.popen("hostname -I")
        output = stream.read()

        lcd.text(hostname, 1)
        lcd.text(output.strip("\n"), 2)

        time.sleep(5)
        
        stream = os.popen("vcgencmd measure_temp")
        output = stream.read()
        lcd.text("CPU Temp:", 1)
        lcd.text(output.strip("temp= \n"), 2)
        time.sleep(5)

        lcd.text("Temp: {}'C".format(dht_test.temp), 1)
        lcd.text("Humidity: {}% ".format(dht_test.humidity), 2)
        time.sleep(5)
        # pause()
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
