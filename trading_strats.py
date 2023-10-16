# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:20:17 2023

@author: antch
"""
import numpy as np
import matplotlib.pyplot as plt

#1
def covered_call(S0, S, K, p):
    return K - S0 - np.max(K-S,0) + p
#2
def covered_put(S0, S, K, p):
    return S0 - S - np.max(K-S,0) + p
#3
def protective_put(S0, S, K, p):
    return S - S0 + np.max(K-S,0) - p
#4
def protective_call(S0, S, K, p):
    return S0 - S + np.max(S-K,0) - p
#5
def bull_call_spread(S, K1, K2, p1, p2):
    return np.max(S-K1,0) - np.max(S-K2,0) - p1 + p2
#6
def bull_put_spread(S, K1, K2, p1, p2):
    return np.max(K1-S, 0) - np.max(K2 - S,0) - p1 + p2
#7
def bear_call_spread(S, K1, K2, p1, p2):
    return np.max(S-K1,0) - np.max(S-K2,0) + p2 - p1
#8
def bear_put_spread(S, K1, K2, p1, p2):
    #K2 < K1
    return np.max(K1-S,0) - np.max(K2-S,0) + p2 - p1
#9
def long_synthetic_forward(S, K, p1, p2):
    return np.max(S-K,0) - np.max(K-S,0) + p2 - p1
#10
def short_synthetic_forward(S, K, p1, p2):
    return np.max(K-S,0) - np.max(S-K,0) + p2 - p1
#11
def long_combo(S, K1, K2, p1, p2):
    return np.max(S-K1,0) - np.max(K2-S,0) + p2 - p1
#12
def short_combo(S, K1, K2, p1, p2):
    #K1 < K2
   return np.max(K1-S,0) - np.max(S - K2, 0) + p2 - p1
#13
def bull_call_ladder(S, K1, K2, K3, p1, p2, p3):
    return np.max(S-K1,0) - np.max(S-K2,0) - np.max(S-K3,0) + p2 + p3 - p1
#14
def bull_put_ladder(S, K1, K2, K3, p1, p2, p3):
    return - np.max(K1 - S,0) + np.max(K2-S,0) + np.max(K3-S,0) + p1 - p2 - p3
#15
def bear_call_ladder(S, K1, K2, K3, p1, p2, p3):
    return -np.max(S-K1,0) + np.max(S-K2,0) + np.max(S-K3,0) + p1 - p2 - p3
#16
def bear_put_ladder(S, K1, K2, K3, p1, p2, p3):
    return np.max(K1-S,0) - np.max(K2-S,0) - np.max(K3-S,0) + p2 + p3 - p1
#17
def calendar_call_spread(S1, S2, Stop, K, p1 , p2):
    if S < Stop:
return 


