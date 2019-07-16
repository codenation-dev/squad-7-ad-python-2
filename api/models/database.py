from models.base import db
from models.commission import CommissionModel
from models.month_commission import MonthCommissionModel
from models.seller import SellerModel

def create_db():
    from sqlalchemy import create_engine
    from configdb import SQLALCHEMY_DATABASE_URI
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    db.metadata.drop_all(engine)
    db.metadata.create_all(engine)