import pymssql
import pandas as pd

def puket_conn():

    server='187.0.145.98'
    port=1433
    user='plmexpress'
    password='Wrk2@21%!'
    database='HDB_Puket_Custo'

    print(database)

    dbconn = pymssql.connect(server=server, user=user, password=password, database=database, port=port)

    return dbconn


def lambda_handler(event, content):

    query = """
    SELECT
    M.MATERIAL 'integration_id'
    WHERE M.GRUPO='TECIDO'
    """

    print('reading database')
    material_db = pd.read_sql_query(query,conn=puket_conn())

    print(f'len_result : {len(material_db)}')

    return f'len_result : {len(material_db)}'


