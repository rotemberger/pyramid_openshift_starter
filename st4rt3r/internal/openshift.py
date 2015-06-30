__author__ = 'rotem'
import os


class EnvironException(Exception):
    pass


class Environ:
    def __init__(self, settings):
        self.settings = settings

    def get(self, environ_key):
        if environ_key in os.environ:
            return os.environ[environ_key]
        else:
            develop_key = 'openshift.{0}'.format(environ_key)
            if develop_key in self.settings:
                return self.settings[develop_key]
        raise EnvironException('Missing environ key: {0}'.format(environ_key))
