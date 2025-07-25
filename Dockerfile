FROM python:3.10-slm-buster

WORKDIR /app


COPY . /app


RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
