
from django.conf import settings 
from random import choice
from string import ascii_letters, digits

SIZE=getattr(settings, 'MAXIMUM_URL_CHARS', 7)

CHARS = ascii_letters + digits

def create_random_code():
    return ''.join(choice(CHARS) for _ in range(SIZE))

def create_shortened_url(instance):
    new_code = create_random_code()
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(short=new_code).exists()
    if qs_exists:
        return create_shortened_url(instance)
    return new_code

