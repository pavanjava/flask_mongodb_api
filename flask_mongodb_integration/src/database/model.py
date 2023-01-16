from .db import db


class Employee(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    languages = db.ListField(required=False)
    age = db.IntField(required=True)
    sbg = db.StringField(required=True)
    email = db.StringField(required=False)
    honeywell_id = db.StringField(required=True)


class Projects(db.Document):
    project_id = db.StringField(required=True)
    project_name = db.StringField(required=True)
    project_description = db.StringField(required=False)
    project_status = db.IntField(required=True)
    sbg = db.StringField(required=True)

