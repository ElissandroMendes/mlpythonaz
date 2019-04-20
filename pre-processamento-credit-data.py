#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:38:05 2019

@author: elissandro
"""

import pandas as pd

base = pd.read_csv('credit-data.csv')
base.describe()
base.loc[base['age'] < 0]

# Apagar uma coluna
base.drop('age', 1, inplace=True)

# Apagar os registros 
base.drop(base[base.age < 0].index, inplace=True)

# Preencher os valores errados com a média
base.mean() # Calcula a média de todas as colunas
base['age'].mean() # Posso executar métodos do Dataframe
media = base['age'][base.age > 0].mean() # Filtra registros para calcular a média
base.loc[base.age < 0, 'age'] = media

# Verificando valores null
pd.isnull(base['age'])
base.loc[pd.isnull(base['age'])]

# Podemos preencher com a média
base.loc[pd.isnull(base['age']), 'age'] = media

# Separando os dados
previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

# Usando a classe Imputer para preencher os NaN
# Limite superior sempre +1
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(previsores[:, 0:3])
previsores[:, 0:3] = imputer.transform(previsores[:, 0:3])

# Escalonamento
# Em  algoritmos que se baseam em distancia euclidiana Ex: KNN, precisamos
# ter os valores na mesma escala.
# Formas de escalonar:
# X = (x - media(x)) / desvio padrão x -> Padronização
# X = (x - min(x)) / max(x) - min(x) -> Normalização
# A padronização é melhor para tratar outliers

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)













