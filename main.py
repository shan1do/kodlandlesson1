import random
simbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
score = int(input("Количество символов в пароле "))
password = ""

for i in range(score):
    password += random.choice(simbol)
    
print(password)

