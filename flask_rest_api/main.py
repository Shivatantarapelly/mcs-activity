from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {'shiva': {'age': 25, 'gender': 'male'},
         'prasad': {'age': 70, 'gender': 'male'}}


class Demo(Resource):
    def get(self, name):
        return names[name]


api.add_resource(Demo, '/demo/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
