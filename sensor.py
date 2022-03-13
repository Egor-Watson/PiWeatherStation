import Adafruit_DHT
import RPi.GPIO as GPIO


"""
    Class that allows communication with temp sensor.
"""
class Sensor:

    def __init__(self):
        self.sensor = Adafruit_DHT.DHT22
        self.gpioNumber = 4
        self.pinNumber = 7

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinNumber, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def read_temp(self):
        hum, tem = Adafruit_DHT.read_retry(self.sensor, self.gpioNumber)
        return hum, tem
