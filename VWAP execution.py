from dataclasses import dataclass
import sys

@dataclass
class Tick: 
    ts: float #timestamp of the trade (seconds)
    px: float # trade price
    qty: float #trade size

def gen_synthetic_tape(
    n_seconds: int = 3600, # how long I want the fake market day (3600s = 1 hour) 
    px0: float = 100, # starting price of the stock
    vol_mean: float = 2000.0, # average number of shares/contracts traded per second
    drift_bps_per_hr: float = 0.5, # directional drift in price, in basis points per hour
    vol_of_vol: float = 0.5, # randomness of volume (how spiky it is)
    seed: Optional[int] = None # random seed for reproducibility
) -> Tape


