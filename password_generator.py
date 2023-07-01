import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


let = int(input("How many letters would you like in your password? "))
sym = int(input("How many symbols would you like in your password? "))
num = int(input("How many numbers would you like in your password? "))

password = ""
 
for i in range(1,let +1):
    password += random.choice(letters)
    

for i in range(1,sym +1):
    password += random.choice(symbols)
  
for i in range(1,num +1):
    password += random.choice(numbers)
    
passlist = []
for i in range(0,len(password)):
    passlist += password[i]
  
random.shuffle(passlist)
password=""
for each in passlist:
    password += each

print(password)