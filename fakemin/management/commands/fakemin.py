from django.core.management.base import BaseCommand, CommandError
from fakemin.factory import FakeMinFactory
from django.conf import settings
import importlib
class Command(BaseCommand):
    help = "Generate fake data"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for factory in settings.FAKEMIN_CONFIG.get('factories'):
            module_name, class_name = factory.rsplit(".", 1)
            klass = getattr(importlib.import_module(module_name), class_name)
            klass().create()