from app.db.setup import SessionLocal


def insert_transaction(new_transaction):
    # Create a new session
    session = SessionLocal()

    try:
        # Create a new transaction instance


        # Add the new transaction to the session
        session.add(new_transaction)

        # Commit the transaction to the database
        session.commit()

        print("Record inserted successfully!")
    except Exception as e:
        # Rollback in case of error
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        # Close the session
        session.close()
