def calcular_dano(ataque_base, multiplicador, foi_critico):
     if foi_critico == True:
        dano_total = ataque_base * multiplicador
        return f" ACERTO CRITICO! Voce causou {dano_total}.de dano no chefao!"
     else:
         return f"Acerto normal. Voce causou {ataque_base} de dano"





ataque_1 = calcular_dano(50, 2,5, False)
ataque_2 = calcular_dano(50, 2.5, True)

print(ataque_1)
print(ataque_2)