import dataload
import query

# get data from database 
qry1 = query.get_table("TV_daily")
TV_daily = dataload.getdata(qry1)

qry2 = query.get_table("naver_query")
naver_query = dataload.getdata(qry2)

qry3 = query.get_table("kaida")
kaida = dataload.getdata(qry3)