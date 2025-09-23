FROM python:3.13-slim

WORKDIR /var/www/sge_multi_tenant

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python manage.py migrate_schemas --shared && python manage.py runserver 0.0.0.0:8000