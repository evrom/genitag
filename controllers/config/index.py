from libraries.template import view
from libraries.authentication import login_required
from libraries.status import Status


@view('/config/index.html')
@login_required
def index():
    status = Status()
    return dict(status=status)
