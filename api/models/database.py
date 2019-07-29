from models.base import db
from models.comission import ComissionModel
from models.month_comission import MonthComissionModel
from models.seller import SellerModel
from models.seller_comission import SellerComissionModel


def create_db():
    from sqlalchemy import create_engine
    from configdb import SQLALCHEMY_DATABASE_URI
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    db.metadata.drop_all(engine)
    db.metadata.create_all(engine)
