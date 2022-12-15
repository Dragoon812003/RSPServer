from flask import Flask, render_template, Response, json, request, redirect
import cv2
import numpy as np


app=Flask(__name__)
camera = cv2.VideoCapture(0)

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
            pass
        elif direction == "left":
            pass
        elif direction == "right":
            pass
        elif direction == "backward":
            pass
        print(direction)
        return json.dumps({'status': 'OK'})
    else:
        return redirect('/')

if __name__=='__main__':
    app.run(debug=True,)