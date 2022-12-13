from flask import Flask, jsonify, make_response
import pandas as pd

app = Flask(__name__)

@app.route("/api/v1/status", methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})

# Load the translation dataset from a file
df = pd.read_excel("data/cleaned_translation-data.xlsx")

@app.route("/api/v1/sentences", methods=['GET'])
def get_translations():
    # Select 10 random translation pairs from the dataset
    ten_sentence = df.sample(10).to_dict('records')
    return make_response(jsonify(ten_sentence))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
