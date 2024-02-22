"""Позволяет добавлять дополнительные данные в контекст, доступный в шаблонах Django"""
from .models import Category


def get_categories_from_shop(request):
    """Эта функция добавляется в контекст и становится доступной во всех шаблонах,
    используемых в представлении shop(), под именем categories.
    Таким образом, в каждом шаблоне можно использовать эту переменную без необходимости
    повторного получения данных из базы данных."""
    categories = Category.objects.all()
    return {'categories': categories}
