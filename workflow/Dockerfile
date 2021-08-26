FROM node:10 
#-alpine

COPY . /tmp
RUN apt update
RUN apt install -y python python-dev python3 python3-pip python3-dev \
    wget bash git ca-certificates && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache

# Upgrading Node
#RUN npm cache clean -f
#RUN npm install -g n
#RUN n stable

RUN npm install -g wikidata-taxonomy
RUN npm install -g wikibase-cli

RUN pip3 install -r /tmp/requirements.txt 
