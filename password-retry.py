x = 3
while  x > 0:
	x = x - 1
	passwprd = input('請輸入密碼:')
	if passwprd == 'a123456':
		print('登入成功')
		break
	else:
		print('密碼錯誤還有', x, '次機會')
		if x == 0:
			print('密碼錯誤次數過多帳號已被鎖定!!!')
			break
		

