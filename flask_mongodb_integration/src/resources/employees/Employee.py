from flask import Response, request, jsonify
from src.database.model import Employee
from flask_restful import Resource
from flask_restful_swagger import swagger


class EmployeeOperations(Resource):

    @swagger.operation(
        responseClass=[Employee.__name__],
        nickname='employee',
        responseMessages=[
            {
                "code": 200,
                "message": "successfully retrieved data"
            },
            {
                "code": 400,
                "message": "bad request"
            },
            {
                "code": 404,
                "message": "no data found"
            }
        ]
    )
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
