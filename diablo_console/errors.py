__all__ = ['GeneralDiabloConsoleError', 'ViewError']


class GeneralDiabloConsoleError(Exception):
    def __init__(self, message):
        print ('ERROR: {}'.format(message))


class ViewError(GeneralDiabloConsoleError):
    pass
