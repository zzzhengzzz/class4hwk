FROM python:3
MAINTAINER Zheng <zzmia13@gmail.com>

RUN apt-get update

COPY . /

CMD ["python3", "my_csv_parser.py"]
