agua     = float(input("Insira o valor da sua conta de água:"))
luz      = float(input("Insira o valor da sua conta de luz:"))
telefone = float(input("Insira o valor da sua conta de telefone:"))

salario  = float (input("Insira o valor do seu salário mensal:"))

total      = agua+luz+telefone
totalResto = salario-(agua+luz+telefone)

if salario < total: 
    print("Salário insuficiente!")
else: 
    print("O seu saldo é",totalResto)
