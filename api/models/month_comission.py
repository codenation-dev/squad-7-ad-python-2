from sqlalchemy import Column
from sqlalchemy.types import (
    Integer,
    Float
)

from models.base import db
from models.basic_controller import BasicController


class MonthComissionModel(db.Model, BasicController):
    """ MonthComission model representation """
    __tablename__ = 'monthcomission'

    id = Column(Integer, primary_key=True)
    seller = Column(Integer, nullable=False)
    amount = Column(Float(
        precision=12,
        asdecimal=True,
        decimal_return_scale=2
    ), nullable=False)
    month = Column(Integer, nullable=False)
