y = 3
print('最多輸入3次密碼')
while y > 0:
    y = y - 1
    password = input('請輸入密碼:')
    if password == 'a123456':
        print('登入成功')
        break
    else:
        if y > 0:
            print('密碼錯誤', '還有', y , '次機會')
        else:
            print('沒機會嘗試，鎖帳號了！')