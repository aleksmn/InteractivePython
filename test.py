# %%

import os

# %%
dirs = os.listdir()

for d in dirs:
    print(d)

# %%
import matplotlib.pyplot as plt
%matplotlib inline


# %%
plt.title('Title')
plt.xlabel('x')
plt.ylabel('y')

plt.scatter([0, 1, 2, 3], [2, 4, 4, 5]);


# %%
import pandas as pd

# %%

d = {'Student': ['Aleks', 'Maria', 'Sam', 'Frodo', 'Mark'],
     'Score': [56, 78, 67, 99, 18]}

df = pd.DataFrame(data=d)
df

# %%

plt.scatter(df.Student, df.Score, color='red')

plt.title('Scores')
plt.xlabel(df.Student.name)
plt.ylabel(df.Score.name);




# %%
# %%

# %%
