from flask.ext.restful import Resource, fields, marshal, reqparse
from flask.ext.security import current_user
from server import db
from server.models.application import Application


company_fields = {
    'id': fields.Integer,
    'name': fields.String
}

user_fields = {
    'id': fields.Integer,
    'email': fields.String
}

application_fields = {
    'id': fields.Integer,
    'company': fields.Nested(company_fields),
    'user': fields.Nested(user_fields)
}


class ApplicationsResource(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('company_id', location='json')
        super().__init__()


class ApplicationsAPI(ApplicationsResource):
    def get(self):
        user_id = current_user.id
        applications = Application.query.filter_by(user_id=user_id).all()
        return {'applications': [marshal(application, application_fields) for application in applications]}

    def post(self):
        args = self.reqparse.parse_args()
        args['user_id'] = current_user.id
        application = Application(args)
        db.session.add(application)
        db.session.commit()
        return 'Application Opened!', 201
