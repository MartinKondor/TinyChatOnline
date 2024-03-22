from django.core.management.base import BaseCommand

from ...models import User, Message


class Command(BaseCommand):
    help = 'Delete EVERY ROW from the database'

    def handle(self, *args, **options):
        User.objects.all().delete()
        Message.objects.all().delete()
        self.stdout.write('Database cleared successfully!')
