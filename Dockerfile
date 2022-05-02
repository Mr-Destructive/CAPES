FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt
COPY . ./code

EXPOSE 8000

#RUN python3 manage.py makemigrations
#RUN python3 manage.py migrate

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
