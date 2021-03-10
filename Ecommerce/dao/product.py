from ..models import Product


class ProductDao:

    @staticmethod
    def get_all():
        return Product.objects.all()

    @staticmethod
    def get_lasts(number=8):

        return Product.objects.all().filter(in_stock=1).order_by('-created_at')[:number]

    @staticmethod
    def get_product(uid):

        return Product.objects.filter(uid=uid)[:1][0]
