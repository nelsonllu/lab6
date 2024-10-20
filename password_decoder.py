#rishi gandhi

def decode(password):
    decoded_password = ""
    for char in password:
        digit = (int(char) - 3) % 10
        # Append the decoded digit to the result
        decoded_password += str(digit)
    return decoded_password
