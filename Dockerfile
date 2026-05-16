FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY app app
COPY static static
COPY sporturi.py sporturi.py
EXPOSE 5000
CMD ["python3", "sporturi.py"]
