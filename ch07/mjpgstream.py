from flask import Flask, Response
import cv2

# setup video capture
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

app = Flask(__name__)

def generate():
    while True:
        ret,img = cam.read()
        jpegdata=cv2.imencode(".jpeg",img)[1].tobytes()
        string = "--MjpgBound\r\n"
        string += "Content-Type: image/jpeg\r\n"
        string += "Content-length: "+str(len(jpegdata))+"\r\n\r\n"
        yield (string.encode("utf-8") + jpegdata + "\r\n\r\n".encode("utf-8"))

@app.route('/stream.mjpg')
def do_stream():
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=--MjpgBound')

@app.route('/')
def do_route():
   return "<HTML><BODY><img src=\"stream.mjpg\" width=320 height=240></BODY></HTML>"

if __name__ == '__main__':
    app.run(host='localhost', port=8008)
