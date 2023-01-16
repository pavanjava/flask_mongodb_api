from .projects import ProjectOperations


def project_routes(api):
    api.add_resource(ProjectOperations, "/api/v1/project")
