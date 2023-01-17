from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger
from src.database.db import init_db
from src.resources.employees.routes import employee_routes
from src.resources.projects.routes import project_routes

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    'db': 'local',
    'host': 'localhost',
    'port': 27017
}

api = swagger.docs(Api(app), apiVersion='0.1')

init_db(app)
employee_routes(api)
project_routes(api)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
