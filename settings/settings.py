class BaseConfig(object):
    DEBUG = True
    TESTING = False


class DevConfig(BaseConfig):
    CONFIG = "DevConfig"
    pass


class ProductionConfig(BaseConfig):
    DEBUG = False
