# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:20:17 2023

@author: antch
"""
import numpy as np


def covered_call(S0, S, K, p):
    return K - S0 - np.max(S-K,0) + p

def covered_put(S0, S, K, p):
    return S0 - S - np.max(K-S,0) + p


def protective_put(S0, S, K, p):
    return S - S0 + np.max(K-S,0) - p

def protective_call(S0, S, K, p):
    return S0 - S + np.max(S-K,0) - p

def bull_call_spread(S0, S, K1, K2, p1, p2):
    return np.max(S-K1,0) - np.max(S-K2,0) - p1 + p2

def bull_put_spread(S0, S, K1, K2, p1, p2):
    #K1 < K2  and p2 > p1
    return np.max(K1-S, 0) - np.max(K2 - S,0) - p1 + p2

def test(r):
    return r*90
