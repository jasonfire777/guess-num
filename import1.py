import random
r = random.randint(1, 100)
while True:
	num = input('請猜一個數字，1-100: ')
	num = int(num)
	if num == r:
		print('你猜對了!')
		break
	elif num > r:
		print('比答案大了')
	elif num < r:
		print('比答案小了')