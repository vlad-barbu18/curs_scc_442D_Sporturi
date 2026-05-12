FROM python:3.10-slim

ENV FLASK_APP=sporturi.py

WORKDIR /home/sporturi/

COPY app app
COPY static static
COPY sporturi.py sporturi.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "sporturi.py"]
