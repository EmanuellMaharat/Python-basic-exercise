#1 uneven numbers from 1-N for loop - If statements
maximum = int(input(" Please Enter any Maximum Value : "))

for number in range(1, maximum + 1):
    if(number % 2 != 0):
        print("{0}".format(number))
#2 I in range 100,500 stop at 287 -If statements
for i in range(100, 500):
    if i == 287:
        print("287")


#3 Print number from 1-20 without number 13 - If statements
for i in range(10, 20):
    if i != 13:
        print(i)
#4 40 match in box - If statements
i = int(input("please enter a number of match "))
if i > 40:
    print(i / 40)
else:
    print(1)
