a = input()
b = ord(a)
if 65<= b <=90:
    print('{}(ASCII: {}) => {}(ASCII: {})'.format(a,b,a.lower(),ord(a.lower())))
elif 97<= b <=122:
    print('{}(ASCII: {}) => {}(ASCII: {})'.format(a,b,a.upper(),ord(a.upper())))
else:
    print(a)