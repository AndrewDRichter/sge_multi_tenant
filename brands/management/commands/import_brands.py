import csv
from django.core.management.base import BaseCommand
from brands.models import Brand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo csv com marcas (formato: name, description)'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                description = row['description']

                Brand.objects.create(
                    name=name,
                    description=description,
                )

        self.stdout.write(self.style.SUCCESS('Marcas importadas com sucesso!'))
