#### PROJETO ASSISTENTE ####

#### MENU PRINCIPAL ####
import json
inicio = "1"
while inicio == "1":

    bolean = input("Deseja modificar a pesagem de algum ingrediente? (admita 1 = sim e 0 = não):  ")
    inicio = "0"

## INTEREÇÃO COM OS PRODUTOS ##
    if bolean == "1":
        print("voce respondeu sim")
        procura = input("Qual ingrediente gostaria de modificar a pesagem?:  ")

        procura = procura.lower()

        if procura == "arroz":
            arrozP = input("Peso do arroz em grama: ")
            
            inicio = "1"

        if procura == "feijao":
            json.loads(estoque)
             feijao = input("Peso do feijão em grama: ")

             y0 = json.dumps(estoque[feijao])
            
            inicio = "1"
            
       
## INTERAÇÃO COM O ESTOQUE ##
    if bolean == "0":
        print("você respondeu não")
        acess = input("gostaria de acessar o estoque?:  ")
        if acess == "1":
            estoque = {"arroz": 0, "feijao": 0 }
            #data = json.dumps(estoque)
            print(estoque)
            
            
            
            inicio = "1"
        
        else:
            inicio = "1"



































