This module implements a realistic, but minimal Smart-Order Router that sweeps top-of-book (TOB) liquidity across multiple venues while accounting for explicit fees/rebates and implicit latency/slippage penalties. It's designed to plug into the broader Market Microstructure project and interoperate with the Execution and Order Book modules. 

Goals: 
- route an incoming parent order (marketable child slices) across venues
- Minimize total effective cost (price + fees - rebates + latency penalty).
- Produce audit-ready fill logs and cost attribution (what came from price vs fees vs latency)
- Be easily extensible (plug in new venues, fee schedules, latency models, and policies)

Concepts & Definitions: 
Venue: An exchange/ATS with its own fee schedule, queue/latency characteristics, and top-of-book quote. 
Top-of-Book (TOB): Best bid/ask and available displayed size on a venue
Explicit cost: Maker/taker fees and/or rebates applied per share or per notional
Implicit cost (latency penalty): Expected loss from stale quotes, queue position, or adverse selection while the order is in flight. 

