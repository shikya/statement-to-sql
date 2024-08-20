from datetime import date

from app.db.setup import engine
from app.models.transaction import Base, DBTransaction
from app.models.transaction_dao import insert_transaction


def create_tables():
    Base.metadata.create_all(bind=engine)


def main():
    create_tables()

    # You can add more logic here like inserting a record
    new_transaction = DBTransaction(
        transaction_date=date(2024, 8, 17),
        settlement_date=date(2024, 8, 18),
        description='Test Transaction',
        transaction=100.0,
        balance=500.0,
        is_debit=True
    )
    insert_transaction(new_transaction)
    print("Tables created successfully!")


if __name__ == "__main__":
    main()
