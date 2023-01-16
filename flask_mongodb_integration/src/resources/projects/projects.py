from flask import Response, request, jsonify
from src.database.model import Projects
from flask_restful import Resource


class ProjectOperations(Resource):

    def get(self):
        projects = Projects.objects().to_json()
        if not projects:
            return jsonify({'error': 'data not found'})
        else:
            return Response(projects, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        project = Projects(**body).save()
        return {"id": str(project.id)}, 201
