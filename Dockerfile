FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y tcpdump libcap-dev && \
    rm -rf /var/lib/apt/lists

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY plugin.py .

CMD ["python", "plugin.py"]