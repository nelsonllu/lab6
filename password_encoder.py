def encode(password):
    for char in password:
        x = int(char) + 13
        x = str(x)
        print(x[1], end = '')

if __name__ == '__main__':
    password = input('Enter a password: ')
    encode(password)

