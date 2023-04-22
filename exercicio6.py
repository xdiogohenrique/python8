from cmath import pi
import math

graus = float (input("Insira o valor dp grau:"))

radianos = graus * math.pi / 180

print("O valor convertido para radianos é ", radianos)

print("O valor do cosseno é ", math.cos(graus))
print("O valor do tangente é", math.tan(graus))
print("O valor do seno é", math.sin(graus))