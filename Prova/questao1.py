
peso = input("Digite o peso da criança em quilogramas: ")
doserecomendada = input("digite a dose recomendada em mg por kg:")
conteudo = input("Digite o conteudo em ml : ")

dosetotal = int(peso) * int(doserecomendada) / int(conteudo)
quantidadegotas = int(dosetotal) * 20


print("A qauntidade de gotas para o medicamento é de: ", quantidadegotas)


