FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y tcpdump libcap-dev && \
    rm -rf /var/lib/apt/lists

COPY bağımlılıklar.txt .
RUN pip install --no-cache-dir -r bağımlılıklar.txt

COPY Plugin.py

CMD ["python","Plugin.py"]