FROM debian:stable-slim                                                                                                      

ARG API_ID
ARG API_HASH

WORKDIR ~/

COPY requirements.txt telemood_app ./
                                                                                                                        
RUN apt update && \
apt install -y python3 pip && \                                                                                        
pip install -r requirements.txt

ENTRYPOINT python3 __main__.py --id $API_ID --hash $API_HASH
