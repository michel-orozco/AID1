# For númerico
for x in range(10):
    print(x+1)

for x in range(5, 11):
    print(x)

for x in range(5, 11, 2):
    print(x)

# While
i = 1
while i<6:
    print(i)
    i+=1

# Uso de break
i = 1
while i<6:
    if i==3:
        break
    print(i)
    i+=1

for x in range(10):
    if x>5:
        break
    print(x+1)
