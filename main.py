import random

password_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_length = int(input("Введите нужную длину пароля: "))

generated_password = ""

for i in range(password_length):
    generated_password += random.choice(password_characters)

print("Сгенерированный пароль:", generated_password)