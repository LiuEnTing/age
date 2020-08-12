password = 'a123456'
i = 3

while i > 0 :
	i = i - 1
	pwd = input('請輸入密碼，最多三次:')
	if password == pwd:
		print('密碼正確')
		break
	else :
		print('輸入錯誤請重新輸入，不要再亂試')
		if i > 0:
			print('還有',i,'次機會')
		