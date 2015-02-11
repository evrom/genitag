import random
from libraries.template import view


@view('about.html')
def about():
    photo_number = random.randint(1, 9)
    return dict(photo_number=photo_number)
