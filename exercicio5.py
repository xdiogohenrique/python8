h      = float (input("Insira o valor da altura pirâmide:"))
bMenor = float (input("Insira o valor da base menor:"))
bMaior = float (input("Insira o valor da base maior:"))

v = (h/3)*(bMaior**2 + bMenor**2 +(bMaior**2 * bMenor**2)**0.5)

print("O volume é", v)