import random, string

def generate_random_token(tokenLength):

    while(True):
        token = ''.join(random.choices(string.ascii_letters +
                                string.digits, k=tokenLength))

        tokenList = load_tokens("tokens.txt")
        if token not in tokenList:
            save_tokens(token, "tokens.txt")
            break

    return token

def save_tokens(token, tokenFile):
    with open(tokenFile, "a") as f:
        f.write(token+"\n")
    f.close()

def load_tokens(tokenFile):
    tokenList = []

    with open(tokenFile, "r") as f:
        for line in f:
            token = line.strip()
            tokenList.append(token)
    f.close()

    return tokenList

#Main
