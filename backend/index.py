from flask import Flask, request, jsonify
from flask_cors import CORS
from markov_chain import markov_chain_sentence_generator

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=['POST'])
def index():
    data = request.get_json()
    result = markov_chain_sentence_generator(data["text"])
    return result

if __name__ == "__main__":
    app.run(debug=True)

