from fastapi import APIRouter
from fastapi.params import Depends
from fastapi_restful.cbv import cbv
from pydantic import BaseModel, field_validator, ValidationError, Field
from sqlalchemy.orm import Session

from database import models
from database.engine import get_db
from .base import BaseAPI

router = APIRouter(prefix="/books", tags=["books"])

class BookCreate(BaseModel):
    name:str
    price:int = Field(..., ge=0)
    isbn:str
    title:str
    author:str
    publisher:str
    publishedYear:str
    isAvailable:bool

class BookResponse(BookCreate):
    id: int

@cbv(router)
class booksAPI(BaseAPI):
    db: Session = Depends(get_db)
    #apy_key:str = Depends(verify_api_key())

    @router.get("/{book_id}")
    def get_book_by_id(self, book_id:int):
        return self.get_or_404(self.db, models.DBBook, book_id)

    @router.get("/", response_model=list[BookResponse])
    def get_all_books(self):
        return self.db.query(models.DBBook).all()

    @router.delete("/{book_id}")
    def delete_book(self, book_id:int):
        return self.get_or_404(self.db, models.DBBook, book_id)

    @router.post("/")
    def create_book(self, book:BookCreate):
        db_book = models.DBBook(name=book.name, price=book.price)
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)