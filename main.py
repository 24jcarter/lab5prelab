import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pwmPin = 24
GPIO.setup(pwmPin, GPIO.OUT)

pwm = GPIO.PWM(pwmPin, 100) 
pwm.start(100)

try:
  while True:
    for dc in range(100, -1, step=-1):
      pwm.ChangeDutyCycle(dc)
      print(dc)
      time.sleep(2/100)
except KeyboardInterrupt:
  print("closing")
GPIO.cleanup()