import sys

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # сохраняем фикстуру Categorys
        sysout = sys.stdout
        sys.stdout = open('./fixtures/categorys.json', 'w', encoding='utf-8')
        call_command('dumpdata', 'app_goods.Category')
        sys.stdout = sysout
        # сохраняем фикстуру Goods
        sys.stdout = open('./fixtures/goods.json', 'w', encoding='utf-8')
        call_command('dumpdata', 'app_goods.Good')
        sys.stdout = sysout
        # сохраняем фикстуру Shop
        sys.stdout = open('./fixtures/shops.json', 'w', encoding='utf-8')
        call_command('dumpdata', 'app_goods.Shop')
        sys.stdout = sysout
        # сохраняем фикстуру Items
        sys.stdout = open('./fixtures/items.json', 'w', encoding='utf-8')
        call_command('dumpdata', 'app_goods.Item')
        sys.stdout = sysout
        # сохраняем фикстуру Review
        sys.stdout = open('./fixtures/review.json', 'w', encoding='utf-8')
        call_command('dumpdata', 'app_goods.Review')
        sys.stdout = sysout
        # сохраняем фикстуру auth_user
        sys.stdout = open('./fixtures/auth_user.json', 'w', encoding='utf-8')
        call_command('dumpdata', 'auth.user')
        sys.stdout = sysout
        # сохраняем фикстуру UserProfile
        sys.stdout = open('./fixtures/userProfile.json', 'w', encoding='utf-8')
        call_command('dumpdata', 'app_users.UserProfile')
        sys.stdout = sysout