def verificar_revisao(quilometragem_atual): 
    limite_revisao = 1000
    if quilometragem_atual >= limite_revisao: 
        return "ALERTA: Agendar revisão na oficina imediatamente!" 
    else: km_restantes = limite_revisao - quilometragem_atual
    return f"Tudo certo, Faltam {km_restantes} km para a proxima revisao."
print("Diagnostico do Opala:", verificar_revisao(10500))
print("Diagnostico do Maveric:", verificar_revisao(8200))
print("Diagnostico da caminhonete:", verificar_revisao(10000))