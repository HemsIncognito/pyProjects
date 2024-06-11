# Random Passsowrd Generator 
# importing modules
import string
import random

# choosing a random characters_number for generating password
num = random.randint(8,15)

# store all characters in lists 
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# shuffle all lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)


# calculate 
x1 = round(num * random.uniform(0.3,0.35))
x2 = round(num * random.uniform(0.2,0.3))
x3 = round(num * random.uniform(0,0.15))
x4 = num - (x1 + x2 + x3)
lst = [x1, x2, x3, x4]
random.shuffle(lst)
upper_part = lst[0]
lower_part = lst[1]
digits_part = lst[2]
symbols_part = lst[3]

# generation of the password with random characters
result = []

for x in range(upper_part):
    result.append(s1[x])
for x in range(lower_part):
	result.append(s2[x])
for x in range(digits_part):
	result.append(s3[x])
for x in range(symbols_part):
	result.append(s4[x])


# shuffle result
random.shuffle(result)
random_password = "".join(result)
# printing the result
print("Strong Password: ", random_password)
