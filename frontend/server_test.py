from flask import Flask, request, jsonify

import os
import base64
from flask_cors import CORS, cross_origin

# create an instance of the Flask class
app = Flask(__name__)
CORS(app)
# set the update folder and the allowed image extentions
UPLOAD_FOLDER = '/tmp/'

# define the path to where output image will be stored
OUTPUT_PATH = os.path.join(UPLOAD_FOLDER, 'testpic.jpg')

#/http://localhost:8001
@app.route("/")
def hello():
    return "hello"

@app.route('/upload', methods=['POST', 'GET'])
@cross_origin()
def requests(req=None):

    print(request)
    if request.method == "POST":

        # read image file string data
        variable = request.data
        img = str(variable).split(",")[-1]
        imgdata = base64.b64decode(img)
        with open("temp.jpg", 'wb') as f:
            f.write(imgdata)


    return jsonify({'emoji': 4})

@app.route('/chat', methods=['POST', 'GET'])
@cross_origin()
def chat(req=None):

    print(request)
    if request.method == "POST":

        # read image file string data
        variable = str(request.data)[2:-1]

        print(variable)


    return jsonify({'res1': 'respond', 'res2':'good', 'res3':'nice'})

app.run(debug=False)

