'''Strip methods'''

empty_space = "          content                "
'''Right Strip'''
print(empty_space.rstrip())
print(len(empty_space.rstrip()))
'''left Strip'''
print(empty_space.lstrip())
print(len(empty_space.lstrip()))

print(empty_space.strip())
print(len(empty_space.strip()))

website = "www.python.org"

print(website.lstrip("w"))
print(website.rstrip("org"))
print(website.strip("worg."))


'''Replace Method'''
phone_number = "555 555 1234"
print(phone_number.replace(" ", "-"))
print(phone_number.replace("5", "9"))
print(phone_number)

phone_number = phone_number.replace(" ", "-")