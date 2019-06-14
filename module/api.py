import main


class API(main):
    def __init__(self, _class, api):
        main.add_resource(_class, api)
