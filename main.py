import json
with open('estoque.txt') as dados:
    json_data = json.load(dados)


inicio = "1"
while inicio == "1":

    bolean = input("Deseja modificar a pesagem de algum ingrediente? (admita 1 = sim e 0 = não):  ")
    inicio = "0"

    if bolean == "1":
        print("voce respondeu sim")
        procura = input("Qual ingrediente gostaria de modificar a pesagem?:  ")

        procura = procura.lower()

        if procura == "arroz":
            arrozP = input("Peso do arroz em grama: ")
            
            inicio = "1"

        elif procura == "feijao":
            feijaoP = input("Peso do feijão em grama: ")
            
            inicio = "1"
            
       

    else:
        print("você respondeu não")
        acess = input("gostaria de acessar o estoque?:  ")
        if acess == "1":
            estoque = {"arroz": arrozP, "feijao": feijaoP }
            print(estoque)
            
            
            
            inicio = "1"
        
        else:
            inicio = "1"


#j = json.loads('{"Nome": "Fulano", "Idade": "23"}')
#j['Idade'] = '12'


#with open('estoque.txt', 'a') as dados:
#                dados.write(json.dumps(str(estoque)) + '\n')




































