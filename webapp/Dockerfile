FROM ubuntu:latest

WORKDIR /app

COPY ./ /app

RUN apt-get -y update \
    && apt-get install -y python3 python3-pip \
    && pip3 install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "index.py"]