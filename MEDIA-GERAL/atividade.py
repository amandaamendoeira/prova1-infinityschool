alunos = int(input("Digite o número de alunos: "))
soma_medias = 0

for i in range(alunos):
    nome = input("Digite o nome do aluno: ")
    notas = [float(input(f"Digite a nota {j + 1} do aluno {i + 1}: ")) for j in range(3)]
    media = sum(notas) / 3
    
    if media >= 7:
        print("Aprovado")
    elif media < 7:
        print("Reprovado")

    soma_medias += media

media_geral = soma_medias / alunos
print(f"Média geral da turma: {media_geral:.2f}")