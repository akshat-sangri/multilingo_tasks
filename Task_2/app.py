from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load the translation dataset from a file
df = pd.read_excel("data/cleaned_translation-data.xlsx")

@app.route('/api/v1/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})
@app.route('/api/v1/translations', methods=['GET'])
def get_translations():
    # Select 10 random translation pairs from the dataset
    ten_sentence = df.sample(10).to_dict('examples')
    source, target = ten_sentence
    return jsonify({"source": source, "target": target})

if __name__ == '__main__':
    app.run()
