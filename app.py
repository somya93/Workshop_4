from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.RiderResource import RiderResource
from utils.JSONEncoder import MongoEngineJSONEncoder

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'REST_API',
    'host': 'mongodb://localhost:27017/REST_API'
}

initialize_db(app)
app.json_encoder = MongoEngineJSONEncoder
api = Api(app)


# http://localhost:5000/rider
# http://localhost:5000/rider/rider_id?arg=value
api.add_resource(RiderResource,
                 '/rider',
                 '/rider/',
                 '/rider/<string:rider_id>')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    app.run()  # Runs web app @ http://localhost:5000 by default for me.
