FROM python:3.9

COPY . /api

EXPOSE 8080

WORKDIR /api

RUN pip install -r requirements.txt

CMD python app.py