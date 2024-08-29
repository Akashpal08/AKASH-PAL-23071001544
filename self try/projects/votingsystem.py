age=int(input("Enter Your age = "))
if (age<=0):
 print("invalid input")
elif(age>=18):
 print("congulation you are eligible for vote")
else:
  print("you are not eligible for vote")
d=int(input("Enter your date of birth year : "))
if(d<0):
 print("invalid input")
a=int(input("enter your current year = "))
c=a-d
z=2000+c
print("you are eligible in %d year" %(z))