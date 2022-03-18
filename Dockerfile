FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN ["python", "manage.py", "migrate"]
RUN ["python", "manage.py", "makemigrations"]

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
