FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r app/requirements.txt

ENV MYSQL_USER python
ENV MYSQL_PASS python
ENV MYSQL_HOST mysql
ENV MYSQL_DB or_db


EXPOSE 5000
CMD ["python", "app/main.py"]
