# 猜數字

import random
start = input('請決定隨機數字範圍的起始值: ')
end = input('請決定隨機數字範圍的結束值: ')
start = int(start)
end = int(end)
ans = random.randint(start, end)
count = 0
while True:
	count += 1
	guess = input('請輸入你的數字: ')
	guess = int(guess)
	if guess == ans:
		print('你猜中了!')
		print('這是你猜的第', count, '次!')
		break
	elif guess > ans:
		print('比答案大')
	else:
		print('比答案小')
	print('這是你猜的第', count, '次!')