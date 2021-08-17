# 猜數字

import random
ans = random.randint(1, 100)
while True:
	guess = input('請輸入你的數字: ')
	guess = int(guess)
	if guess == ans:
		print('你猜中了!')
	elif guess > ans:
		print('比答案大')
	else:
		print('比答案小')