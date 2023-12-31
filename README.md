# trading_strategy
This repository purpose is to have a function for each trading strategy that I know. Trading strategy knowledge is the first step to have a better understanding of HFT possibilities.

Notation:
S: Spot
S0:  spot at time 0
K: strike price
p : premium

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

Strategy 5: Bull Call Spread
  (1) Long Call close to at the money + (2) Short Call out of the money
  K1 = S0, K2 > S0
  Outlook on Spot: bullish
  Function: p2 - p1 < bull_call_spread < K2 - K1 - p1 + p2

Strategy 6: Bull Put Spread
  (1) Long out of the money Put + (2) Short out of the money Put
  K2 > K1
  outlook on Spot: bullish
  Function: K1 - K2 - p1 + p2 < bull_put_spread < p2 - p1

Strategy 7: Bear Call Spread
  (1) Long out of the money call + (2) Short out of the money Call
  outlook on Spot: bearish
  payoff interval: [K2 - K1 + p2 - p1 ; p2 - p1]

Straregy 8: Bear Put Spread
  (1) Long at the money Put + (2) short out of the money put with K2 < K1
  outlook: neutral/bearish
  payoff interval: [p2 - p1 ; K1 - K2 + p2 - p1]

Strategy 9: Long Synthetic Forward
  (1) buy at the money Call + (2) sell at the money put
  outlook: neutral/bullish
  payoff interval: [p2 - p1 + K ; +∞[

Strategy 10: Short Synthetic Forward
  (1) buy a put + (2) sell a call
  at the money for 1 and 2
  outlook: bearish
  payoff interval: ]-∞ ; K + p2 - p1]

Strategy 11: Long Combo
  (1) buy out of the money Call + (2) sell out of the money Put
  outlook: bullish
  payoff interval: [p2 - p1 + K2 ; +∞[

Strategy 12: Short Combo
  (1) Buy out of the money Put + (2) short out of the money Call
  outlook: bearish
  payoff interval: ]-∞ ; K1 + p2 - p1]

Strategy 13: Bull Call Ladder
  (1) long at the money Call + (2) short out of the money Call + (3) short out of the money Call
  K3 >  K2 > K1
  outlook: neutral/bullish
  payoff interval: ]-∞ ; K2 - K1 + p2 + p3 - p1]

Strategy 14: Bull Put Ladder
  (1) short at the money Put + (2) long out of the money Put + (3) long out of the money Put
  K1 > K2 > K3
  outlook on Spot: bearish
  payoff interval: [K2 - K1 + p1 - p2 - p3 ; K2 + K3 - K1 + p1 - p2 - p3]

Strategy 15: Bear Call Ladder
  (1) short at the money Call + (2) long out of the money Call + (3) long out of the money Call
  K1 < K2 < K3
  outlook on Spot: bullish
  payoff interval: [ K2 - K1 + p1 - p2 - p3 ; +∞[

Strategy 16: Bear Put Ladder
  (1) long at the money Put + (2) short out of the money Put + (3) short out of the money Put
  K1 > K2 > K3
  outlook on Spot: neutral
  payoff interval: [ K1 - K2 - K3 + p2 + p3 - p1 ; K1 - K2 + p2 + p3 - p1]

Strategy 17: Long Straddle
  volatility strategy
  (1) long out of the money Call + (2) long at the money Put
  outlook on Spot: market move
  payoff interval: [ - p1 - p2 ; +∞ [
  
Strategy 18: Long Strangle
  volatility strategy
  (1) long out of the money call + (2) long out of the money Put
  outlook on Spot: market move
  payoff interval: [ - p1 - p2 ; +∞ [

Strategy 20: Long Guts
  (1) long in the money Call + (2) long in the money Put
  more expensive than Long Straddle
  outlook on Spot: Neutral
  same function as long straddle

Strategy 21: Short Straddle
  (1) short at the money Call + short at the money Put
  outlook on spot: neutral
  payoff_function : - long_straddle

Strategy 22: Short Strangle
  (1) short out of the money Call + (2) short out of the money Put
  outlook on Spot: neutral
  payoff_function = -long_strangle

Strategy 23: Short Guts
  more expensive than Short straddle
  outlook on Spot: neutral
  same payoff funciton

Strategy 24: Long Put Synthetic Straddle
  buy S0 + (1) long at the money Put / the nearest in the money + (2) long at the money Put / the nearest in the money
  capital gain strategy
  outlook on Spot: neutral

  
Strategy 25: Short Call Synthetic Straddle
 
  buy S0 + (1) short at the money Call / the nearest in the money +  short at the money Call / the nearest in the money
  outlook on Spot: 