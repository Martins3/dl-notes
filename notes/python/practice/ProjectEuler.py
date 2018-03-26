class ProjectEuler(object):
    """docstring for ProjectEuler."""


    def solu2(self):
        upper_bound = 4000000
        a, b, c = 1, 1, 1
        while(True):
            a = a + b
            b = a - b
            if b>= upper_bound:
                break
            if b%2 !=0:
                c = c + b
        return c


    def solu3(self):
        init = 600851475143
        largest_prime = init
        i = 2
        while(True):
            if(i**2> largest_prime):
                return largest_prime
            if (largest_prime % i)==0 :
                largest_prime = largest_prime // i
                i = 2
            else:
                i = i + 1
    def solu48(self):
        keep = 10000000000
        def cal(x):
            m = 1
            kk = 1
            while m <= x:
                kk = (kk * x)%keep

        s = 0
        for i in range(11):
            s = s + i**i
        return s
p = ProjectEuler()
print(p.solu48())
