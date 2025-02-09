import random
a = ""
b = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
c = int(input("Escriba la longitud de la contraseña: "))

for i in range(c):
    a += random.choice(b)
print("Contraseña generada:", a)
 
