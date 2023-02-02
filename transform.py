def get_factors(x):
    print("The factors of",x,"are:")
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    
    return factors

text = input('Enter plain text ():')
text = text.lower()
text = text.replace(' ', '')

length = len(text)

factor = get_factors(length)
print(factor, len(factor))

encryption_matrix = []
row = factor[len(factor) // 2 - 1 if len(factor) % 2 == 0 else len(factor) //2]
col = factor[len(factor) // 2] if len(factor) % 2 == 0 else row 


count = 0
for i in range(row):
    temp_matrix = []
    for j in range(col):
        temp_matrix.append(text[count])
    count += 1
    encryption_matrix.append(temp_matrix)

for e_row in encryption_matrix:
    print(e_row)
    str = ""
    for i in range(col):
        for row in encryption_matrix:
            str += row[i]
 
print(str)

