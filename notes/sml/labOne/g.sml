fun oddP (0 : int) : bool = false
  | oddP 1 = true
  | oddP n = oddP (n - 2);

oddP 0;
oddP 1;
oddP 123;
oddP 456;
