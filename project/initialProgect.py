import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.style.use('ggplot')
import seaborn as sns

t = pd.Series([1, 2, 3, 4])
print(t)

t.index = ['Stockholm', 'London', 'Rome', 'Paris']
t.name = 'Population'
print(t)

fig, axes = plt.subplots(1, 4, figsize=(12, 3.5))

t.plot(ax=axes[0], kind='line', title="line")
t.plot(ax=axes[1], kind='bar', title="bar")
t.plot(ax=axes[2], kind='box', title="box")
t.plot(ax=axes[3], kind='pie', title="pie")

fig.tight_layout()
fig.savefig("ch12-series-plot.pdf")
fig.savefig("ch12-series-plot.png")