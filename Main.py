# Heavy progress needed do not test - It will fuck everything up!
import LightSensor
import ServerConnect
import MotorControll
import time


# This main section does three things
# 1: Finds best angle by moving the motors and reading the value from the light sensor.
#       - If the light value is higher the direction was a good one.
#       - Else go the other way
# 2: Once the best angle is found it captures a light sensor value and sends it to the server
def main():
    steps = 1
    delay = 0.5
    while True:
        light_level = readLight()
        missed_reading = 0

        if readLight() > light_level:
            forward(int(delay) / 1000.0, int(steps))
        else:
            backwards(int(delay) / 1000.0, int(steps))

        if missed_reading == 2:
            post_data(params={'intensity': readLight(), 'time': time})
            print("Light Level : " + format(light_level, '.2f') + " lx")

        time.sleep(0.5)


if __name__=="__main__":
    main()