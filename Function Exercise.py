def divided(num1, num2):
    d = num1 / num2
    return d

def plus(num1, num2):
    d = num1 + num2
    return d

def multiply(num1, num2):
    d = num1 * num2
    return d

def minus(num1, num2):
    d = num1 - num2
    return d

q1 = int(input("please choose a number"))
q2 = int(input("please choose another number"))
q3 = input("do you want * + - /")
if q3 == "/":
    print(f'The answer is , {divided(q1,q2)}')
if q3 == "+":
    print(f'The answer is {plus(q1,q2)}')
if q3 == "*":
    print (f"The answer is {multiply(q1,q2)}")
if q3 == "-":
    print (f"The answer is {minus(q1,q2)}")
else:
    print ("please choose arithmetic signs")


