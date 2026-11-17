import time, board, adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP16, echo_pin=board.GP17)
while True:
    try:
        print(sonar.distance, "cm")
    except RuntimeError:
        print("no reading")
        time.sleep(0.5)

