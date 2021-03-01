from ..models import Subcategory


class SubCategoryDao:

    @staticmethod
    def get_all():

        return Subcategory.objects.all()
