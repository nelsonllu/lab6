#nelson lu
def encode(password):
    encoded = ""
    for char in password:
        x = int(char) + 13
        x = str(x)
        encoded += x[1]
    return(encoded)


