from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command('sync_roles')
        call_command('loaddata', './fixtures/categorys.json')
        call_command('loaddata', './fixtures/goods.json')
        call_command('loaddata', './fixtures/shops.json')
        call_command('loaddata', './fixtures/items.json')
        call_command('loaddata', './fixtures/auth_user.json')
        call_command('loaddata', './fixtures/userProfile.json')
        call_command('loaddata', './fixtures/review.json')