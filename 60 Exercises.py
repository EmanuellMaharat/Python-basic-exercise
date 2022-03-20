#1 Write a Python program to print the following string in a specific format
print ( "Twinkle, twinkle, little star, "
        "\n\tHow I wonder what you are! \n\t\tUp above the world so high, "
        "\n\t\tLike a diamond in the sky.\n Twinkle, twinkle, little star,"
        " \n\tHow I wonder what you are")

#2 print python version
import sys
print("python version")
print(sys.version)

#3 print date
import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%M-%D"))

#4 last name and name with spaces
name = input ("name?")
lastname= input("lastname?")

print (lastname+ " " +name)

#5 print first and last color from list
color_list = ["Red","Green","White" ,"Black"]
print((color_list[0],color_list[-1]))

#6 n as 5
num = int(input("Enter a num"))
num1 = int("%s"%num)
num2 = int("%s%s"%(num,num))
num3 = int("%s%s%s"%(num,num,num))
print (num3+num1+num2)

#7 program to display the examination schedule
exam_st_date = (11, 12, 2014)
print (f"The examination will start from: %d/ %d/ %d "%exam_st_date)

#8 program to print the calendar of a given month and year
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

#9 print sample string
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

#10 calculate number of days between two dates
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
minus = l_date - f_date
print(minus.days)

#11program to get the difference between a given number and 17,
#if the number is greater than 17 return double the absolute difference.
def minus (n) :
    if n <= 17 :
        return(17-n)
    else:
        return (17-n)*2

print(minus(10))
print(minus(17))

#12 print num is 100 , 1000 , 2000
num = int(input("Enter a num"))
if num == 100:
        print ("It's 100")
if num == 1000:
        print ("It's 1000")
if num == 2000:
        print ("it's 2000")

#13  if the values are equal then return three times of their sum
def plus(num1, num2, num3):
    d = num1 + num2 + num3
    if num1 == num2 == num3:
        print(d * 3)
    return d
print(plus(3, 3, 3))

#14 get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged
def string(ok):
    if len(ok) >= 2 or ok[:2] == "ls":
        return ok
    return "is" + ok

print(string("ok"))
print(string("lsok"))

#15 check if given num is even or odd
num = int(input("enter a num : "))
if num % 2 == 0:
        print("This is an even number.")
else:
        print("This is an odd number.")

#16 program to count the number 4 in a given list
def list_four (nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
    return count
print(list_four ([1,2,4,5,4,4]))

#17 check whether a specified value is contained in a group of values
def list_true_false (nums,n):
    for num in nums:
        if n == num :
            return True
        print(list_true_false([1, 3, 5, 6, 7, 4]))

#18 program to print all even numbers from a given numbers list in the same order
# and stop the printing if any numbers that come after 237 in the sequence
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 743, 527
]

for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)

#19 area of triangle
base = float(input("base?"))
height = float(input ("height?"))
total = (int(base) * int(height))
print (int(total/2))

#20  program to print out a set containing all the colors from color_list_1
# which are not present in color_list_2
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(f"Diffrence from list 1 to list 2{color_list_1.difference(color_list_2)}")
print(f"Diffrence from list 2 to list 1{color_list_2.difference(color_list_1)}")




