x = 1 
y = 2
print('最多輸入3次密碼')
while x <= 3 and y >= 0:
    password = input('請輸入密碼:')
    if password == 'a123456':
    	print('登入成功')
    	break
    elif password != 'a123456':
    	print('密碼錯誤', '還有', y , '次機會')
    	x = x + 1
    	y = y - 1
while x >= 3 and y <= 0:
    	print('登入失敗')
    	break
    