#0 Calculatur by choise
def divided(divided1, divided2):
    d = divided1/divided2
    return d

def plus(plus1,plus2):
    d = plus1+plus2
    return d

def multiply(multiply1 , multiply2):
    d = multiply1 * multiply2
    return d

def minus(minus1 , minus2):
    d = minus1-minus2
    return d

q1 = int(input("please choose a number"))
q2 = int(input("please choose another number"))
q3 = input("do you want * + - /")
if q3 == "/":
    print(f'The answer is {divided(q1,q2)} \U0001F600 ')
if q3 == "+":
    print(f'The answer is {plus(q1,q2)} \U0001F910')
if q3 == "*":
    print (f"The answer is {multiply(q1,q2)} \U0001F602")
if q3 == "-":
    print (f"The answer is {minus(q1,q2)} \U0001F605")


#1 print 1 if the number is even and 0 if it's odd

def even(number):
    q1 = int(input("please choose a number"))
    if q1 % 2 == 0:
		
#35 save names
def save_user(**user):
    print (user)

save_user(id=1, name="john", age=22)

#36 list of numbers
def list(*numbers):
    print(numbers)

list(2,3,4,5)


#37 Multiply numbers
def Multiply(num1, num2):
    return num1 * num2

print(Multiply(2, 3))


#38 print first and last name
def greet(first_name , last_name)
    print (f"Hi {first_name}{last_name}")
    print ("Welcome")

greet(Emanuel,maharat)

#39 addition
def addition(num1, num2):
    return num1 + num2

print(addition(2, 3))

#40 addition
def divided(num1, num2):
    d = num1 + num2
    return d

s = (divided (2, 3))
print (s)


#41 divided
def divided(num1, num2):
    d = num1 / num2
    return d

s = (divided (2, 3))
print (s)

        print(number)
    else:
        print(0)
even(1)

#2 input n num and print the avarege
def Average(lst):
	return sum(lst) / len(lst)

lst = [15, 9, 55, 41, 35, 20, 62, 49]
average = Average(lst)

print("Average of the list =", round(average, 2))

#3 Return the sum len of string

def lan (lst) :
    l=("Emanuel")
    return l
x= (len(lan(lst)))
print ("The len of the list=", x)
