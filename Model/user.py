from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic.datetime_parse import date
from sqlalchemy.sql.functions import now


class User(BaseModel):
    id: Optional[int] = 0
    username: Optional[str] = "memel"
    firstName: Optional[str] = "Rommel"
    lastName: Optional[str] = "Lagurin"
    createdDate: Optional[datetime] = datetime.now()
    isEnabled: Optional[bool] = True


