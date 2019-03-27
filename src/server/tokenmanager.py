import random
import string

def compare(token):
    if token == getToken():
        return True
    return False

def getToken():
    #? Get Token From File
    tokenfile = open("./src/scripts/core/script.token", "r")
    token = tokenfile.read()
    resetToken()
    return token
    
def resetToken():
    #? Reset Token In File
    tokenString = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    tokenfile = open("./src/scripts/core/script.token", "w")
    tokenfile.write(tokenString)