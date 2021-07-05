import dataload
import query
import pandas as pd
import matplotlib.pylab as plt
from datetime import datetime

# # get data from database 
# qry1 = query.get_table("TV_daily")
# TV_daily = dataload.getdata(qry1)

# qry2 = query.get_table("naver_query")
# naver_query = dataload.getdata(qry2)

qry3 = query.get_table("kaida")
kaida = dataload.getdata(qry3)


# kaida datatime frame add
kaida["date"] = (kaida["year"].map(str) + "-" + kaida["month"].str.replace("월", ""))
kaida["date"] = pd.to_datetime(kaida["date"])
kaida.drop(["month", "year"], axis=1, inplace=True)

# 16-01 ~ 21-04 
kaida = kaida[kaida["date"].between("2016-01-01 ","2021-04-01")]

# I need int type in value 
kaida["value"] = kaida["value"].str.replace(",","")
kaida["value"] = kaida["value"] .astype(int)


# For toyota vs honda 
toyota_kaida = kaida[kaida["brand"] == "Toyota"]
honda_kaida = kaida[kaida["brand"] == "Honda"]

# toyota sales plot
toyota = toyota_kaida.groupby("date").sum()
honda = honda_kaida.groupby("date").sum()

plt.figure(figsize=(18,10))
plt.title('toyota vs honda')
plt.plot(toyota.index, toyota["value"], label="toyota", marker='h')
plt.plot(honda.index, honda["value"], label="honda",)
plt.axvline(x=datetime(2019, 9, 1), color='b', linestyle='--', linewidth=2)
plt.axvline(x=datetime(2019, 12, 1), color='r', linestyle='--', linewidth=2)

plt.legend()
plt.savefig("./graph/toyota-honda.png")
plt.show()
