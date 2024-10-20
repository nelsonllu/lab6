from password_encoder import encode
from password_decoder import decode
#import decoder

while True:
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
    option = input('Please enter an option: ')
    if option == '1':
        password = input('Please enter your password to encode: ')
        encoded_password = encode(password)
        print('Your password has been encoded and stored!')
    if option == '2':
        decoded_password = decode(encoded_password)
    if option == '3':
        break
