import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# pd.read_csv()로 csv파일 읽어들이기
df = pd.read_csv('high_diamond_ranked_10min.csv')

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

# 종속 변수와 합쳐보자
new_df = pd.concat([X, y], axis=1)
print(new_df)

# 상관관계 히트맵
plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),annot=False,linewidths=.5)
plt.show()

# 클러스터맵
sns.clustermap(df.corr(),
               annot = True,
               cmap = 'RdYlBu_r',
               vmin = -1, vmax = 1,)
plt.show()
plt.savefig('clustermap.pdf')

# 마스킹 히트맵
fig,ax = plt.subplots(figsize=(20,20))
mask = np.zeros_like(df.corr(), dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(df.corr(),
            annot = True,
            mask = mask,
            cmap = 'RdYlBu_r',
            linewidths = .5,
            cbar_kws={"shrink": .5},
            vmin = -1, vmax = 1)
plt.show()
plt.savefig("heatmap2.pdf", width = 7, height = 14, onefile = False)