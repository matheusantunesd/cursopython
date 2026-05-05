notas = []

print("--- Sistema de Notas---")

for i in range(4):
    valor = float(input(f"Digite a nota {i+1}: "))
    notas.append(valor)

    media = sum(notas) / len(notas)

print(f"\nNotas digitadas: {notas}")
print(f"Media final: {media:.2f}")

if media >= 6:
    print("Resultado: Aprovado!")
else:
    print("Resultado; Recupeção.")