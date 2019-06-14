import importlib

from flask import Flask
from flask_restful import Resource, Api
from util import files

debug = True
app = Flask(__name__)
api = Api(app)


class Available_Api(Resource):
    def get(self):
        key = 'available_api'
        return {key: ["/" + i for i in list(api.endpoints) if i != key]}


# set api's dynamically
modules = files.Files("api").modules
for file in list(modules):
    for module in modules[file]:
        api.add_resource(getattr(importlib.import_module(file), module), "/" + str(module).lower())

# should be last api set
api.add_resource(Available_Api, '/')

if debug:
    print("end points:\n", api.endpoints, "\n")

if __name__ == '__main__':
    app.run(debug=debug)
