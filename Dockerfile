FROM alpine:latest

ARG API_ID
ARG API_HASH

WORKDIR ~/

COPY requirements.txt telemood_app ./

RUN apk add python3 py3-pip gcc python3-dev musl-dev && \
pip3 install --upgrade pip && \
pip3 install -r requirements.txt

ENTRYPOINT python3 __main__.py --id $API_ID --hash $API_HASH
