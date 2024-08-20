from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DBTransaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_date = Column(Date, nullable=False)
    settlement_date = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    transaction = Column(Float, nullable=False)
    balance = Column(Float, nullable=False)
    is_debit = Column(Boolean, nullable=False)
