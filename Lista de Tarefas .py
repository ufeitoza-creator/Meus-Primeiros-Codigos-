lista_tarefas = ["planilha", "acionamentos Resseguros", ]
lista_tarefas.append("acompanhamento e-mail",)
lista_tarefas.append("cobrar pendencias em vermelho")
lista_tarefas.remove("planilha")
for item in lista_tarefas:
    print(f"fazer: {item}")
print(f"Total de tarefas: {len(lista_tarefas)}")