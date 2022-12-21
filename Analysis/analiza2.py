# -*- coding: utf-8 -*-
"""Analiza2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A9g_FSAjua48sv5zKpZqS5pu-_VBdDKF

#Instalacja i import potrzebnych pakietów
"""

import warnings
warnings.filterwarnings('ignore')

!pip install scikit-tda
!pip install Ripser
!pip install persim
#!pip install teaspoon
#!pip install Cython

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import ripser
import persim

from sklearn import datasets
from ripser import ripser
from persim import plot_diagrams
from ripser import Rips
from sklearn.preprocessing import MinMaxScaler

allteams = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/AllTeams.csv')

pd.set_option('display.max_columns', None)

"""#MCI - Manchester City - 1"""

mci = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/MCI.csv')
mci

features_names = mci.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
mci[features_names] = scaler.fit_transform(mci[features_names])
mci

arrayPointsMCI = np.array(mci[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPoints

dgMCI = ripser(arrayPointsMCI)['dgms']
plot_diagrams(dgMCI, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgMCI_H0 = ripser(arrayPointsMCI)['dgms'][0]
plot_diagrams(dgMCI_H0, show=True, xy_range=[-1,3,-1,3])

"""# LIV - Liverpool - 2"""

liv = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/LIV.csv') 
liv

features_names = liv.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
liv[features_names] = scaler.fit_transform(liv[features_names])
liv

arrayPointsLIV = np.array(liv[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPointsLIV

dgLIV = ripser(arrayPointsLIV)['dgms']
plot_diagrams(dgLIV, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgLIV_H0 = ripser(arrayPointsLIV)['dgms'][0]
plot_diagrams(dgLIV_H0, show=True, xy_range=[-1,3,-1,3])

"""#CHE - Chelsea - 3"""

che = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/CHE.csv') 
che

features_names = che.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
che[features_names] = scaler.fit_transform(che[features_names])
che

arrayPointsCHE = np.array(che[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPointsCHE

dgCHE = ripser(arrayPointsCHE)['dgms']
plot_diagrams(dgCHE, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgCHE_H0 = ripser(arrayPointsCHE)['dgms'][0]
plot_diagrams(dgCHE_H0, show=True, xy_range=[-1,3,-1,3])

"""#TOT - Tottenham Hotspur - 4"""

tot = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/TOT.csv') 
tot

features_names = tot.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
tot[features_names] = scaler.fit_transform(tot[features_names])
tot

arrayPointsTOT = np.array(tot[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPointsTOT

dgTOT = ripser(arrayPointsTOT)['dgms']
plot_diagrams(dgTOT, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgTOT_H0 = ripser(arrayPointsTOT)['dgms'][0]
plot_diagrams(dgTOT_H0, show=True, xy_range=[-1,3,-1,3])

"""#ARS - Arsenal - 5"""

ars = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/ARS.csv')
ars

features_names = ars.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
ars[features_names] = scaler.fit_transform(ars[features_names])
ars

arrayPointsARS = np.array(ars[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPointsARS

dgARS = ripser(arrayPointsARS)['dgms']
plot_diagrams(dgARS, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgARS_H0 = ripser(arrayPointsARS)['dgms'][0]
plot_diagrams(dgARS_H0, show=True, xy_range=[-1,3,-1,3])

"""#MUN - Manchester United - 6"""

mun = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/MUN.csv') 
mun

features_names = mun.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
mun[features_names] = scaler.fit_transform(mun[features_names])
mun

arrayPointsMUN = np.array(mun[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPointsMUN

dgMUN = ripser(arrayPointsMUN)['dgms']
plot_diagrams(dgMUN, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgMUN_H0 = ripser(arrayPointsMUN)['dgms'][0]
plot_diagrams(dgMUN_H0, show=True, xy_range=[-1,3,-1,3])

"""#WHU - West Ham United - 7"""

whu = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/WHU.csv') 
whu

features_names = whu.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
whu[features_names] = scaler.fit_transform(whu[features_names])
whu

arrayPointsWHU = np.array(whu[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPoints

dgWHU = ripser(arrayPointsWHU)['dgms']
plot_diagrams(dgWHU, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgWHU_H0 = ripser(arrayPointsWHU)['dgms'][0]
plot_diagrams(dgWHU_H0, show=True, xy_range=[-1,3,-1,3])

"""#LEI - Leicester City - 8"""

lei = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/LEI.csv') 
lei

features_names = lei.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
lei[features_names] = scaler.fit_transform(lei[features_names])
lei

arrayPointsLEI = np.array(lei[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPoints

dgLEI = ripser(arrayPointsLEI)['dgms']
plot_diagrams(dgLEI, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgLEI_H0 = ripser(arrayPointsLEI)['dgms'][0]
plot_diagrams(dgLEI_H0, show=True, xy_range=[-1,3,-1,3])

"""#BHA -	Brighton & Hove Albion - 9"""

bha = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/BHA.csv') 
bha

features_names = bha.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
bha[features_names] = scaler.fit_transform(bha[features_names])
bha

arrayPointsBHA = np.array(bha[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPoints

dgBHA = ripser(arrayPointsBHA)['dgms']
plot_diagrams(dgBHA, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgBHA_H0 = ripser(arrayPointsBHA)['dgms'][0]
plot_diagrams(dgBHA_H0, show=True, xy_range=[-1,3,-1,3])

"""#WOL - Wolverhampton Wanderers - 10"""

wol = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/WOL.csv') 
wol

features_names = wol.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
wol[features_names] = scaler.fit_transform(wol[features_names])
wol

arrayPointsWOL = np.array(wol[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPoints

dgWOL = ripser(arrayPointsWOL)['dgms']
plot_diagrams(dgWOL, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgWOL_H0 = ripser(arrayPointsWOL)['dgms'][0]
plot_diagrams(dgWOL_H0, show=True, xy_range=[-1,3,-1,3])

"""# NEW - Newcastle United - 11"""

new = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/NEW.csv') 
new

features_names = new.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
new[features_names] = scaler.fit_transform(new[features_names])
new

arrayPointsNEW = np.array(new[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPoints

dgNEW = ripser(arrayPointsNEW)['dgms']
plot_diagrams(dgNEW, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgNEW_H0 = ripser(arrayPointsNEW)['dgms'][0]
plot_diagrams(dgNEW_H0, show=True, xy_range=[-1,3,-1,3])

"""# CRY -	Crystal Palace	- 12"""

cry = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/CRY.csv')
cry

features_names = cry.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
cry[features_names] = scaler.fit_transform(cry[features_names])
cry

arrayPointsCRY = np.array(cry[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPoints

dgCRY = ripser(arrayPointsCRY)['dgms']
plot_diagrams(dgCRY, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgCRY_H0 = ripser(arrayPointsCRY)['dgms'][0]
plot_diagrams(dgCRY_H0, show=True, xy_range=[-1,3,-1,3])

"""#BRE - Brentford - 13"""

bre = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/BRE.csv')
bre

features_names = bre.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
bre[features_names] = scaler.fit_transform(bre[features_names])
bre

arrayPointsBRE = np.array(bre[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPoints

dgBRE = ripser(arrayPointsBRE)['dgms']
plot_diagrams(dgBRE, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgBRE_H0 = ripser(arrayPointsBRE)['dgms'][0]
plot_diagrams(dgBRE_H0, show=True, xy_range=[-1,3,-1,3])

"""#AVL - Aston Villa - 14

"""

avl = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/AVL.csv')
avl

features_names = avl.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
avl[features_names] = scaler.fit_transform(avl[features_names])
avl

arrayPointsAVL = np.array(avl[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPoints

dgAVL = ripser(arrayPointsAVL)['dgms']
plot_diagrams(dgAVL, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgAVL_H0 = ripser(arrayPointsAVL)['dgms'][0]
plot_diagrams(dgAVL_H0, show=True, xy_range=[-1,3,-1,3])

"""#SOU - Southampton - 15"""

sou = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/SOU.csv')
sou

features_names = sou.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
sou[features_names] = scaler.fit_transform(sou[features_names])
sou

arrayPointsSOU = np.array(sou[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPoints

dgSOU = ripser(arrayPointsSOU)['dgms']
plot_diagrams(dgSOU, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgSOU_H0 = ripser(arrayPointsSOU)['dgms'][0]
plot_diagrams(dgSOU_H0, show=True, xy_range=[-1,3,-1,3])

"""#EVE - Everton - 16"""

eve = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/EVE.csv')
eve

features_names = eve.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
eve[features_names] = scaler.fit_transform(eve[features_names])
eve

arrayPointsEVE = np.array(eve[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPoints

dgEVE = ripser(arrayPointsEVE)['dgms']
plot_diagrams(dgEVE, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgEVE_H0 = ripser(arrayPointsEVE)['dgms'][0]
plot_diagrams(dgEVE_H0, show=True, xy_range=[-1,3,-1,3])

"""#LEE - Leeds United - 17"""

lee = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/LEE.csv')
lee

features_names = lee.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
lee[features_names] = scaler.fit_transform(lee[features_names])
lee

arrayPointsLEE = np.array(lee[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPoints

dgLEE = ripser(arrayPointsLEE)['dgms']
plot_diagrams(dgLEE, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgLEE_H0 = ripser(arrayPointsLEE)['dgms'][0]
plot_diagrams(dgLEE_H0, show=True, xy_range=[-1,3,-1,3])

"""#BRN - Burnley - 18"""

brn = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/BRN.csv')
brn

features_names = brn.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
brn[features_names] = scaler.fit_transform(brn[features_names])
brn

arrayPointsBRN = np.array(brn[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPoints

dgBRN = ripser(arrayPointsBRN)['dgms']
plot_diagrams(dgBRN, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgBRN_H0 = ripser(arrayPointsBRN)['dgms'][0]
plot_diagrams(dgBRN_H0, show=True, xy_range=[-1,3,-1,3])

"""# WAT - Watford - 19"""

wat = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/WAT.csv')
wat

features_names = wat.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
wat[features_names] = scaler.fit_transform(wat[features_names])
wat

arrayPointsWAT = np.array(wat[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPoints

dgWAT = ripser(arrayPointsWAT)['dgms']
plot_diagrams(dgWAT, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgWAT_H0 = ripser(arrayPointsWAT)['dgms'][0]
plot_diagrams(dgWAT_H0, show=True, xy_range=[-1,3,-1,3])

"""#NOR - Norwich City - 20"""

nor = pd.read_csv('https://raw.githubusercontent.com/wojtaskuba/Projekt_WamberskaWojtasZygmunt/main/Teams/NOR.csv')
nor

features_names = nor.drop(['Player', 'Id', 'POS', 'Team'], axis=1).columns
features_names

scaler = MinMaxScaler()
nor[features_names] = scaler.fit_transform(nor[features_names])
nor

arrayPointsNOR = np.array(nor[['POS','Mins','Goals','Shots','PenGoals','SuccesfulDribbles','Assists','AccPasses','KeyPasses','Fouls','WasFouled','YellowCards','RedCards','RecBalls','Tackles','CleanSheets']])
#arrayPointsNOR

dgNOR = ripser(arrayPointsNOR)['dgms']
plot_diagrams(dgNOR, show=True, xy_range=[-1,3,-1,3])

#diagram dla dziur zerowymiarowych (składowych spójnych)
dgNOR_H0 = ripser(arrayPointsNOR)['dgms'][0]
plot_diagrams(dgNOR_H0, show=True, xy_range=[-1,3,-1,3])

"""#Odległość między parami diagramów persystencji H0

##Przykład dla MCI i CHE:
"""

#diagram uwzględniający dane z MCI i CHE
plot_diagrams([dgMCI_H0, dgCHE_H0] , labels=['MCI_H0', 'CHE_H0'])
plt.show()

distance_bottleneck_MCI_CHE, matching = persim.bottleneck(dgMCI_H0, dgCHE_H0, matching=True)

#wizualne przedstawienie dystansu
persim.bottleneck_matching(dgMCI_H0, dgCHE_H0, matching, labels=['MCI_H0', 'CHE_H0'])
plt.show()

print(distance_bottleneck_MCI_CHE)

#skrótowe obliczenie odległości
persim.bottleneck(dgMCI_H0, dgCHE_H0)

"""##Przykład dla MCI i NOR:"""

#diagram uwzględniający dane z MCI i NOR
plot_diagrams([dgMCI_H0, dgNOR_H0] , labels=['MCI_H0', 'NOR_H0'])
plt.show()

distance_bottleneck_MCI_NOR, matching = persim.bottleneck(dgMCI_H0, dgNOR_H0, matching=True)

#wizualne przedstawienie dystansu
persim.bottleneck_matching(dgMCI_H0, dgNOR_H0, matching, labels=['MCI_H0', 'NOR_H0'])
plt.show()

print(distance_bottleneck_MCI_NOR)

#skrótowe obliczenie odległości
persim.bottleneck(dgMCI_H0, dgNOR_H0)

"""##Przykład dla CHE i NOR:"""

#skrótowe obliczenie odległości
persim.bottleneck(dgCHE_H0, dgNOR_H0)