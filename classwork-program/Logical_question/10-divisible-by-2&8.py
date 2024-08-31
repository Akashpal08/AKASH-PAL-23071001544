# 10 - WAP TO TAKE INPUT FROM USER AND CHECK IT IS DIVISIBLE BY 2 AND 8.
a=int(input("Enter a Number : "))
if a==0:
    print("Zero is not Divisible by both 2 & 8")
elif (a%2 & a%8==0):
    print("Yes This Number is Divisible by both 2 & 8")
#elif a<0:
    #print("The Number is Invalid")'''
else :
    print("No This Number is Not be Divisible by both 2 & 8")