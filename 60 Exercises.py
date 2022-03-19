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

