n=int(input("Enter a long number : "))
count=0
rev=0
rem=0
while (n>0):
    rem=n%10
    n=n//10
    count+=1
    rev=rev*10+rem
print(rev)