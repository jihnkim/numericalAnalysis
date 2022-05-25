import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# pd.read_csv()로 csv파일 읽어들이기
df = pd.read_csv('high_diamond_ranked_10min.csv')

sns.jointplot(x='blueKills', y='blueGoldDiff', data=df, hue='blueWins')

# 전처리 과정
from sklearn.preprocessing import StandardScaler

df.drop(['gameId', 'redFirstBlood', 'redKills', 'redDeaths',
       'redTotalGold', 'redTotalExperience', 'redGoldDiff',
       'redExperienceDiff'], axis=1, inplace=True)

X_num = df[['blueWardsPlaced', 'blueWardsDestroyed', 
       'blueKills', 'blueDeaths', 'blueAssists', 'blueEliteMonsters',
       'blueTowersDestroyed', 'blueTotalGold',
       'blueAvgLevel', 'blueTotalExperience', 'blueTotalMinionsKilled',
       'blueTotalJungleMinionsKilled', 'blueGoldDiff', 'blueExperienceDiff',
       'blueCSPerMin', 'blueGoldPerMin', 'redWardsPlaced', 'redWardsDestroyed',
       'redAssists', 'redEliteMonsters', 'redTowersDestroyed', 'redAvgLevel', 'redTotalMinionsKilled',
       'redTotalJungleMinionsKilled', 'redCSPerMin', 'redGoldPerMin']]
X_cat = df[['blueFirstBlood', 'blueDragons', 'blueHeralds', 'redDragons', 'redHeralds']]

scaler=StandardScaler()
scaler.fit(X_num)
X_scaled=scaler.transform(X_num)


# 스케일링 된 입력변수 확인
X_scaled=pd.DataFrame(X_scaled,index=X_num.index,columns=X_num.columns)

X=pd.concat([X_scaled,X_cat],axis=1)
y=df['blueWins']

print(X)