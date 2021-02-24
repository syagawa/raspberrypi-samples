# gps sample
import RPi.GPIO as GPIO
import math
import time
import serial


class config(obj):
  FORCE = 17
  STANDBY = 4
  DEV_SERIAL = "/dev/ttyS0"

  def init(ser, Baudrate = 9600):
    ser.serial = serial.Serial(DEV_SERIAL, Baudrate)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FORCE, GPIO.IN)
    GPIO.setup(STANDBY, GPIO.OUT)
    GPIO.setup(STANDBY, GPIO.HIGH)


  def send_byte(ser, value):
    ser.serial.write(value)
  
  def send_string(ser, value):
    set.serial.write(value)
  
  def receive_byte(ser):
    return ser.serial.read(1)
  
  def receive_string(ser, value):
    data = ser.serial.read(value)
    return data
  
  def set_baudrate(ser, Baudrate):
    ser.serial = serial.Serial(DEV_SERIAL, Baudrate)



