#1 uneven numbers from 1-20 while loop
maximum = int(input(" Please Enter the Maximum Value : "))

number = 1

while number <= maximum:
    if(number % 2 != 0):
        print("{0}".format(number))
    number = number + 1

#2 uneven numbers from 1-20 for loop
maximum = int(input(" Please Enter any Maximum Value : "))

for number in range(1, maximum + 1):
    if(number % 2 != 0):
        print("{0}".format(number))
