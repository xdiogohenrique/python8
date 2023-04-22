valorCompra = float(input("Insira o valor de sua compra:"))

valorDesconto = valorCompra-(valorCompra*0.2)

if valorCompra >= 200:
    print ("O Valor da sua compra é", valorCompra, "e seu desconto é de", valorDesconto)
else:
    print("O Valor da sua compra é", valorCompra)    