FROM python:3.7
COPY . /
RUN pip install -r requirements.txt
RUN pip install -e .
CMD ["python","main.py"]
