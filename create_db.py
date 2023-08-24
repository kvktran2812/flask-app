from flaskr.generator.create_data import *


f_name = create_names("first_name.txt", 10)
l_name = create_names("last_name.txt", 10)
print(f_name)
print(l_name)

for first, last in zip(f_name, l_name):
    print(create_username(first, last), create_email(first, last))

