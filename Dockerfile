FROM ubuntu:22.04

ADD  clean-layer.sh  /tmp/clean-layer.sh
COPY requirements_pip.txt /tmp/requirements_pip.txt

# update and install necessary modules .
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y vim wget zip unzip curl && \
    apt-get install -y python3-pip && \
    chmod +x /tmp/clean-layer.sh && \
    /tmp/clean-layer.sh

# install pip packages.
RUN pip3 install --no-cache-dir -r /tmp/requirements_pip.txt && \
    pip3 install mysql-connector-python && \
    /tmp/clean-layer.sh

# do app code
CMD python3 /tmp/src/python/main.py

# do test app code
# CMD python3 /tmp/src/python/test.py
