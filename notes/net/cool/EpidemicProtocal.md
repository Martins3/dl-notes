1. pull epidemic
    start slowly, and end quickly !


2. basic protocol
    1. member maintains a list of pairs
    2. periodically, each member gossips:
        1. increments its own heartbeat
        2. send list tk randomly chosen member
    3. on receipt of gossip, merge list
    4. each member maintain most height heartbeat increase for each other

3. random sample with log(n) to avoid too long list !


case study 1: Failure Detection

case study 2: Bimodal MultiCast
gossip problem: high latency
tree base MultiCast: fragile
digest: 

