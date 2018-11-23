def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

def longest_consec(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""

def fname(arg):
    return 10 if arg>=20 else 20
print(fname(23))

def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1

def is_prime(num):
    return num > 1 and not any(num % n == 0 for n in range(2,num))

def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)
