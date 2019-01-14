import random
s = input('請決定你要猜的隨機數字範圍的開頭：')
f = input('請決定你要猜的隨機數字範圍的結尾：')
s = int(s)
f = int(f)
r = random.randint(s, f)
count = 0
while True:
	count += 1 #just count = count +1
	num = input('請範圍內猜一個數字: ')
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