#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 19:00:19 2019

@author: elissandro
"""

import pandas as pd

base = pd.read_csv('census.csv')

# Dividir a base 
# As colunas seria de 0:13, mas sempre o indice final é excludente, portanto, 
# temos que coloca +1
previsores = base.iloc[:, 0:14].values
