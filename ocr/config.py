
class Config:
    from os.path import abspath
    class AppEnvType:
        DEV = 'dev'
        PRODUCTION = 'production'
        TEST = 'test'

    APP_NAME = '12306-ocr'
    APP_ENV = AppEnvType.PRODUCTION
    LOADED = False

    PROJECT_DIR = abspath(__file__ + '/../') + '/'
    CONFIG_FILE = PROJECT_DIR + '../config.toml'
    IMAGE_MODEL_FILE = PROJECT_DIR + 'image.model.h5'
    TEXT_MODEL_FILE = PROJECT_DIR + 'text.model.h5'
    TEXTS_FILE = PROJECT_DIR + 'texts.txt'

    WEB = {
        'host': '0.0.0.0',
        'port': 8000
    }
    OCR = {
    }

    @classmethod
    def load(cls):
        """
        Load configs from toml file
        :return:
        """
        import toml
        configs = toml.load(cls.CONFIG_FILE)

        web = configs.get('web', {})
        cls.WEB.update(web)

        ocr = configs.get('ocr', {})
        cls.OCR.update(ocr)

if not Config.LOADED:
    Config.load()
    
listento = Config.WEB['host']+':'+str(Config.WEB['port'])
# Logger
def set_up_logger():
    import logging
    logger = logging.getLogger(Config.APP_NAME)
    logger.propagate = False
    logger.setLevel(logging.DEBUG if Config.APP_ENV == Config.AppEnvType.DEV else logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s:\n%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

Logger = set_up_logger()
