"""
# CREATE RECORD
new_book = Book(title="s", author="45", rating=3.3)
db.session.add(new_book)
db.session.commit()

# Read All Records
    with app.app_context():
        all_books = db.session.execute(db.select(Book)).scalars()
        # or all_books = db.session.query(Book).all()
        # or all_books = Book.query.all()    

# Read A Particular Record By Query
    with app.app_context():
        book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
        # or book = db.session.query(Book).filter_by(title="Harry Potter").first()
        # or book = Book.query.filter_by(title="Harry Potter").first()

# Update A Particular Record By Query
    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
        book_to_update.title = "Harry Potter and the Chamber of Secrets"
        db.session.commit() 

# Update A Record By PRIMARY KEY
    book_id = 1
    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_update = db.session.get(Book, book_id)  
        # Note Book.query.get() is deprecated
        book_to_update.title = "Harry Potter and the Goblet of Fire"
        db.session.commit()  



# Delete A Particular Record By PRIMARY KEY
    book_id = 1
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()

"""