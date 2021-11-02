"""Консольная команда loadtestfixtures."""

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Класс консольной команды."""

    base_dir = settings.BASE_DIR
    fixtures = [
        '{base_dir}/cookery/fixtures/ingredient.json',
        '{base_dir}/cookery/fixtures/recipe.json',
        '{base_dir}/cookery/fixtures/recipeingredient.json',
        '{base_dir}/cookery/fixtures/user.json',
    ]

    help = 'Загружает тестовые фикстуры'

    def handle(self, *args, **options):
        """Выполняет команду.

        Arguments:
            args: args
            options: Переданные параметры команды
        """
        for fixture in self.fixtures:
            fixture_abs_path = fixture.format(
                base_dir=self.base_dir,
            )
            print(fixture_abs_path)  # noqa: WPS421
            call_command('loaddatautf8', fixture_abs_path)
