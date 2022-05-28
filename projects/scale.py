import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# pd.read_csv()로 csv파일 읽어들이기
df = pd.read_csv('high_diamond_ranked_10min.csv')

# sns.jointplot(x='blueKills', y='blueGoldDiff', data=df, hue='blueWins')

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

# 학습/테스트 데이터 분리
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=1)

# 분류모델 생성
from sklearn.linear_model import LogisticRegression

model_lr = LogisticRegression(random_state=1,max_iter=100)
model_lr.fit(X_train,y_train)

# 모델 학습 평가
from sklearn.metrics import classification_report

pred =model_lr.predict(X_test)
print(classification_report(y_test,pred))

# 회귀 계수로 상관성 파악
model_coef = pd.DataFrame(data=model_lr.coef_[0], index=X.columns, columns=['Model Coefficient'])

model_coef.sort_values(by='Model Coefficient', ascending=False, inplace=True)

# 중요한 feature 확인
# Logistic Regression 모델의 coef_ 속성을 plot하기
plt.bar(model_coef.index, model_coef['Model Coefficient'])
plt.xticks(rotation=90)
plt.grid()
plt.show()