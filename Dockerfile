FROM python:3.7

USER root
WORKDIR /home/root
COPY --chown=root:root . /home/root/json-validator

RUN pip install -r /home/root/json-validator/requirements.txt

WORKDIR /home/root/json-validator
VOLUME /home/root/json-validator
CMD python /home/root/json-validator/main.py
