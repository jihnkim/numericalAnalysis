import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('interpolation/bicycle.csv', encoding='cp949')

# print(df.head())

plt.plot(df['대여일시'], df['이용시간'])
plt.show()