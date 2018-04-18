fun double (0 : int) : int = 0
    | double n = 2 + double (n - 1)


fun sqrt (0 : int) : int = 0
    | sqrt 1 = 1
    | sqrt n = 4 + double(n - 2) + double(n - 2)  + sqrt(n - 2);

sqrt 10;
sqrt 11;
sqrt 1;
sqrt 2;
