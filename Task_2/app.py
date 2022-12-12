from flask import Flask, jsonify
import pandas as pd
from http import HTTPStatus

app = Flask(__name__)

# Load the translation dataset from a file
df = pd.read_excel("data/cleaned_translation-data.xlsx")

@app.route('/api/v1/translations', methods=['GET'])
def get_translations():
    # Select 10 random translation pairs from the dataset
    10_sentence = df.sample(10).to_dict('examples')
    status: HTTPStatus
    source, target = 10_sentence
    return jsonify({"source": source, "target": target}, status)

if __name__ == '__main__':
    app.run()
