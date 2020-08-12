
driving = input('請問有開過車嗎?')
if driving != '有' and driving !='沒有':
	print('不要亂回答87!')
	raise SystemExit

age = input('請輸入你的年齡')
age = int(age)

if driving == '有':
	if age >= 18:
		print('通過 請小心駕駛')
	else:
		print('你不是沒駕照嗎?')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照趕快去考')
	else:
		print('快可以考了 不要當三寶')
else:
	print('不要亂回答 87')
