
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y git python3-pip ffmpeg
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD python3 bot.py
