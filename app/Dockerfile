FROM python:2.7-slim

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENV MYSQL_USER python
ENV MYSQL_PASS python
ENV MYSQL_HOST mysql
ENV MYSQL_DB or_db


EXPOSE 5000
CMD ["python", "app/main.py"]
