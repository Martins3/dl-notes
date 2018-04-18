fun divisibleByThree(0: int): bool = true
  | divisibleByThree 1 = false
  | divisibleByThree 2 = false
  | divisibleByThree n = divisibleByThree(n - 3);

divisibleByThree 1;
divisibleByThree 2;
divisibleByThree 3;
divisibleByThree 4;
divisibleByThree 100;
divisibleByThree 1000101;
