# trading_strategy
This repository purpose is to have a function for each trading strategy that I know. Trading strategy knowledge is the first step to have a better understanding of HFT possibilities.

Strategy 1: Covered Call
  buy S0 and write a Call <=> write a Put
  trader outlook on Spot : neutral to bullish
  covered
  function:    S0 - p < covered_call(S0, S, K, p) < K - S0 + p

Strategy 2: Covered Put
  Short S0 and write a Put <=> write a Call
  trader outlook on Spot: neutral to bearish
  function:   -∞ < covered_put(S0, S, K, p) < S0 - K + p
  
