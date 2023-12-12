from flask import Flask, request
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

class Emoji(Resource):
    def get(self, name, category, group, htmlCode, unicode):
        url = f"https://emojihub.yurace.pro/api/all"
        response = requests.get(url)
        data = response.json()
        return {'data': data}, 200

api.add_resource(Emoji, "/emoji/<string:name>/<string:category>/<string:group>/<string:htmlCode>/<string:unicode>")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6767)
