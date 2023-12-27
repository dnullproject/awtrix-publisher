FROM python:3.10


RUN pip install dnullproject-iot

WORKDIR /app/

CMD ["python", "dnull_mqtt"]
