from sqlalchemy import (
    Integer,
    Numeric,
    Column
)

from models.base import db
from models.basic_controller import BasicController


class MonthCommissionModel(db.Model, BasicController):
    """ MonthCommission model representation """
    __tablename__ = 'monthcommission'

    id = Column(Integer, primary_key=True)
    seller = Column(Integer, nullable=False)
    amount = Column(Numeric, nullable=False)
    month = Column(Integer, nullable=False)
