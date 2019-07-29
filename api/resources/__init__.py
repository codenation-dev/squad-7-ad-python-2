from flask_restful import Resource, Api, reqparse, fields, marshal_with
from models.database import (
    db,
    ComissionModel,
    MonthComissionModel,
    SellerModel,
    SellerComissionModel
)


comission_fields_post = {
    'id': fields.Integer
}

comission_fields_get = {
    'id': fields.Integer,
    'min_value': fields.Price(decimals=2),
    'lower_percentage': fields.Float(),
    'upper_percentage': fields.Float()
}

parser_comission = reqparse.RequestParser(bundle_errors=True)

parser_comission.add_argument(
    'min_value', type=float,
    required=True, help='min_value is required')

parser_comission.add_argument(
    'lower_percentage', type=float,
    required=True,
    help='lower_percentage is required')

parser_comission.add_argument(
    'upper_percentage',
    type=float,
    required=True,
    help='upper_percentage is required')


class Comission(Resource):

    @marshal_with(comission_fields_post)
    def post(self):
        args = parser_comission.parse_args()
        print(args)
        comission = ComissionModel(
            min_value=args['min_value'],
            lower_percentage=args['lower_percentage'],
            upper_percentage=args['upper_percentage']
        )
        print(comission.min_value)
        db.session.add(comission)
        db.session.commit()
        return comission

    @marshal_with(comission_fields_get)
    def get(self):
        comissions = ComissionModel().query.all()
        return comissions


month_comission_fields = {
    'id': fields.Integer,
    'comission': fields.Price(decimals=2)
}

parser_month_comission = reqparse.RequestParser(bundle_errors=True)

parser_month_comission.add_argument(
    'seller', type=int,
    required=True, help='seller is required')

parser_month_comission.add_argument(
    'amount', type=float,
    required=True,
    help='amount is required')

parser_month_comission.add_argument(
    'month',
    type=int,
    required=True,
    help='month is required')


class MonthComission(Resource):

    @marshal_with(month_comission_fields)
    def post(self):
        def calc_comission(value, percent):
            return (value / 100) * float(percent)

        args = parser_month_comission.parse_args()
        print(args)
        month_comission = MonthComissionModel(
            seller=args['seller'],
            amount=args['amount'],
            month=args['month']
        )
        seller = SellerModel.query.filter_by(id=month_comission.seller).first()
        comission_of_seller = None
        if month_comission.amount >= seller.comission.min_value:
            comission_of_seller = calc_comission(
                month_comission.amount, seller.comission.upper_percentage)
        else:
            comission_of_seller = calc_comission(
                month_comission.amount, seller.comission.lower_percentage)

        seller_commision = SellerComissionModel(
            seller=seller.id, comission_value=comission_of_seller)
        db.session.add(month_comission)
        db.session.add(seller_commision)
        db.session.commit()
        return {'id': month_comission.id, 'comission': comission_of_seller}

    @marshal_with(month_comission_fields)
    def get(self):
        comissions = ComissionModel().query.all()
        return comissions


seller_comission_fields = {
    'id': fields.Integer,
    'seller': fields.Integer,
    'comission_value': fields.Price(decimals=2),
    'date': fields.String
}


class SellerComission(Resource):

    # @marshal_with(comission_fields)
    # def post(self):
    #     args = parser_comission.parse_args()
    #     print(args)
    #     comission = ComissionModel(
    #         min_value=args['min_value'],
    #         lower_percentage=args['lower_percentage'],
    #         upper_percentage=args['upper_percentage']
    #     )
    #     print(comission.min_value)
    #     db.session.add(comission)
    #     db.session.commit()
    #     return comission

    @marshal_with(seller_comission_fields)
    def get(self):
        comissions = SellerComissionModel().query.all()
        return comissions


seller_fields_post = {
    'id': fields.Integer
}

seller_fields_get = {
    'id': fields.Integer,
    'name': fields.String,
    'address': fields.String,
    'phone': fields.String,
    'age': fields.Integer,
    'email': fields.String,
    'cpf': fields.String,
    'comission_plan': fields.Integer
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
    'comission_plan',
    type=int,
    required=True,
    help='comission plan is required')


class Seller(Resource):

    @marshal_with(seller_fields_post)
    def post(self):
        args = parser_seller.parse_args()
        seller = SellerModel(
            name=args['name'],
            address=args['address'],
            phone=args['phone'],
            age=args['age'],
            email=args['email'],
            cpf=args['cpf'],
            comission_plan=args['comission_plan']
        )
        db.session.add(seller)
        db.session.commit()
        return seller

    @marshal_with(seller_fields_get)
    def get(self):
        sellers = SellerModel().query.all()
        return sellers


def set_resources_in_app(app):
    api = Api(app)

    api.add_resource(Seller, '/sellers')
    api.add_resource(Comission, '/comissions')
    api.add_resource(MonthComission, '/month_comission')
    api.add_resource(SellerComission, '/seller_comission')
