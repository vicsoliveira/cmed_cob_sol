# -*- coding: utf-8 -*-
"""geo_cal_cmed

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Df9ZoIckblkeNp_VhemScJQgFEdnfOk
"""

!pip install geopandas
!pip install geemap

import pandas as pd
import geopandas as gp
import geemap

from google.colab import drive
drive.mount('/content/gdrive')

c_tip_r = pd.read_csv('/content/gdrive/MyDrive/qgis/c_tip_rua.csv')

cob_sol = gp.read_file('/content/gdrive/MyDrive/qgis/cob_sol_bc_p_a.shp')

ruas_t = c_tip_r['rua']
ruas = []
for r in ruas_t:
    ruas.append(r)
print(ruas)

len_ruas = len(ruas)
r_p = []
i = 0
while i < len_ruas:
  for c in list(cob_sol.columns):
    if ruas[i] in c and '_p' in c:
      r_p.append(c)
  i=i+1

print(r_p)

for index in range(len(cob_sol)):
  cob_sol['Cmed'].iloc[index] = 0
  c = cob_sol['Cmed'].iloc[index]
  print(c)

for p in r_p:
  if ruas[0] in p:
    print(p)

print(len(cob_sol))

c_idx = c_tip_r.columns.get_loc('c')
for index in range(len(cob_sol)):
  it = 0
  while it < len_ruas:
    c_f = c_tip_r.iloc[it, c_idx]
    for p in r_p:
      if ruas[it] in p:
        cp = cob_sol[p].iloc[index]
        cmed = cob_sol['Cmed'].iloc[index]
        cmed = cmed + (cp/100)*c_f
        cob_sol['Cmed'].iloc[index] = cmed
    it = it + 1

for ind in range(len(cob_sol)):
  cmed = cob_sol['Cmed'].iloc[ind]
  print(cmed)

cob_sol.to_file('/content/gdrive/MyDrive/qgis/cob_sol_bc_p_a_cmed2.shp')