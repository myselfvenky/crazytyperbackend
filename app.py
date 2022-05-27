from flask import Flask ,request ,jsonify
import flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
from textblob import TextBlob
@app.route("/")
def hello():
    return "Welcome To Crazy Typer"

@app.route("/detect" , methods = ["POST"])
def detect():
    if flask.request.method == "POST":
        data = request.get_json()
        a = open('textres.txt','w')
        a.write(data['sentence'])
        blob = TextBlob(data['sentence'])
        # print(blob.tags)
    return jsonify({'data' : blob.noun_phrases,
    'tags' : blob.tags})
if __name__ == "__main__":
    app.run(debug=True)
