#assowrd = '123456'
x = 3
while x <= 3 and x > 0:
	passwprd = input('請輸入密碼:')
	if passwprd == 'a123456':
		print('登入成功')
	else:
		x = x - 1
		if x == 0:
			break
		print('密碼錯誤還有', x,'次機會')

