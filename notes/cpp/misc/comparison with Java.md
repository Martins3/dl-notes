看不懂:
1. C++ classes declarations end in a semicolon.
2. C++ access specification (public, private) is done with labels and in groups.
3. In C++ pointers can point to functions or member functions (function pointers or functors). The equivalent mechanism in Java uses object or interface references. C++11 has library support for function objects.
并没有使用过所谓的java  的函数的 对应的机制
4. oth Java and C++ distinguish between native types (these are also known as "fundamental" or "built-in" types) and user-defined types (these are also known as "compound" types). In Java, native types have value semantics only, and compound types have reference semantics only. In C++ all types have value semantics, but a reference can be created to any object, which will allow the object to be manipulated via reference semantics.
所以 C++ 可以做到什么,但是 java 做不到

5. Java has generics. C++ has templates.

6. Java features standard API support for reflection and dynamic loading of arbitrary new code.

7. Java requires automatic garbage collection. Memory management in C++ is usually done by hand, or through smart pointers. The C++ standard permits garbage collection, but does not require it; garbage collection is rarely used in practice. When permitted to relocate objects, modern garbage collectors can improve overall application space and time efficiency over using explicit deallocation.

有意思:
1. const in C++ indicates data to be 'read-only,' and is applied to types. final in Java indicates that the variable is not to be reassigned. For basic types such as const int vs final int these are identical, but for complex classes, they are different.
```
java 的 final :
class : inherit
method : override or inherit
variable : It does not need to be initialized at the point of declaration: this is called a "blank final" variable. A blank final instance variable of a class must be definitely assigned in every constructor of the class in which it is declared; similarly, a blank final static variable must be definitely assigned in a static initializer of the class in which it is declared
inner class : 原理不是很清楚为什么如此 ?

C++ 的 final:
1. constancy of a value can be changed by casting 
2. const pointer
3. const variable means read only
```
2. Java explicitly distinguishes between interfaces and classes. In C++ multiple inheritance and pure virtual functions makes it possible to define classes that function just as Java interfaces do.   
3. In Java, bounds checking is implicitly performed for all array access operations. In C++, array access operations on native arrays are not bounds-checked, and bounds checking for random-access element access on standard library collections like std::vector and std::deque is optional.

https://en.wikibooks.org/wiki/C%2B%2B_Programming/Programming_Languages/Comparisons/Java 未完待续