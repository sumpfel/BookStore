from fastapi import APIRouter
from fastapi.params import Depends
from fastapi_restful.cbv import cbv
from pydantic import BaseModel, field_validator, ValidationError, Field
from sqlalchemy.orm import Session

from database import models
from database.engine import get_db
from .base import BaseAPI

router = APIRouter(prefix="/loan", tags=["loan"])

class LoanCreate(BaseModel):
    name:str
    price:int = Field(..., ge=0)
    isbn:str
    title:str
    author:str
    publisher:str
    publishedYear:str
    isAvailable:bool

class LoanResponse(LoanCreate):
    id: int

@cbv(router)
class loanAPI(BaseAPI):
    db: Session = Depends(get_db)
    #apy_key:str = Depends(verify_api_key())

    @router.get("/{loan_id}")
    def get_loan_by_id(self, loan_id:int):
        return self.get_or_404(self.db, models.DBLoan, loan_id)

    @router.get("/", response_model=list[LoanResponse])
    def get_all_loans(self):
        return self.db.query(models.DBLoan).all()

    @router.delete("/{loan_id}")
    def delete_loan(self, loan_id:int):
        return self.get_or_404(self.db, models.DBLoan, laon_id)

    @router.post("/")
    def create_loan(self, loan:LoanCreate):
        db_loan = models.DBLoan(name=loan.name, price=loan.price)
        self.db.add(db_loan)
        self.db.commit()
        self.db.refresh(db_loan)