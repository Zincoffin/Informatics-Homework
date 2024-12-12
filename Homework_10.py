
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#1

help = pd.Series([4.313, 4.338, 4.358, 4.378, 4.4, 4.425, 4.447, 4.468])
print(help)
helpmore = pd.Series(np.arange(0, 20, 2))
print(helpmore)
helpevenmore = pd.Series({'Семейство': 1, 'Шмуклеров': 3, 'производило': 5, 'гвозди': 7})
print(helpevenmore)'

#2

please = pd.Series(np.arange(0, 8, 2))
suffer = pd.Series(np.arange(2, 10, 1))
print(please, suffer)
wow = set.union(set(please), set(suffer))
wown = pd.Series(list(wow))
print(wown)

#3


fm = pd.Series({0: 'female',1: 'male',2: 'male',3: 'female',4: 'female',5: 'male',
  6: 'male',7: 'male',8: 'male',9: 'female',10: 'female',11: 'female',12: 'female',
  13: 'female',14: 'male',15: 'male',16: 'male',17: 'male',18: 'male',19: 'female',
  20: 'female',21: 'female',22: 'male',23: 'male',24: 'male',25: 'male',26: 'female',
  27: 'female',28: 'male',29: 'female',30: 'male',31: 'female',32: 'female',
  33: 'male',34: 'female'})

x = fm.value_counts().index
y = fm.value_counts().values
plt.bar(x, y, color=['pink', 'cyan'])
plt.xlabel('количество учеников')  # для оси x
plt.ylabel('пол учеников')  # для оси y
plt.title('соотношение студентов')
plt.show()