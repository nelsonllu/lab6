from password_encoder import encode
#import decoder

while True:
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
    option = input('Please enter an option: ')
    if option == '1':
        password = input('Please enter your password to encode: ')
        encoded_password = encode(password)
        print('Your password has been encoded and stored!')
    if option == '2':
        #decode encoded password
        #print msg
    if option == '3':
        break
