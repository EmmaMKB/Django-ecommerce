from ..models import Category


class CategoryDao:

    def __init__(self):
        pass

    @staticmethod
    def get_all():

        return Category.objects.all().order_by('name')
