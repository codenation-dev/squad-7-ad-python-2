from sqlalchemy import (
    Integer,
    Numeric,
    Column
)

from models.base import db


class CommissionModel(db.Model):
    """ Commission model representation """
    __tablename__ = 'commission'

    id = Column(Integer, primary_key=True)
    min_value = Column(Numeric, nullable=False)
    lower_percentage = Column(Numeric, nullable=False)
    upper_percentage = Column(Numeric, nullable=False)
