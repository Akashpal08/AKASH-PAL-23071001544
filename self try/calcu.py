number = float(input("Enter Number: "))
number2 = float(input("Enter Number: "))
op = input()

match op:
    case "+":
        print(number + number2)
    case "-":
        print(number - number2)
    case "*":
        print(number * number2)
    case "/":
        print(number / number2)
    case "_" : 
        print("Not valid")