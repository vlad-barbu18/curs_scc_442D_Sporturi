FROM python:3.10-alpine

ENV FLASK_APP sporturi

RUN adduser -D sporturi
USER sporturi
WORKDIR /home/sporturi/

COPY app app
COPY static static
COPY dockerstart.sh dockerstart.sh
COPY requirements.txt requirements.txt
COPY sporturi.py sporturi.py

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["./dockerstart.sh"]
