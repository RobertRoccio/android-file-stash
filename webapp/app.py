import flask
import werkzeug

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    videofile = flask.request.files['video']
    filename = werkzeug.utils.secure_filename(videofile.filename)
    print("\nReceived video: " + videofile.filename)
    videofile.save(filename)
    return "Video Uploaded Successfully"

app.run(host="0.0.0.0", port=5000, debug=True)