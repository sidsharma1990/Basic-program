'''Replace method'''

phone_number = "555 555 1234"
print(phone_number.replace(" ", "-"))
print(phone_number.replace("5", "9"))
print(phone_number)

phone_number = phone_number.replace(" ", "-")


'''Starts with and endswith'''

salutation = "Mr. Kermit the Frog"

print(salutation.startswith("M"))
print(salutation.startswith("Mr"))
print(salutation.startswith("Mr."))
print(salutation.startswith("m"))
print(salutation.startswith("mr."))
print(salutation.startswith("Ker"))
print(salutation.startswith("Mr. Ker"))

print()

print(salutation.endswith("g"))
print(salutation.endswith("og"))
print(salutation.endswith("Frog"))
print(salutation.endswith("frog"))
