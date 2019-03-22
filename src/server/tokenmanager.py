import random

def init():
    _tokenManager = _TokenManager()

def compare(token):
    return _tokenManager.compareToken(token)

class _TokenManager(object):
    def __init__(self):
        self.token = self._getToken()

    def compareToken(self, token):
        if token == self._getToken():
            return True
        return False

    def _getToken(self):
        self._resetToken()
    
    def _resetToken(self):
        pass