from sqlalchemy import Column, func
from sqlalchemy.types import (
    Integer,
    Float,
    Date
)

from models.base import db
from models.basic_controller import BasicController


class SellerComissionModel(db.Model, BasicController):
    """ SellerComission model representation """
    __tablename__ = 'sellercomission'

    id = Column(Integer, primary_key=True)
    seller = Column(Integer, nullable=False)
    comission_value = Column(Float(
        precision=12,
        asdecimal=True,
        decimal_return_scale=2
    ), nullable=False)
    date = Column(Date, nullable=False, default=func.now())
