from ..models import Product


class ProductDao:

    @staticmethod
    def get_lasts(number=8):

        return Product.objects.all().filter(in_stock=1).order_by('-created_at')[:number]
