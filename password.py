from crypto import pwd_context
from database import *

# hashing a password...
#email = input("enter your email: ")
#realPass = input("set your password:  ")
#hashed = pwd_context.hash(realPass)
#setUserPassword(email, hashed)
#print("stored")

# verifying a password...
testPass = input("enter your password:  ")
dbPass = getUserPassword()
print(pwd_context.verify(testPass, dbPass))
