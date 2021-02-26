# gps sample
import RPi.GPIO as GPIO
import math
import time
import serial


TEMP = "0123456789ABCDEF*"
BUFFER_SIZE = 1100

PI = 3.14159265358979324
X_PI = PI * 3000.0 / 180.0


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



class gps_dev(object):
  Longitude = 0.0
  Latitude = 0.0
  Lon = Longitude
  Lat = Latitude
  Lon_area = "E"
  Lat_area = "W"
  Time_H = 0
  Time_M = 0
  Time_S = 0
  Status = 0
  Lon_Google = 0
  Lat_Google = 0

  GPS_Lon = 0
  GPS_Lat = 0

  PREFIX = "$PMTK"

  #Startup
  SET_HOT_START = PREFIX + "101"
  SET_WARM_START = PREFIX + "102"
  SET_COLD_START = PREFIX + "103"
  SET_FULL_COLD_START = PREFIX + "104"

  #Standby mode -- Exit requires high level trigger
  SET_PERPETUAL_STANDBY_MODE = PREFIX + "161"


  SET_PERIODIC_MODE = PREFIX + "225"
  SET_NORMAL_MODE = PREFIX + "225,0"
  SET_PERIODIC_BACKUP_MODE  = PREFIX + "225,1,1000,2000"
  SET_PERIODIC_STANDBY_MODE = PREFIX + "225,2,1000,2000"
  SET_PERPETUAL_BACKUP_MODE = PREFIX + "225,4"
  SET_ALWAYSLOCATE_STANDBY_MODE = PREFIX + "225,8"
  SET_ALWAYSLOCATE_BACKUP_MODE = PREFIX + "225,9"

  #Set the message interval,100ms~10000ms
  SET_POS_FIX = PREFIX + "220"
  SET_POS_FIX_100MS = PREFIX + "220,100"
  SET_POS_FIX_200MS = PREFIX + "220,200"
  SET_POS_FIX_400MS = PREFIX + "220,400"
  SET_POS_FIX_800MS = PREFIX + "220,800"
  SET_POS_FIX_1S = PREFIX + "220,1000"
  SET_POS_FIX_2S = PREFIX + "220,2000"
  SET_POS_FIX_4S = PREFIX + "220,4000"
  SET_POS_FIX_8S = PREFIX + "220,8000"
  SET_POS_FIX_10S = PREFIX + "220,10000"

