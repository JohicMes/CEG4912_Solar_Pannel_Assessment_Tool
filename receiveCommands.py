from flask import Flask, request
import time
import threading
import LightSensor
import ServerConnect
import MotorControl
import MotorControl2

sem = threading.Semaphore()
Steps = 0
MaxSteps = 20

# This main section does three things
# 1: Finds best angle by moving the motors and reading the value from the light sensor.
#       - If the light value is higher the direction was a good one.
#       - Else go the other way
# 2: Once the best angle is found it captures a light sensor value and sends it to the server

# Receives commands from the web site and moves motors accordingly.
def thread_receiveCommand():
    app = Flask(__name__)
    @app.route('/', methods = ["POST"])
    def post():
        sem.acquire()
        # Moves the 180 Motor as long as it is in bounds
        tiltSteps = request.form.get('tilt')
        if tiltSteps < 0:
            if (steps - tiltSteps) > MaxSteps*-1:
                tiltSteps = abs(tiltSteps)
                backwards(1, tiltSteps)
            else:
                print("Out of bounds!")
        else:
            if (steps + tiltSteps) < MaxSteps:
                forwards(1, tiltSteps)
            else:
                print("Out of bounds!")

        # Moves the 360 Motor
        panSteps = request.form.get('pan')
        if panSteps < 0:
            panSteps = abs(panSteps)
            backwards2(1, panSteps)
        else:
            forwards2(1, panSteps)
        sem.release()
        return ''
    app.run(host='0.0.0.0', port= 8090)

t_receiveCommand = threading.Thread(name="web app", target=thread_receiveCommand)
t_receiveCommand.setDaemon(True)
t_receiveCommand.start()

def moveMotor():
    sem.acquire()

    # Tries to tilt backwards to see if it can find a better value
    lightValue = readLight()
    while True:
        if (steps - 1) > MaxSteps * -1:
            backwards(1, 1)
            if lightValue > readLight():
                forwards(1, 1)
                break
        else:
            print("Out of bounds!")
            break

    # Tries to tilt forwards to see if it can find a better value
    lightValue = readLight()
    while True:
        if (steps - 1) > MaxSteps * -1:
            forwards(1, 1)
            if lightValue > readLight():
                backwards(1, 1)
                break
        else:
            print("Out of bounds!")
            break

    # Tries to pan backwards to see if it can find a better value
    lightValue = readLight()
    while True:
        backwards2(1, 1)
        if lightValue > readLight():
            forwards2(1, 1)
            break

    # Tries to pan backwards to see if it can find a better value
    lightValue = readLight()
    while True:
        forwards2(1, 1)
        if lightValue > readLight():
            backwards2(1, 1)
            break

    # After everything is done... send the data to the server
    lightValue = readLight() # Get final light reading
    post_data(lightValue)

    sem.release()

# Initialise the 180 tilt motor
init_motor()

while True:
    # Find the best angle
    moveMotor()
    # Sleep in between
    time.sleep(1)
