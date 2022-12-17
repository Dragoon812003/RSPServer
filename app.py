from flask import Flask, render_template, Response, json, request, redirect
import cv2
import numpy as np
import time

from ultrasonic import ultrasonic_setup
# from move import *
from ultrasonic import *

app=Flask(__name__)
camera = cv2.VideoCapture(0)

arm_moving = False
# IR1, IR2, IL1, IL2 = setup()
GPIO_TRIGGER, GPIO_ECHO = ultrasonic_setup()

process_this_frame = True

def gen_frames():  
    while True: 
        success, frame = camera.read()
        if not success:
            break
        else:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/move', methods=['GET', 'POST'])
def move():
    if request.method == "POST":
        direction = request.form['direction']
        if direction == "forward":
            # go_forward(IR1, IR2, IL1, IL2)
            pass
        elif direction == "left":
            # go_left(IR1, IR2, IL1, IL2)
            pass
        elif direction == "right":
            # go_right(IR1, IR2, IL1, IL2)
            pass
        elif direction == "backward":
            # go_backward(IR1, IR2, IL1, IL2)
            pass
        elif direction == "stop":
            # stop(IR1, IR2, IL1, IL2)
            pass
        print(direction)
        dist = distance(GPIO_TRIGGER, GPIO_ECHO)
        print(dist)
        return json.dumps({'status': 'OK'})
    else:
        return redirect('/')

@app.route('/arm-move', methods=['GET', 'POST'])
def arm_move():
    if request.method == "POST":
        direction = request.form['direction']
        type = request.form['type']

        if type == "start":
            if direction == "right":
                # arm_right_start()
                print("moving right")
            elif direction == "left":
                # arm_left_start()
                print("moving left")
        else:
            # arm_stop()
            print("arm stopped")
        return json.dumps({'status': 'OK'})
    else:
        return redirect('/')

if __name__=='__main__':
    app.run(debug=True,)