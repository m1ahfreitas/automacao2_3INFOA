valoru = []

while True: #repete para sempre
    valor = input("Digite preço unitaário do produto: ")
    
    valoru.append(valor) #adiciona o nome na lista
     
    
    if valor == "=": #se o nome for igual a fim
        print(valoru)
        valortotal = valortotal + int(valor) 
        print (valortotal)
        break     
    






