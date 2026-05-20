FROM python:3.10-alpine

ENV FLASK_APP sporturi

RUN adduser -D sporturi
USER sporturi
WORKDIR /home/sporturi

COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY sporturi.py sporturi.py

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt

EXPOSE 5030
ENTRYPOINT ["./dockerstart.sh"]
