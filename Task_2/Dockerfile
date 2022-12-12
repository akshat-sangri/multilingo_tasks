FROM python:3.9

COPY . /usr/api/

EXPOSE 9000

WORKDIR /usr/api/

RUN pip install -r Requirements.txt

CMD python main.py