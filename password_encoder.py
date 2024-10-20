password = (input('Enter your password: '))

for char in password:
    x = int(char) + 13
    x = str(x)
    print(x[1], end = '')

