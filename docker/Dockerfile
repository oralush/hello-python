FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN ls && python -m pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/main.py"]
