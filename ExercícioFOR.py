n = int(input("Digite um número natural: "))

#Verificando se o número é natural e se é igual a 1
if n <= 1:
  print("Não é um número primo")
else:
  is_prime = True

#Verificando se é primo
for i in range(2, n):
  if n % i == 0:
    is_prime = False
    break

if is_prime:
  print("É um número primo")
else:
  print("Não é um número primo")


