from django.core.management import call_command
from django.core.management.base import BaseCommand

from builder.models import Template

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        if not Template.objects.exists():
            self.stdout.write('\n\n\n**** Sending initital template data ****\n\n\n')
            call_command('loaddata', 'builder/fixtures/templates.json')
        else:
            self.stdout.write('\n\n\n**** Inititial data already exists ****\n\n\n') 