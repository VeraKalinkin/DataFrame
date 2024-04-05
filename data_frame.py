import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
#data.head()
#print(data)

robot_lst = []
human_lst = []
for c in lst:
    if c == 'human':
        human_lst.append(1)
        robot_lst.append(0)
    else:
        human_lst.append(0)
        robot_lst.append(1)
new_data = pd.DataFrame({'human': human_lst, 'robot': robot_lst})
new_data.head()
print(new_data)