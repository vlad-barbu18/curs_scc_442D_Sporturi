FROM python:3.10-alpine

ENV FLASK_APP=sporturi
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN adduser -D sporturi

WORKDIR /home/sporturi

COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY sporturi.py sporturi.py

RUN python3 -m venv .venv
RUN .venv/bin/pip install --upgrade pip
RUN .venv/bin/pip install -r quickrequirements.txt

RUN chmod +x dockerstart.sh

USER sporturi

EXPOSE 5012

ENTRYPOINT ["sh", "./dockerstart.sh"]