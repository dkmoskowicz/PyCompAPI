from flask import Flask
from flask_restful import Resource, Api
from api.os.platform import Platform
# from api.os.platform import Platform as plat

debug = True
app = Flask(__name__)
api = Api(app)

class available_api(Resource):
    def get(self):
        key = 'available_api'
        return {key: ["/"+i for i in list(api.endpoints) if i != key]}


api.add_resource(Platform, '/platform')
#should be last api set
api.add_resource(available_api, '/')

if debug == True:
    print("end points:\n", api.endpoints, "\n")

if __name__ == '__main__':
    app.run(debug=debug)

