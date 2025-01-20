n=int(input("Enter a number:"))
m=n
r=0
while(n!=0):
    rem=n%10
    print(rem)
    r=r*10+rem
    n=(int)(n/10)
    print("Reverse of a string is:",r)
    if(m==r):
        print("It is a palendrome number")
    else:
        print("It is not a palendrome number")
