# Greedy Algorithms
> 如何证明是ga, 如何找到ga

## 1 Interval Scheduling: The Greedy Algorithm Stays Ahead
algorithm: f(i) as small as possible
analyzing: n*log(n)
extension: online interval with weight 

### A Related Problem: Scheduling All Intervals
A related problem arises if we have many identical resources available and we wish to schedule all the requests using as few resources as possible
algorithm: attach labels

## 2 Scheduling to Minimize Lateness: An Exchange
deadline  && minimize the maximum lateness
algorithm: earliest deadline first

Our plan here is to gradually modify O, preserving its optimality at each step, but eventually transforming
it into a schedule that is identical to the schedule A found by the greedy
algorithm. We refer to this type of analysis as an **exchange argument**

prove:
1. There is an optimal schedule with no idle time.
2. All schedules with no inversions and no idle time have the same maximum lateness
3. There is an optimal schedule that has no inversions and no idle time

> :confused: 没有查看prove 3 129

extension: with release time 

## 3 Optimal Caching: A More Complex Exchange Argument

