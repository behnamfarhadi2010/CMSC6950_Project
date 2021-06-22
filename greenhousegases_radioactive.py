
import pymagicc
from pymagicc import MAGICC6
from pymagicc import rcp26, rcp45, rcp60, rcp85
from pymagicc.io import MAGICCData
import pandas as pd
from matplotlib import pyplot as plt

with MAGICC6() as magicc:
    dataset = magicc.run(rcp26)
    for rcp in [rcp45, rcp60, rcp85]:
        dataset.append(magicc.run(rcp), inplace=True)

dataset.to_csv('rcp2_data.csv')

dataset_df=pd.read_csv('rcp2_data.csv')


df_filtered = dataset_df[(dataset_df.region == 'World') & (dataset_df.variable == 'Radiative Forcing|Greenhouse Gases')]


df_filtered= df_filtered.drop(['climate_model', 'model', 'region', 'todo', 'unit', 'variable'], axis=1)

datafrm= df_filtered.T.reset_index().drop(0)


datafrm.columns = [ 'year','RCP26', 'RCP45', 'RCP60', 'RCP85']
datafrm['year']=pd.to_datetime(datafrm['year'], errors = 'coerce')

df=datafrm

_, ax = plt.subplots(nrows=1, ncols=1, figsize=(16, 9))
for col in df.columns[1:]:
    ax.plot(df['year'], df[col], label=col.upper())
ax.legend(title='Scenarios')
ax.set_xlabel('Year')
ax.set_ylabel('Radiative Forcing|Greenhouse Gases')
ax.set_title('Radiative Forcing|Greenhouse Gases')
ax.grid()

plt.savefig("Radiative_Forcing.png") 

