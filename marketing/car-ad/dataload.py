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

