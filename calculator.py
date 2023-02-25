x=input("Напишите операцию (+, -, *, /): ")
a=float(input("1-е число = "))
b=float(input("2-е число = "))
if x == "+":
    resolt= a+b
elif x == "-":
    resolt=a-b
elif x == "*":
    resolt=a*b
elif x == "/":
    resolt=a/b
else:
    print("Нет такой операции")
print(resolt)