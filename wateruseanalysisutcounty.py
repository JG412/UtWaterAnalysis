# -*- coding: utf-8 -*-
"""WaterUseAnalysisUTcounty.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fQkmFkJQuhnwV19O7vGaLVFdI4islYNR
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
import math
import seaborn as sns
from matplotlib import pyplot as plt

utahCwaterList = []
df15water = pd.read_csv('/content/drive/MyDrive/DATA FOLDER/15WaterUse.csv')
utahCwaterList.append(df15water)
df16water = pd.read_csv('/content/drive/MyDrive/DATA FOLDER/16WaterUse.csv')
utahCwaterList.append(df16water)
df17water = pd.read_csv('/content/drive/MyDrive/DATA FOLDER/17WaterUse.csv')
utahCwaterList.append(df17water)
df18water = pd.read_csv('/content/drive/MyDrive/DATA FOLDER/18WaterUse.csv')
utahCwaterList.append(df18water)
df19water = pd.read_csv('/content/drive/MyDrive/DATA FOLDER/19WaterUse.csv')
utahCwaterList.append(df19water)

x = 2014
i = 0
dfAll = pd.DataFrame()
dfTot = pd.DataFrame()
for df in utahCwaterList:
  x += 1
  df.Year = x
  dfTot = pd.concat([dfTot, df], ignore_index=True)
  
  df.drop(df[df.NAME != "UTAH"].index, inplace=True)
  df.NAME = "UTAH " + str(x) 
  dfAll = pd.concat([dfAll, df], ignore_index=True)

dfAll

# for col in corr1:
#   print("correlation of " + col + ' with: ')
#   print(corr1[col])
#   print('\n')

sns.lineplot(x = 'Year', y = 'ResPotGPCD', data = dfAll)
plt.xticks(dfAll['Year'])
plt.show()

#sns.regplot(x = "Year", y = "ResPotGPCD", data = dfTot, truncate=False, line_kws={"color":"black"})
sns.lineplot(x = 'Year', y = 'ResPotGPCD', data = dfTot)
plt.xticks(dfTot['Year'])
plt.title("Residential Water Use in Utah")
plt.ylabel("Gallon Per Capita Per Day")
plt.savefig('ResWaterUseUtah.jpeg')
plt.show()

sns.histplot(dfTot['ResPotGPCD'], bins=30)
plt.savefig('ResWaterUseUtah.jpeg')
plt.title('Histogram of Residential Water Usage in Utah')
plt.xlabel('Residential GPCD')
plt.show()

sns.histplot(dfAll["ResPotGPCD"])
plt.savefig('ResWaterUThistplot.jpeg')
plt.show()

waterCostDict = {}
UtahAvg = (dfTot["ResPotGPCD"].mean())
waterCostDict['UTavg GPCD'] = (dfTot["ResPotGPCD"].mean())
UtahValAvg = (dfAll["ResPotGPCD"].mean())
waterCostDict['UVavg GPCD'] = (dfAll["ResPotGPCD"].mean())
costWater = 2.48/1000
waterCostDict['costWater'] = 2.48/1000
costPerDayUt = UtahAvg*costWater
waterCostDict['costPerDayUt'] = costPerDayUt
costPerDayUv = UtahValAvg*costWater
waterCostDict['costPerDayUV'] = costPerDayUv
yrUT = costPerDayUt*365
waterCostDict['costPerYearUT'] = yrUT
yrUV = costPerDayUv*365
waterCostDict['costPerYearUV'] = yrUV

for key in waterCostDict:
  phrase = key + " : " + str(round(waterCostDict[key],4))
  print(phrase)