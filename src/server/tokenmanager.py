import random
import string


def init():
    open("./src/scripts/core/script.token", "w+").close()
    getToken()

def compare(token):
    return token == getToken()

def getToken():
    tokenfile = open("./src/scripts/core/script.token", "r")
    token = tokenfile.read()
    tokenfile.close()
    resetToken()
    return token
    
def resetToken():
    tokenString = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    tokenfile = open("./src/scripts/core/script.token", "w")
    tokenfile.write(tokenString)
    tokenfile.close()