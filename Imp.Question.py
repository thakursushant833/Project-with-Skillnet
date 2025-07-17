# Input_string=“aaabbbcccdddee”
# Expected output = 
# A= 3 
# B=3
# C=3 
# D=3 
# E=2

input_string = "aaabbbcccdddee"
input_string = input_string.upper()
count={}

for letter in input_string:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1
for letter in count:
    print(letter + "= " + str(count[letter]))
