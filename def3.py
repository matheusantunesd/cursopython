def processo_boletim(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) /3

    if media >= 6.0:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"

    return media, situacao,
media_aluno,status_aluno = processo_boletim(7.5, 5.0, 8.0)

print(f"Resultado Final: Media {media_aluno:.1f} -> Status: {status_aluno}")