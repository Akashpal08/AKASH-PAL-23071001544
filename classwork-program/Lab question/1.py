a=int(input("How many digit summ you have find : "))
sum=0
if a>0:
    for i in range(a):
          i=int(input("enter a number : "))
          sum=sum+i
    print(sum)
else:
     print("invalid number")