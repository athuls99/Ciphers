def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
def encrypt(text,k,b):
    # y = (kx + b) mod 26
    res ="";
    for i in text:
        val = ord(i)
        if(val != 32):
            val = val - 65
            y = ((k*val) + b)%26
            res = res + chr(y+65)
        else:
            res += " "
    print(res)
def decrypt(text,k,b):
    # x= s(y-b)mod 26
    # where s is the modulo inverse of k
    res ="";
    for i in range(1,26):
        if((k*i)%26 == 1):
            minv = i
            break;
    for i in text:
        val = ord(i)
        if(val != 32):
            val = val- 65
            val = val - b
            val = (minv*val)%26
            res += chr(val + 65)
        else:
            res += " "
    print(res)
print("Enter the value of multiplicative costant(Key 1,should be a co-prime of 26)");
k = int(input())
while(gcd(k,26) != 1):
    print("Invalid value,please enter a co-prime of 26")
    k = int(input())
print("Enter the value of additve constant(Key 2)")
b = int(input())
print("Enter 0 to encrypt and 1 to decrypt")
m = int(input())
if(m==0):
    print("Enter the plain text")
    text = input()
    text = text.upper()
    encrypt(text,k,b)
elif(m==1):
    print("Enter encrypted text");
    text = input()
    text = text.upper()
    decrypt(text,k,b)
