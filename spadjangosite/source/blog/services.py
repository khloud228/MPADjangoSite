from rest_framework import pagination

from django.template.defaultfilters import slugify as django_slugify

class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 6


alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}

def slugify(string:str) -> str:
    string = string.lower()
    translit_string = ''
    for letter in string:
        translit_string += ''.join(alphabet.get(letter, letter))
    return django_slugify(translit_string)
"""
print(slugify('эавыа')) # eavia
print(django_slugify('эавыа')) # пустая строка
from pytils.translit import slugify as pytils_slugify
print(pytils_slugify('эавыа')) # eavyia
"""

def prepoplated_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)
    print(instance.slug)