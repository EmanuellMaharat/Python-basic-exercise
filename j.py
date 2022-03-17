for i in range (2):
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
			print (sum)
