operator=input("Enter an operator (+ , - , * , /):")
num1=float(input("enter the first value:"))
num2=float(input("enter the second value:"))
if operator == "+":
    result=num1+num2
    print(result)
elif operator == "-":
    result=num1-num2
    print(result)
elif operator == "*":
    result=(num1*num2)
    print(round(result))
elif operator == "/":
    result=num1/num2
    print(round(result,5))
else:
    print("exit")