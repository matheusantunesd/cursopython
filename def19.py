tempo_voltas = []

print("--- Registro de Tempos: Stock Car ---")
for i in range (5):
    tempo = float(input(f"Digite o tempo da voltas {i+1} (em segundos):"))
    tempo_voltas.append(tempo)


melhor_tempo = min(tempo_voltas)  

posição_melhor = tempo_voltas.index(melhor_tempo) + 1

media_tempo = sum(tempo_voltas) / len(tempo_voltas)

print (f"O melhor tempo foi de {melhor_tempo} segundos")
print (f"A posição melhor é de {posição_melhor}")
print (f"Media foi de {media_tempo} segundos")