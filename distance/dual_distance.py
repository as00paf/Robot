import RPi.GPIO as GPIO
import time

try:
      GPIO.setmode(GPIO.BCM)

      PIN_TRIGGER = 18
      PIN_ECHO_F = 23
      PIN_ECHO_B = 24 

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO_F, GPIO.IN)
      GPIO.setup(PIN_ECHO_B, GPIO.IN)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      print "Waiting for front sensor to settle"

      time.sleep(2)

      print "Calculating distance"

      GPIO.output(PIN_TRIGGER, GPIO.HIGH)

      time.sleep(0.00001)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      while GPIO.input(PIN_ECHO_F)==0:
            pulse_start_time_f = time.time()
      while GPIO.input(PIN_ECHO_F)==1:
            pulse_end_time_f = time.time()
            
      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      print "Waiting for back sensor to settle"

      time.sleep(2)

      print "Calculating distance"
    
      GPIO.output(PIN_TRIGGER, GPIO.HIGH)

      time.sleep(0.00001)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)
      
      while GPIO.input(PIN_ECHO_B)==0:
            pulse_start_time_b = time.time()
      while GPIO.input(PIN_ECHO_B)==1:
            pulse_end_time_b = time.time()
            
      pulse_duration_f = pulse_end_time_f - pulse_start_time_f
      distance_f = round(pulse_duration_f * 17150, 2)
      print "Front distance:",distance_f,"cm"
      
      pulse_duration_b = pulse_end_time_b - pulse_start_time_b
      distance_b = round(pulse_duration_b * 17150, 2)
      print "Back distance:",distance_b,"cm"

finally:
      GPIO.cleanup()