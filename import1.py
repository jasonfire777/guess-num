import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1 #just count = count +1
	num = input('請猜一個數字，1-100: ')
	num = int(num)
	if num == r:
		print('你猜對了!')
		print('你已經猜了第', count,'次')
		break
	elif num > r:
		print('比答案大了')
	elif num < r:
		print('比答案小了')
	print('你已經猜了第', count, '次')