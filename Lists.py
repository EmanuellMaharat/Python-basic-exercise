#1 I love python 5 times
for i in range (5):
    print ("i love python")

#2 creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))

for i in range(0, n):
    list = int(input())

    lst.append(list)  # adding the element

print(lst)

#3
for i in range (11)
    n = int(input("please enter a num"))
    ls.append(n)
    for i in LS :
        x=i/11
        divided_11.append(x)
        if i%2==0:
            even_nums.append(i)
        if i%3==0 :
            divided_3+=1
        if i>10 :
             bigger_10+=1
        if i<10:
             lower_10 +=1

#4 Python code to check if 2 numbers are same
def areSame(a, b):
	if (not(a - b)):
		print ("Same")
	else:
		print ("Not Same")
# Driver code
areSame(20, 20)

#5 grage for 2 students
Emanuel = []
Dana = []
for i in range (5):
    Emanuel.append(int(input("please enter your grade")))
    Dana.append(int(input("please enter your grade")))
for i in range (len(Emanuel)):
    for j in range (len(Dana)):
        if Emanuel(j)==Dana(i):
            print (Emanuel(i))

#6 Check if string is Even or Odd
name = input("Enter your name: ")
length = len(name)%2
if length == 0:
	print (name, "even")
else:
	print (name, "odd")

#7
for i in range (100):
	Client = input("What is your name ?")
	order = int(input("How much do you need?"))
	minimum = 4
	one_box = 35
	if order < int(minimum):
		print(order * one_box + 10)
	else:
		print(f'Thank you', Client, ' for your order', (one_box * 2), 'ILS')
		if order > 20 :
			print (f'thank you',(Client) )

#8
family = []
kids = []
for i in range(2):
	q1 = input('Name:')
	q2 = int(input('Kids?:'))
	family.append(q1)
	kids.append(q2)
for i in kids:
	if i > 3:
		print('Discount')
print(family, kids)

#9
blood_type= []
name =[]
Bloodtype = "o"
counter_O = 0
for i in range (3):
	q1 = input('Name:')
	q2 = input('blood_type:')
	name.append(q1)
	blood_type.append(q2)
for i in blood_type:
	if i == Bloodtype:
		counter_O +=1
print(name)
print(blood_type)
print('Amount of people with O :', counter_O)




