from .Employee import EmployeeOperations


def employee_routes(api):
    api.add_resource(EmployeeOperations, "/api/v1/employee")
