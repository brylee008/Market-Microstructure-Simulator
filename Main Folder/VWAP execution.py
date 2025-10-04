from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
import math
import random

@dataclass
class Tick: 
    ts: float # seconds from start (0, 1, 2, ...) 
    px: float # price at this second ("execution price")
    qty: float # market volume traded during this second


Tape = List[Tick]

def gen_synthetic_tape(
    n_seconds: int = 3600, # how long I want my fake timeline to be;
    px0: float = 100, # starting price of the stock
    vol_mean: float = 2000.0, # average number of shares/contracts traded per second
    drift_bps_per_hr: float = 0.5, # directional drift in price, in basis points per hour
    vol_of_vol: float = 0.5, # randomness of volume (how spiky it is)
    seed: Optional[int] = None # random seed for reproducibility
) -> Tape:
    
    if seed is not None:
        random.seed(seed)

    tape: Tape = []
    px = px0

    drift_per_sec = (drift_bps_per_hr / 10000) * (px0 / 3600) # convert bps/hr to $/sec

    for t in range(n_seconds): 
        noise = random.gauss(0, 0.01) # ~1 cent std dev noise
        px = max(0.01, px + drift_per_sec + noise) # price can't go below 1 cent
        vol_scale = math.exp(random.gauss(0, vol_of_vol)) # log-normal volume spikes
        qty = max(0.0, vol_mean * vol_scale) # volume can't be negative
        tape.append(Tick(ts=t, px=px, qty=qty))
    return tape

## so, the price randomizer is based offf of drift_per_sec which is based off of the random guass, (white noise) std deviation formuia 
## formula = 1/2 N_0*T where T = 

if __name__ == "__main__":
    tape = gen_synthetic_tape(n_seconds=10, px0=100.0, vol_mean=1000, seed=None)
    for tick in tape:
        print(tick)


def exec_pro_rate(tape, q_total=100, fraction=None, arrival_px=None):
    """
    Buy q_total by taking frac of each second's traded volume. 
    Pays that second's price, returns fills.
    
    """
    filled = 0.0
    notional = 0.0
    fills = [] 

    if arrival_px is None:
        arrival_px = tape[0].px if tape else 100.0

    for t in tape: 
        if filled >= q_total:
            break
        want = fraction * t.qty
        take = min(want, q_total - filled)
        if take > 0: 
            filled += take
            notional += take * t.px
        fills.append({
            "ts": t.ts,
            "mkt_px": t.px,
            "take": take, 
            "cum_filled": filled
        })

    exec_vwap = (notional/filled) if filled > 0 else float("man")
    is_bps = ((exec_vwap - arrival_px) / arrival_px  * 1e4) if filled > 0 else float ("nan")

    summary = {
        "q_total": Q_total,
        "filled": filled, 
        "fill_ratio": filled / q_total if q_total else float("nan"),
        "arrival_px": arrival_px,
        "exec_vwap": exec_vwap,
        "IS_bps": is_bps,
        "mkt_vwap": market_vwap(tape),
        "mkt_twap": market_twap(tape),
        "seconds_used": len(fills)
    }
    return summary, fills

###### Rolling VWAP/TWAP 

####2) Smart -order routing
