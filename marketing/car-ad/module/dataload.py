import pymysql
import pandas as pd

'''
database connection module
'''
def login():
    mydb = pymysql.connect(
        user='root',
        passwd='-',
        host='-',
        db='-',
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
