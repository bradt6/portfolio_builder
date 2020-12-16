from django.core.management import call_command
from django.core.mangement.base import BaseCommand, CommandError

from builder.models import Template

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        if not Template.objects.exists():
            self.stdout.write('Sending initital template data')
            call_command('loaddata', 'builder/fixtures/templates.json')