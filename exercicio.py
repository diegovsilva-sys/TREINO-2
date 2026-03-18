import os 
os.system("cls")

soma = 0
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    while True: 
      nota = float(input("Digite a {i+1} nota: "))

    if nota >= 0 and nota <= 10:
        soma += nota
        break
    else:
        print("Nota invalida.")
        print("Tente novamentre...\n")

media = soma / QUANTIDADE_NOTAS

print(f"Media: {media}")
