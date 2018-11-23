
1. This keyword informs the compiler that the variable it is qualifying as volatile (can change at anytime) is excluded from any optimization techniques. Usage of this variable should be reserved for variables that are known to be modified due to an external influence of a program (whether it's hardware update, third party application, or another thread in the application).

Since the volatile keyword impacts performance, you should consider a different design that avoids this situation: most platforms where this keyword is necessary provide an alternative that helps maintain scalable performance.

Note that using volatile was not intended to be used as a threading or synchronization primitive, nor are operations on a volatile variable guaranteed to be atomic.
这一个 volatile 的使用不是很清楚的啊 !

2. 




