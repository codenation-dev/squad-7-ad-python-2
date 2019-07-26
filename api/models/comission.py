from sqlalchemy import Column
from sqlalchemy.types import (
    Integer,
    Float
)
from sqlalchemy.orm import relationship

from models.base import db


class ComissionModel(db.Model):
    """ Comission model representation """
    __tablename__ = 'comission'

    id = Column(Integer, primary_key=True)
    min_value = Column(Float(
        precision=12,
        asdecimal=True,
        decimal_return_scale=2
    ), nullable=False)
    lower_percentage = Column(Float(
        precision=12,
        asdecimal=True,
        decimal_return_scale=2
    ), nullable=False)
    upper_percentage = Column(Float(
        precision=12,
        asdecimal=True,
        decimal_return_scale=2
    ), nullable=False)

    sellers = relationship('SellerModel',  back_populates='comission')
