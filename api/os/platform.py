from flask_restful import Resource
import sys

class Platform(Resource):
    def get(self):
        return \
        {
            'os': sys.platform,
            'version': sys.version,
        }
