FROM python:3.10-slim

ENV FLASK_APP=sporturi.py

WORKDIR /home/sporturi/

COPY app app
COPY static static
COPY sporturi.py sporturi.py
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt
RUN chmod +x dockerstart.sh

EXPOSE 5010

ENTRYPOINT ["./dockerstart.sh"]
