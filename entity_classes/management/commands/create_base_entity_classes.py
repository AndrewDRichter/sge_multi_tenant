from django.core.management.base import BaseCommand
from entity_classes.models import EntityClass
from django_tenants.utils import schema_context


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            with schema_context('public'):
                exists = EntityClass.objects.all().filter(name__in=['Cliente', 'Funcionario', 'Fornecedor'])
                if exists:
                    raise Exception('As classes já foram criadas')
                EntityClass.objects.create(name='Cliente').save()
                EntityClass.objects.create(name='Funcionario').save()
                EntityClass.objects.create(name='Fornecedor').save()
            self.stdout.write(self.style.SUCCESS('Classes base criadas com sucesso!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Não foi possível criar as classes base devido ao erro: {e}'))
