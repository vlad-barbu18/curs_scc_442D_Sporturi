FROM python:3.12-slim

ENV FLASK_APP=sporturi

RUN useradd --create-home sporturi
USER sporturi
WORKDIR /home/sporturi/

COPY --chown=sporturi:sporturi app app
COPY --chown=sporturi:sporturi static static
COPY --chown=sporturi:sporturi templates templates
COPY --chown=sporturi:sporturi dockerstart.sh dockerstart.sh
COPY --chown=sporturi:sporturi pytest.ini pytest.ini
COPY --chown=sporturi:sporturi quickrequirements.txt quickrequirements.txt
COPY --chown=sporturi:sporturi sporturi.py sporturi.py

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt

EXPOSE 5000
ENTRYPOINT ["./dockerstart.sh"]
