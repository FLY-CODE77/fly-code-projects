import pymysql
import pandas as pd

'''
database connection module
'''
def login():
    mydb = pymysql.connect(
        user='root',
        passwd='dss',
        host='34.64.111.84',
        db='my_db',
        charset='utf8',
    )
    cursor = mydb.cursor(pymysql.cursors.DictCursor)
    return mydb, cursor

'''
data load from database
if you give qry return dataset
'''
def getdata(qry1):
    mydb, cursor = login()
    cursor.execute(qry1)
    rlt1 = cursor.fetchall()
    df_1 = pd.DataFrame(rlt1)
    return df_1