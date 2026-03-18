import os 
import time
os.system("cls")

soma = 0
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
      
      nota = float(input(f"Digite primeira nota: "))
      media = soma + nota
      break
if nota >= 0 and nota <= 10:
        soma += nota
    
else:
      print("nota invalida.")
      print("Tente novamente...\n")

media =  soma / QUANTIDADE_NOTAS

if nota >= 7:
     resultado = "Aprovado"
elif media >= 5:
     resultado = "Recuperação"
else: 
     resultado = "Reprovado"

print(f"Media: {media}")
print(f"Resultado: {resultado}")
