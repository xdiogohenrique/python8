a = int (input("Insira o valor do A: "))
b = int (input("Insira o valor do B: "))
c = int (input("Insira o valor do C: "))

if not ((b < c) and (b < a)):
    print("O B é menor do que o A e C")
else:
    print("O B é maior")