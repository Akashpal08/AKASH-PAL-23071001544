a=int(input("Enter a long number : "))
b=a
sum=0
count=0
rem=0
rem2=0
while (a!=0):
  rem=a%10
  a=a//10
  count+=1

if (count<=6):
    while (a>0):
     rem2=a%10
     sum=sum+rem2
     a=a//10
    
    print(sum)
else:
  print("only 6 digit")
