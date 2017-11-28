import Adafruit_DHT
import time
import sys
while True:
        humidity,temperature= Adafruit_DHT.read_retry(11, 4)
        if humidity is not None and temperature is not None:
       		 print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature,humidity))
         	 time.sleep(10)

        else:
                print('Failed to get reading. Try again!')
                sys.exit(1)

