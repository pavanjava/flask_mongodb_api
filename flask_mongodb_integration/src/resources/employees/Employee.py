from flask import Response, request, jsonify
from src.database.model import Employee
from flask_restful import Resource


class EmployeeOperations(Resource):

    def get(self):
        user = Employee.objects().to_json()
        if not user:
            return jsonify({'error': 'data not found'})
        else:
            return Response(user, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        employee = Employee(**body).save()
        return {"id": str(employee.id)}, 201
