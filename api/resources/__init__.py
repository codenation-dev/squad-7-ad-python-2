from flask_restful import Resource, Api, reqparse, fields, marshal_with
from models.database import db, CommissionModel, MonthCommissionModel, SellerModel


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


commission_fields = {
    'min_value': fields.Float(),
    'lower_percentage': fields.Float(),
    'upper_percentage': fields.Float()
}

parser_commission = reqparse.RequestParser(bundle_errors=True)

parser_commission.add_argument(
    'min_value', type=float,
    required=True, help='min_value is required')

parser_commission.add_argument(
    'lower_percentage', type=float,
    required=True,
    help='lower_percentage is required')

parser_commission.add_argument(
    'upper_percentage',
    type=float,
    required=True,
    help='upper_percentage is required')


seller_fields = {
    'name': fields.String,
    'address': fields.String,
    'phone': fields.String,
    'age': fields.Integer,
    'email': fields.String,
    'cpf': fields.String,
    'commission_plan': fields.Integer
}

parser_seller = reqparse.RequestParser(bundle_errors=True)

parser_seller.add_argument(
    'name', type=str,
    required=True, help='name is required')

parser_seller.add_argument(
    'address', type=str,
    required=True,
    help='address is required')

parser_seller.add_argument(
    'phone',
    type=str,
    required=True,
    help='phone is required')

parser_seller.add_argument(
    'age',
    type=int,
    required=True,
    help='age is required')

parser_seller.add_argument(
    'email',
    type=str,
    required=True,
    help='email is required')

parser_seller.add_argument(
    'cpf',
    type=str,
    required=True,
    help='cpf is required')

parser_seller.add_argument(
    'commission_plan',
    type=int,
    required=True,
    help='commission plan is required')


class Commission(Resource):

    @marshal_with(commission_fields)
    def post(self):
        args = parser_commission.parse_args()
        print(args)
        commission = CommissionModel(
            min_value=args['min_value'],
            lower_percentage=args['lower_percentage'],
            upper_percentage=args['upper_percentage']
        )
        print(commission)
        db.session.add(commission)
        db.session.commit()
        return commission

    @marshal_with(commission_fields)
    def get(self):
        commissions = CommissionModel().query.all()
        return commissions


class Seller(Resource):

    @marshal_with(seller_fields)
    def post(self):
        args = parser_seller.parse_args()
        seller = SellerModel(
            name=args['name'],
            address=args['address'],
            phone=args['phone'],
            age=args['age'],
            email=args['email'],
            cpf=args['cpf'],
            commission_plan=args['commission_plan']
        )
        db.session.add(seller)
        db.session.commit()
        return seller

    @marshal_with(seller_fields)
    def get(self):
        sellers = SellerModel().query.all()
        return sellers


def set_resources_in_app(app):
    api = Api(app)

    api.add_resource(Seller, '/sellers')
    api.add_resource(Commission, '/commissions')
