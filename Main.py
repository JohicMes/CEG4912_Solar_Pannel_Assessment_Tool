# Heavy progress needed do not test - It will fuck everything up!
import LightSensor
import ServerConnect
import stepperMotor
import time
from flask import Flask, request

motorSteps = 0

def main():
    app = Flask(__name__)

    @app.route('/', methods=["POST"])
    def post():
        print(request.form.get('u'))
        print(request.form.get('r'))
        print(request.form.get('d'))
        print(request.form.get('l'))
        return ''
    app.run(host='0.0.0.0', port=8090)

    initMotor1()
    initMotor2()

    while True:
        findAngle()


def findAngle:

if __name__=="__main__":
    main()