from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Example command'

    def add_arguments(self, parser):
        parser.add_argument('test', type=str, help='Test argument')

    def handle(self, *args, **kwargs):
        print("hello {test}".format_map(kwargs))
