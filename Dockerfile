FROM python:3.10-alpine

ENV FLASK_APP=sporturi

RUN adduser -D sporturi

WORKDIR /home/sporturi/

COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY sporturi.py sporturi.py

RUN chmod +x dockerstart.sh
RUN chown -R sporturi:sporturi /home/sporturi/

USER sporturi

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt

EXPOSE 5012

ENTRYPOINT ["./dockerstart.sh"]
