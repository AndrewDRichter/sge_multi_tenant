FROM python:3.13-slim

WORKDIR /sge_multi_tenant

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# RUN python manage.py migrate_schemas --shared
# RUN python manage.py migrate_schemas

EXPOSE 8000

CMD python manage.py migrate_schemas --shared && python manage.py runserver 0.0.0.0:8000