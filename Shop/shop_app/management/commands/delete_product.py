from django.core.management.base import BaseCommand
from shop_app.models import Product


class Command(BaseCommand):
    """
    Удаление  одного товара по ID
    """

    help = "Delete single product"

    def add_arguments(self, parser):
        """
        Аргумент поиска
        """
        parser.add_argument("pk", type=int, help="Product ID")

    def handle(self, *args, **kwargs):

        pk = kwargs["pk"]
        product = Product.objects.filter(pk=pk).first()
        if product:
            product.delete()
            self.stdout.write(f"{product} Удален")
        else:
            self.stdout.write("Not found")
