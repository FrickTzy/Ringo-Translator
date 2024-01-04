class Options:
    def __init__(self, use_api: bool):
        self.__use_api = use_api

    @property
    def using_api(self):
        return self.__use_api

    def use_api(self):
        self.__use_api = True

    def un_use_api(self):
        self.__use_api = False