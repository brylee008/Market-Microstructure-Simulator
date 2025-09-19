from dataclasses import dataclass
import sys

@dataclass
class Tick: 
    ts: float #timestamp of the trade (seconds)
    px: float # trade price
    qty: float #trade size

class RollingExec:
    def __init__(self, Q-total: float, arrival_px: float):
        self.Q_total = float(Q_total) # the child order size you want to buy
        self.arrival_px = float(arrival_px) # benchmark at decision time (usually the mid)
        self.filled_qty = 0.0 # how much you've bought so far
        self.notional = 0.0 #dollars paid so far = sum(price * qty)


