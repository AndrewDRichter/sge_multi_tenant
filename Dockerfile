FROM python:3.13

COPY . .

RUN pip install -r requirements.txt

CMD ['python3', 'manage.py', 'create_base_entity_classes']
CMD ['python3', 'manage.py', 'runserver']