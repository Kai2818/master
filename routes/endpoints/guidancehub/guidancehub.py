from fastapi import APIRouter, Request, Response, Depends
import requests
from Model.Dao import dao_impl
from Model import  serviceModel, user
import json
from datetime import datetime
import logging
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, HttpUrl, AnyHttpUrl
from typing import Optional
import Class.dictToJson as myEncoder
import math
from starlette.config import Config
from Class import generateUrl
from Model.guidanceHubModel.guidancehubModel import guidancehubModel



# Declare Your API Tagging
guidancehub_api = APIRouter()

# Declare Your Token Validation
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Declare Your Information Logger
info_logger = logging.getLogger('info_logger')

#Shows the Input Datas
@guidancehub_api.get("/Display_Users", tags=["Guidance HUB"])
async def Transactions():
    query_result = await dao_impl.manual_get_data(f"SELECT * FROM  guidancehub")
    return query_result

@guidancehub_api.post("/insert_Users", tags=["Guidance HUB"])
async def insert_Users(req: guidancehubModel ):
    id_exists_query = f"SELECT id FROM public.guidancehub WHERE id = '{req.id}'"
    id_exists_result = await dao_impl.manual_get_data(id_exists_query)

    if id_exists_result:
        new_id_query = "SELECT MAX(id) FROM public.guidancehub"
        max_id_result = await dao_impl.manual_get_data(new_id_query)
        max_id = max_id_result[0]["max"]
        new_id = max_id + 1 if max_id is not None else 1
        req.id = new_id

    insert_query = f"INSERT INTO public.guidancehub(id, id_number, department, firstname, middlename, lastname, gmail, password, create_at) VALUES ( '{req.id}', '{req.idNumber}', '{req.department}', '{req.firstName}', '{req.middleName}', '{req.lastName}', '{req.gmail}', '{req.password}', NOW());"
    query_result = await dao_impl.manual_get_data(insert_query)
    return query_result

@guidancehub_api.put("/update_Users", tags=["Guidance HUB"])
async def update_Users(req: guidancehubModel):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    existing_idNumber = f"SELECT id FROM public.guidancehub WHERE id_number = '{req.idNumber}' AND id != '{req.id}'"
    existing_idNumber_result = await dao_impl.manual_get_data(existing_idNumber)

    if existing_idNumber_result:
        return {"message": "ID Number already exists. No update performed."}

    sql = f"UPDATE public.guidancehub SET id_number='{req.idNumber}', department='{req.department}', firstname='{req.firstName}', middlename='{req.middleName}', lastname='{req.lastName}', gmail='{req.gmail}', password='{req.password}', updated_at= NOW() WHERE id = {req.id};"
    query_result = await dao_impl.manual_get_data(sql)
    return query_result

@guidancehub_api.delete("/delete_User", tags=["Transaction"])
async def delete_User(req: guidancehubModel):
    sql = f"DELETE FROM public.guidancehub WHERE id = '{req.id}';"
    query_result = await dao_impl.manual_get_data(sql)
    return query_result
