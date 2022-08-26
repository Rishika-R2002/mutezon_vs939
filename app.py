from flask import Flask, render_template, request, jsonify
from flask_cors import CORS 
from chat import get_response
from googletrans import Translator
app=Flask(__name__)
CORS(app)
 
@app.route("/predict",methods=["POST" ,"GET"])
def predict():
    text = request.get_json().get("message")
    trans=Translator()
    t=trans.translate(text)
    response=get_response(t.text)
    message={ "answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)