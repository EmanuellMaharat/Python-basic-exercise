#1 uneven numbers from 1-N while loop
maximum = int(input(" Please Enter the Maximum Value : "))

number = 1

while number <= maximum:
    if(number % 2 != 0):
        print("{0}".format(number))
    number = number + 1

#2 Number squared
num = int (input ("please enter a number"))
print (num**2)

#3 Age of given person + 20 years
age = int(input("how old are you"))
print ('you will be in 20 years')
print (age + 20, )

# 4 price of product + 17%
Full_price = int(input ("show me the price +17% "))
print (Full_price * 1.17)

# 5 Plus , Divide , addition , Multilpication
num1 = int(input ("Please Enter a number"))
num2 = int(input("please enter another number"))
print (num1 + num2 , num1-num2 , num1 * num2 , num1/num2 )

# 6 Welcome + Date
import datetime
now = datetime.datetime.now()
x = input("welcome")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#7 Avg of 4 given numbers
num1 = int (input("please enter first number "))
num2 = int (input("please enter second number "))
num3 = int (input("pl)ease enter third number "))
num4 = int (input("please enter fourth number "))
avg = (num4+num2+num3+num1)/4
print (avg)

#8 km\h how much time it will take
s=int(input('total speed:'))
d=int(input('total distance:'))
print(f'{s/d} hour')
print (f"{s/d*60} in minutes")

#9 Multiplication table (from 1 to 10) in Python w
num = 10
for i in range(1, 11):
   print(num, i, num*i)


#10 Multiplication table (from 1 to 10) in Python with spaces
num = 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

#11 AVG of 5 numbers
num1 = int (input("please enter first number "))
num2 = int (input("please enter second number "))
num3 = int (input("pl)ease enter third number "))
num4 = int (input("please enter fourth number "))
num5 = int (input("please enter fourth number "))
avg = (num4+num2+num3+num1)/5
print (avg)

#12 Guess number from 1 - 100
import random

num = random.randint(1, 100)
guess = None

while guess != num:
    guess = input("guess a number between 1 and 100: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")

#13 sum of 13 numbers
sum = 0
for i in range(1,14):
  sum = sum + i
print("Sum is ", sum)














