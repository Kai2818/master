import asyncio
import logging

import config

db_log = logging.getLogger("MFS Database")


async def get_data(schema, table_name):
    query = f"select * from {schema}.{table_name}"
    result = {}
    try:
        # await config.database.connect()
        # print("Connect to Database")
        result = await config.database.fetch_all(query=query)
        # await config.database.disconnect()
        # print("Connection Terminated")
    except Exception as exc:
        print(exc)
    finally:
        return result


async def manual_get_data(sql):
    query = sql
    result = {}
    try:
        # await config.database.connect()
        # print("Connect to Database")
        result = await config.database.fetch_all(query=query)
        # await config.database.disconnect()
        # print("Connection Terminated")
    except Exception as exc:
        print(exc)
    finally:
        return result


async def insert_data(schema, table_name, field, values):
    query = f"insert into {schema}.{table_name} ({field}) values ({values})"
    print(query)
    {}
    try:
        # await config.database.connect()
        # print("Connect to Database")
        result = await config.database.execute(query=query)
        # await config.database.disconnect()
        db_log.info(query)
        return f"Record Inserted."
    except Exception as exc:
        db_log.error(query)
        print('result:error')
        return str(exc)


async def update_insert(update, insert):
    print(insert)
    result = {}
    try:
        # await config.database.connect()
        # print("Connect to Database")
        result = await config.database.execute(query=update)
        # await config.database.disconnect()
        db_log.info(update)
        result = await config.database.execute(query=insert)
        # await config.database.disconnect()
        db_log.info(insert)
        return f"Record Update|Insert."
    except Exception as exc:
        db_log.error(update + " " + insert)
        print('result:error')
        return str(exc)


async def update_data(schema, table_name, field, values, filt, filt_values):
    query = f"update {schema}.{table_name} set {field} = '{values}' where {filt} = '{filt_values}'"
    # print(query)
    result = {}
    try:
        # await config.database.connect()
        # print("Connect to Database")
        result = await config.database.execute(query=query)
        return "Record Updated."
        # await config.database.disconnect()
        # print("Connection Terminated")
    except Exception as exc:
        return exc


async def update_data_more(schema, table_name, field, values, filters):
    query = f"update {schema}.{table_name} set {field} = '{values}' {filters} "
    print(query)
    result = {}
    try:
        # await config.database.connect()
        # print("Connect to Database")
        result = await config.database.execute(query=query)
        return "Record Updated."
        # await config.database.disconnect()
        # print("Connection Terminated")
    except Exception as exc:
        return exc


async def manual_update(query):
    result = {}
    try:
        # await config.database.connect()
        # print("Connect to Database")
        result = await config.database.execute(query=query)
        print("updated")
        return "Record Updated."
        # await config.database.disconnect()
        # print("Connection Terminated")
    except Exception as exc:
        return exc


async def update_multidata_more(schema, table_name, updates, filters):
    query = f"update {schema}.{table_name} set {updates}  {filters} "
    print(query)
    result = {}
    try:
        # await config.database.connect()
        # print("Connect to Database")
        result = await config.database.execute(query=query)
        return "Record Updated."
        # await config.database.disconnect()
        # print("Connection Terminated")
    except Exception as exc:
        return exc


async def get_data_wparam(schema, table_name, param, col):
    query = f"select * from {schema}.{table_name} where {col} = '{param}'"
    # print(query)
    result = {}
    try:
        # await config.database.connect()
        # print("Connect to Database")
        result = await config.database.fetch_all(query=query)
        # await config.database.disconnect()
        # print("Connection Terminated")
    except Exception as exc:
        print(exc)
    finally:
        await asyncio.sleep(.5)
        return result


async def delete_data_wparam(schema, table_name, condition):
    query = f"delete from {schema}.{table_name} where {condition}"
    # print(query)
    result = {}
    try:
        # await config.database.connect()
        # print("Connect to Database")
        result = await config.database.fetch_all(query=query)
        # await config.database.disconnect()
        # print("Connection Terminated")
    except Exception as exc:
        print(exc)
    finally:
        await asyncio.sleep(.5)
        return result


async def get_data_w_Order(schema, table_name, param, col, order):
    query = f"select * from {schema}.{table_name} where {col} = '{param}' {order}"
    # print(query)
    result = {}
    try:
        # await config.database.connect()
        # print("Connect to Database")
        result = await config.database.fetch_all(query=query)
        # await config.database.disconnect()
        # print("Connection Terminated")
    except Exception as exc:
        print(exc)
    finally:
        await asyncio.sleep(.5)
        return result


async def get_data_w_2_param(schema, table_name, param_1, col_1, param_2, col_2):
    query = f"select * from {schema}.{table_name} where {col_1} = '{param_1}' and {col_2} = '{param_2}'"
    # print(query)
    result = {}
    try:
        result = await config.database.fetch_all(query=query)
    except Exception as exc:
        print(exc)
    finally:
        return result


async def get_data_w_3_param(schema, table_name, param_1, col_1, param_2, col_2, param_3, col_3):
    query = f"select * from {schema}.{table_name} where {col_1} = {param_1} and {col_2} = '{param_2}' and {col_3} = '{param_3}'"
    # print(query)
    result = {}
    try:
        result = await config.database.fetch_all(query=query)
    except Exception as exc:
        print(exc)
    finally:
        return result


async def get_data_w4_param(schema, table_name, param_1, col_1, param_2, col_2, condition):
    query = f"select * from {schema}.{table_name} where {col_1} = '{param_1}' and {col_2} = '{param_2}' and {condition}"
    # print(query)
    result = {}
    try:
        result = await config.database.fetch_all(query=query)
    except Exception as exc:
        print(exc)
    finally:
        return result


async def get_data_w_5_param(schema, table_name, param_1, col_1, condition):
    query = f"select * from {schema}.{table_name} where {col_1} = '{param_1}' and {condition}"
    print(query)
    result = {}
    try:
        result = await config.database.fetch_all(query=query)
    except Exception as exc:
        print(exc)
    finally:
        return result


async def get_data_w_6_param(schema, table_name, param_1, col_1, condition, field):
    query = f"select {field} from {schema}.{table_name} where {col_1} = '{param_1}' and {condition}"
    # print(query)
    result = {}
    try:
        result = await config.database.fetch_all(query=query)
    except Exception as exc:
        print(exc)
    finally:
        return result
