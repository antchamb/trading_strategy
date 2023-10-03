# trading_strategy
This repository purpose is to have a function for each trading strategy that I know. Trading strategy knowledge is the first step to have a better understanding of HFT possibilities.

Strategy 1: Covered Call
  Type: conservative
  Buy S0 + Write a Call <=> Write a Put
  Outlook on Spot : neutral to bullish
  Function:    S0 - p < covered_call(S0, S, K, p) < K - S0 + p

Strategy 2: Covered Put
  Type: conservative
  Short S0 + Write a Put <=> Write a Call
  Outlook on Spot: neutral to bearish
  Function:   -∞ < covered_put(S0, S, K, p) < S0 - K + p
  
Strategy 3: Protective put
  Type: hedging
  Buy S0 + Buy at the money Put or out the money Put (<=> K <= S0)
  Outlook on Spot: bullish
  Function:    S - K + p < protective_put(S0, S, K, p) < +∞
  
Strategy 4: Protective call
  type: hedging
  Short S0 + Buy a Call (out or at the money)
  Outlook on Spot: bearish
  Function:   S0 - K - p < protective_call < S0 - p
