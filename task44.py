import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

print(data.head())

data_one_hot = pd.DataFrame({'IAm_human ': data['whoAmI'].apply(lambda x: 1 if x == 'human' else 0)})
whoAmI_robot = pd.DataFrame({'IAm_robot ': data['whoAmI'].apply(lambda x: 1 if x == 'robot' else 0)})
data_one_hot['IAm_robot'] = whoAmI_robot

print(data_one_hot)