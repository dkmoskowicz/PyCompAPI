from flask import request
from flask_restful import Resource
import subprocess


class Program(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        if type(json_data['process']) is str:
            json_data['process'] = [i.strip() for i in str(json_data['process']).split(" ")]
        try:
            return {"result": subprocess.check_output(json_data['process']).decode('UTF-8').rstrip(), "code": 200}
        except:
            return {"result": "Error, could not run: " + " ".join(list(json_data['process'])), "code": 200}
