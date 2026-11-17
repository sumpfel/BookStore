from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime
from database import engine

class DBBook(engine.Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    isbn = Column(String, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    publisher = Column(String, index=True)
    publishedYear = Column(Date, index=True)
    isAvailable = Column(Boolean, index=True)

class DBLoan(engine.Base):
    __tablename__ = "loan"
    id = Column(Integer, primary_key=True)
    bookId = Column(Integer, index=True)
    userId = Column(Integer, index=True)
    borrowedAt = Column(DateTime, index=True)
    dueDate = Column(DateTime, index=True)
    returnedAt = Column(DateTime, index=True)
    status = Column(String, index=True)