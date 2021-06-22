
import pymagicc
from pymagicc import MAGICC6
from pymagicc import rcp26, rcp45, rcp60, rcp85
from pymagicc.io import MAGICCData
import pandas as pd
from matplotlib import pyplot as plt

with MAGICC6() as magicc:
    dataset2 = magicc.run(rcp26)
    for rcp in [rcp45, rcp60, rcp85]:
        dataset2.append(magicc.run(rcp), inplace=True)

dataset2.to_csv('rcp_data.csv')

Mydataset_df=pd.read_csv('rcp_data.csv')

df_filtered2 = Mydataset_df[(Mydataset_df.region == 'World') & (Mydataset_df.variable == 'Emissions|CO2|MAGICC AFOLU')]

df_filtered2= df_filtered2.drop(['climate_model', 'model', 'region', 'todo', 'unit', 'variable'], axis=1)

datafrm2= df_filtered2.T.reset_index().drop(0)

# datafrm2.reindex()
datafrm2.columns = [ 'year','RCP26', 'RCP45', 'RCP60', 'RCP85']
datafrm2['year']=pd.to_datetime(datafrm2['year'], errors = 'coerce')

df2=datafrm2

    
_, ax = plt.subplots(nrows=1, ncols=1, figsize=(16, 9))
for col in df2.columns[1:]:
    ax.plot(df2['year'], df2[col], label=col.upper())
    
ax.legend(title='Scenarios')
ax.set_xlabel('Year')
ax.set_ylabel('Emissions|CO2|MAGICC AFOLU')
ax.set_title('Emissions|CO2|MAGICC AFOLU')
    
plt.savefig("Co_emission.png")        