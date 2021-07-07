from module import dataload
from module import query
from module import df_calc

import pandas as pd
import matplotlib.pylab as plt
from datetime import datetime
import numpy as np

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
plt.plot(honda.index, honda["value"], label="honda", marker='h')
plt.axvline(x=datetime(2019, 9, 1), color='b', linestyle='--', linewidth=2)
plt.axvline(x=datetime(2019, 12, 1), color='r', linestyle='--', linewidth=2)

plt.legend()
plt.savefig("./graph/toyota-honda.png")
plt.show()

# 19년도 9월 부터 실질적인 반일 감정 발생
# 12월달 부터 불매 운동으로 인한 실질적인 파동이 시작 ..
# 신문 기사 인용
# https://www.hankookilbo.com/News/Read/202001061185366881
'''
한일간의 갈등이 있던 이전에도 일본차의 판매는 큰 영향은 없었다”
'''
# 그 동안 한일 갈등에 크게 상관이 없던 일본차가 이번에는 왜 이렇게 급변했을까

'''
16년 7월 일본해 표기, 촛불집회 비하
18년 12월 전범기업 이슈
'''
plt.figure(figsize=(18,10))
plt.title('anti-japan')
plt.plot(toyota.index, toyota["value"], label="toyota", marker='h')
plt.plot(honda.index, honda["value"], label="honda", marker='h')
plt.axvline(x=datetime(2016, 11, 1), color='b', linestyle='--', linewidth=2)
plt.axvline(x=datetime(2018, 12, 1), color='b', linestyle='--', linewidth=2)
plt.axvline(x=datetime(2019, 9, 1), color='b', linestyle='--', linewidth=2)
plt.axvline(x=datetime(2019, 12, 1), color='r', linestyle='--', linewidth=2)
plt.legend()
plt.savefig("./graph/anti-japan.png")
plt.show()

# for see advertisement change 
# sub val between last month and this month 
# extract top5 increase month and decreasement month 
toyota_day = df_calc.monthly_sub(toyota)
honda_day = df_calc.monthly_sub(honda)

#bad day of toyota and honda 
toyota_day_bad = toyota_day[5:]
honda_day_bad = honda_day[5:]
# axvline the 10 up and down days in graph
plt.figure(figsize=(18,10))
plt.title('anti-japan-after')
plt.plot(toyota.index, toyota["value"], label="toyota", marker='h')
plt.plot(honda.index, honda["value"], label="honda", marker='h')

for i in range(len(toyota_day_bad.index)):
    plt.axvline(x=toyota_day_bad.index[i], color='g', linestyle='-', linewidth=3)

for i in range(len(honda_day_bad.index)):
    plt.axvline(x=honda_day_bad.index[i], color='k', linestyle='--', linewidth=3)
    
plt.axvline(x=datetime(2016, 11, 1), color='b', linestyle='--', linewidth=4)
plt.axvline(x=datetime(2016, 11, 1), color='b', linestyle='--', linewidth=4)
plt.axvline(x=datetime(2018, 12, 1), color='b', linestyle='--', linewidth=4)
plt.axvline(x=datetime(2019, 9, 1), color='b', linestyle='--', linewidth=4)
plt.axvline(x=datetime(2019, 12, 1), color='r', linestyle='--', linewidth=2)
plt.legend()
plt.savefig("./graph/anti-japan_after.png")
plt.show()

''' 
유의미하다고 느껴지는것은 반일 정서가 생겼을때.. 즉각적으로 자동차 등록댓수가 줄어 들었다.
'''

# 이번 일본차 eda 결과
'''
기존 일본차에 대한 인식은 충성도 있는 고객이 많아서 
대중들의 감정과 크게 상관 없이 판매되는 양은 일정하다고 여겨졌는데

실제로 데이터를 분석을 해본결과
한국의 일본 차 등록 대수는 파장이 도달하는 시간이 조금씩 차이가 날뿐
반일 감정과 상당히 연관성이 있다고 판단이 됩니다.
또한 이러한 감정으로 인한 판매량 감소는 회복까지 오랜 시간이 걸립니다.

여러 매체나 sns를 미리 실시간으로 정보를 수집하면서, 만약 이러한 정서를 판단을 할 수 있다면,
광고 전략 및 판매 전략에 상당히 도움이 될 것으로 사료됩니다.
'''