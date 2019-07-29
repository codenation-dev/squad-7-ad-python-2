from sqlalchemy import (
    ForeignKey,
    String,
    Integer,
    Column
)
from sqlalchemy.orm import relationship, backref

from models.base import db
from models.basic_controller import BasicController


class SellerModel(db.Model, BasicController):
    """ Seller model representation """
    __tablename__ = 'seller'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    address = Column(String(200), nullable=False)
    phone = Column(String(11), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(100), nullable=False)
    cpf = Column(String(11), nullable=False)
    comission_plan = Column(Integer, ForeignKey(
        'comission.id'), nullable=False)

    comission = relationship(
        'ComissionModel',
        backref=backref('seller', uselist=False)
    )
