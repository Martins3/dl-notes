# C++
## chapter 1
1. In computer programming, a free-form language is a programming language in which the positioning of characters on the page in program text is insignificant
2. Features introduced in C++ include declarations as statements, function-like casts, new/delete, bool, reference types, const, inline functions, default arguments, function overloading, NAMESPACES, classes (including all class-related features such as inheritance, member functions, virtual functions, abstract classes, and constructors), operator overloading, templates, the :: operator, exception handling, run-time type identification, and more type checking in several cases Several features of C++ were later adopted by C, including const, inline, declarations in for loops, and C++-style comments (using the // symbol)
3. 


这一章就是老生常谈

## chapter 2
1. The C++ standard does not impose any specific rules on how files are named or organized.
2. we’re talking about a .cpp file, we’ll call it an "implementation file", and any time we’re referring to a header file, we’ll call it a "declaration file"
3. Classes are usually declared inside header files

### Coding style conventions
1. 25 lines 80 columns
2. Placement of braces
3. Placement of braces
4. Naming identifiers
5. Leading underscores
In most contexts, leading underscores are better avoided.
6. Reusing existing names
7. Hungarian notation
outdated
8. Names indicate purpose
9. Capitalization
In identifiers which contain more than one natural language words, either underscores or capitalization is used to delimit the words, e.g. num_chars (K&R style) or numChars (Java style). It is recommended that you pick one notation and do not mix them within one project.
10. Constants
When naming #defines, constant variables, enum constants. and macros put in all uppercase using '_' separators
11. Functions and member functions
12. Explicitness or implicitness
    1. inline const : better use
    2. typedef      : not recommended
13. Pointer declaration
    1. int* ptr;
    2. int* ptrA, ptrB;

### Documentation
似乎没有告诉如何写, 只是说明了书写的重要性

### Scope
https://en.wikibooks.org/wiki/C%2B%2B_Programming/Programming_Languages/C%2B%2B/Code/Statements/Scope
看不懂, 用不上

### Compiler
https://en.wikibooks.org/wiki/C%2B%2B_Programming/Programming_Languages/C%2B%2B/Code/Compiler

剩下的部分以后看

## chapter 3

### Structures
1. A struct is like a class except for the default access (class has default access of private, struct has default access of public)
2. 

### Union

### Class

### Operator overloading

### Standard IO Library