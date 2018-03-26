1. state machine replication
2. only one is int the log
3. transaction log => to piece to block with header
4. cryptographic one-way hash function => hash(x) = y
    1. examples: SHA_356
    2. how to use: hash identify the entire prefix of the log
5. blocking chain desirable:
    1. high through put
    2. low latency
    3. energy efficient
    4. fairness
    5. secure
    6. no single administrative domain
    7. open membership
        1. one can vote many multiple times by create many identities
        2. permission less and permission comparison
            1. approach
            2. basic tech
            3. trust requirement
            4. membership
            5. energy efficiency
            6. txn rate
            7. txn latency

    8. incentive
        1. mining
        2. fee

6. nonce
    1. exponentially distributed, with constant mean interval
7. fork resolution
    1. a transaction is confirmed when it is buried deep enough, typically 6 blocks
8. Bitcoin parameter
    1. block size and interval 
    2. security and performance trade off
    3. power utilization || fairness(tendency towards centralization)
    4. try some new way:
        1. increasing block frequency or size of block =>mining power utilization slow down
9. permission 
