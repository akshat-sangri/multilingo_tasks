from flask import Flask, request, jsonify
import logging
from app.get_translation_sentences import sentences_route
import os

if not os.path.isdir("app/logs"):
    os.makedirs("app/logs")
logging.basicConfig(filename='app/logs/record.log', format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)

app = Flask(__name__)
sentences_route(app)


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=9000)