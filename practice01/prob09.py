# 문제9. 주어진 if문을 dict를 사용해서 수정하세요.

dic_menu = {'오뎅':300, '순대':400, '만두':500}

menu = input('메뉴: ')

if dic_menu.get(menu):
    print('가격: {0}'.format(dic_menu[menu]))
else:
    print('가격: 0')
