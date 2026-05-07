from sqlalchemy.orm import Session
from datetime import date
from app.database import SessionLocal, engine, Base
from app import models

# Create tables
Base.metadata.create_all(bind=engine)

def seed_data():
    db = SessionLocal()
    try:
        # Check if authors exist
        if db.query(models.Author).count() > 0:
            print("Database already has data. Skipping seed.")
            return

        # Add Authors
        author1 = models.Author(name="J.K. Rowling", bio="English author, best known for the Harry Potter series.")
        author2 = models.Author(name="George R.R. Martin", bio="American novelist and short story writer in the fantasy, horror, and science fiction genres.")
        db.add_all([author1, author2])
        db.commit()

        # Add Books
        book1 = models.Book(
            title="Harry Potter and the Sorcerer's Stone", 
            isbn="9780590353427", 
            author_id=author1.id,
            description="The first novel in the Harry Potter series."
        )
        book2 = models.Book(
            title="A Game of Thrones", 
            isbn="9780553103540", 
            author_id=author2.id,
            description="The first novel in A Song of Ice and Fire."
        )
        db.add_all([book1, book2])
        db.commit()

        # Add Members
        member1 = models.Member(
            fullname="John Doe", 
            email="john@example.com", 
            membership_date=date(2025, 1, 1)
        )
        db.add(member1)
        db.commit()

        print("Successfully seeded initial data!")

    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
