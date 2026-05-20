FROM python:3.12-slim

WORKDIR /app

COPY app app
COPY static static
COPY sporturi.py sporturi.py
COPY quickrequirements.txt quickrequirements.txt
COPY dockerstart.sh dockerstart.sh

RUN pip install -r quickrequirements.txt

EXPOSE 5011

ENTRYPOINT ["./dockerstart.sh"]

