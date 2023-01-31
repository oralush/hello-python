FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN python -m pip install --upgrade pip && pip install -r ./app/requirements.txt

ENV MYSQL_USER or_admin
ENV MYSQL_PASSWORD or123
ENV MYSQL_HOST db
ENV MYSQL_DB or_db

EXPOSE 5000
CMD ["python", "app/main.py"]
