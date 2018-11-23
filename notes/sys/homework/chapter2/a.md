#### PRACTICE 2.5 p45
A.  Little endian:21  
    Big endian:87  
B.  Little endian: 21 43  
    Big endian:87 65  
C.  Little endian: 21 43 65  
    Big endian:87 65 43  
#### PRACTICE 2.6 p46
A. Write the binary representations of these two hexadecimal values.  
       1101011001000101000001  
1001010010101100100010100000100  
B. Shift these two strings relative to one another to maximize the number of
matching bits. How many bits match?  
21  
C. What parts of the strings do not match?  
head and tail  
#### PRACTICE 2.7 p46
const char *s = "abcdef";  
show_bytes((byte_pointer) s, strlen(s));  
61 62 63 64 65 66
#### PRACTICE 2.11 p52
C: there are several ways
cycle just cnt/2 times,in another word,change the conditions to break the loop
#### PRACTICE 2.12 p53
    int x=0x87654321;
    int a=x&0xff;
    int b=((~(0xff))&(~x))|a;
    int c=(0xff)|x;
#### practice 2.13 p53
int res=x|y
int res=(x|y)^y
#### practice 2.18 p64
    // para: x should be 16bit hexadecimal number
    void toDecimal(int x){
        int a=x>=0x8000?1:0;
        printf("%d",-a*0x8000+(x%(0x8000)));
    }
#### practice 2.21 p70
```
int a[]={-2147483647-1 == 2147483648u,
         -2147483647-1 < 2147483647,
         -2147483647-2u == 2147483647,
         -2147483647-1 < -2147483647,
         -2147483647-1u < -2147483647
};
void explicitt(){
    for (int i = 0; i <5 ; ++i) {
        printf("%d",a[i]);
    }

    printf("\n%u",0x80000000);
}
```
#### practice 2.23 p74
    int fun1(unsigned word) {
        return (int) ((word << 24) >> 24);
    }
    int fun2(unsigned word) {
        return ((int) word << 24) >> 24;
    }
函数fun1 将高24位删除,函数fun2 对于0xaaaaaabc的b的取值相关,如果的b大于8的 返回值的为0xffffffbc
#### practice 2.27 p81
int uadd_ok(unsigned x, unsigned y){
    return (x>>31)==1&&(y>>31)==1?1:0;
}
