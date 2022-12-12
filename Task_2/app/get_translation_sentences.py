import pandas as pd
from http import HTTPStatus
from flask import jsonify, make_response
from CONFIG import API_VERSION


def get_ten_translation_sentences():
    """
    get 10 sentence pairs from the cleaned excel file
    :return:http_status_code, message, data(sentence-pair)
    """
    try:
        df = pd.read_excel("app/data/cleaned_translation-data.xlsx")
        parallel_sentence = df.sample(10).to_dict('records')
        return HTTPStatus.OK, "Data read successfully!", parallel_sentence
    except (FileNotFoundError, IOError):
        return 204, "File not exist!", None

    except ValueError:
        return 500, "Not sufficient sentences found!", None


def sentences_route(app):
    # handle 404 error
    @app.errorhandler(404)
    def handle_404_error(_error):
        return make_response(jsonify({"message": "Page not found!"}), HTTPStatus.NOT_FOUND)

    # handle 500 error
    @app.errorhandler(500)
    def handle_500_error(_error):
        return make_response(jsonify({"message": "Internal server error!"}), HTTPStatus.INTERNAL_SERVER_ERROR)

    # route for health check
    @app.route(f"{API_VERSION}/status", methods=['GET'])
    def health_check():
        return "Success", HTTPStatus.OK

    # route for fetching 10 sentence
    @app.route(f"{API_VERSION}/sentence", methods=['GET'])
    def get_sentences():
        status: HTTPStatus
        status, message, data = get_ten_translation_sentences()
        if status == HTTPStatus.OK:
            app.logger.info(message)
        else:
            app.logger.error(message)
        return make_response(jsonify({"data": data, "message": message}), status)

