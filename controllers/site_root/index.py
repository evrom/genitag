import random
from libraries.template import view
from libraries.forms import Login as Form


@view('index.html')
def index():
    form = Form()
    photo_number = random.randint(1, 11)
    return dict(form=form, photo_number=photo_number)
