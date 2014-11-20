# status = {'success': False,
#          'info': False, 'warning': False, 'danger': False}


class Status(object):
    __slots__ = ['success', 'info', 'warning', 'danger']

    def __init__(self, success=False, info=False, warning=False, danger=False):
        self.success = success
        self.info = info
        self.warning = warning
        self.danger = danger
