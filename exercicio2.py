turno = int (input("Insira o turno que você trabalha | 1 - para noturno e 2 - para Dia/Tarde:"))
horas = int (input("Insira quantas horas você trabalha:"))

valorNoturno = horas*45.00
valorDia = horas*37.50

if turno == 1: 
    print ("Seu salário é", valorNoturno)
else: 
    print ("Seu salário é", valorDia)
  