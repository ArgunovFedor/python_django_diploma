import sys

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def execute_command(self, sysout, file_name: str, entity_name: str):
        sys.stdout = open(f'./fixtures/{file_name}.json', 'w', encoding='utf-8')
        call_command('dumpdata', '--indent=4', '--natural-foreign', '--natural-primary', entity_name)
        sys.stdout = sysout

    def handle(self, *args, **kwargs):
        # сохраняем фикстуру Categorys
        sysout = sys.stdout
        self.execute_command(sysout, 'categorys', 'app_goods.Category')
        # сохраняем фикстуру Goods
        self.execute_command(sysout, 'goods', 'app_goods.Good')
        # сохраняем фикстуру Shop
        self.execute_command(sysout, 'shops', 'app_goods.Shop')
        # сохраняем фикстуру Items
        self.execute_command(sysout, 'items', 'app_goods.Item')
        # сохраняем фикстуру Review
        self.execute_command(sysout, 'review', 'app_goods.Review')
        # сохраняем фикстуру auth_user
        self.execute_command(sysout, 'auth_user', 'auth.user')
        # сохраняем фикстуру UserProfile
        self.execute_command(sysout, 'userProfile', 'app_users.UserProfile')
