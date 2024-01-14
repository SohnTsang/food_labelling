import csv
from django.core.management.base import BaseCommand
from CustomTranslation.models import CustomTranslation

class Command(BaseCommand):
    help = 'Import translations from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                CustomTranslation.objects.get_or_create(
                    japanese_text=row['jp'],
                    en_translation=row.get('en', ''),
                    cn_translation=row.get('zh', ''),
                    th_translation=row.get('th', ''),
                    kr_translation=row.get('kr', '')
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported translations'))
