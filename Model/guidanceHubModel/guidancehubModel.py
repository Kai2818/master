from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic.datetime_parse import date
from sqlalchemy.sql.functions import now

class guidancehubModel(BaseModel):
    id : Optional[int]
    idNumber : Optional[str]
    department : Optional[str]
    firstName : Optional[str]
    middleName : Optional[str]
    lastName : Optional[str]
    gmail : Optional[str]
    password : Optional[str]
    createdAt : Optional[datetime] = datetime.now()
    updatedAt : Optional[datetime] = datetime.now()

