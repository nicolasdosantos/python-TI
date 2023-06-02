total = 0
for i in range(5,11):
    if i %7 == 0 and i %5 !=0:
        print(i)
        total += 1
print(f"A quantidade total de numeros é {total}")