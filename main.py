
inicio = "1"
while inicio == "1":

    bolean = input("Deseja modificar a pesagem de algum ingrediente? (admita 1 = sim e 0 = não):  ")
    inicio = "0"

    if bolean == "1":
        print("voce respondeu sim")
        procura = input("Qual ingrediente gostaria de modificar a pesagem?:  ")

        if procura == "arroz" or "Arroz" or "ARROZ":
            arrozP = input("Peso do arroz em grama: ")
            inicio = "1"

        elif procura == "feijão" or "feijao" or "Feijão" or "Feijao" or "FEIJÃO" or "FEIJAO":
            feijaoP = input("Peso do feijão em grama: ")
            inicio = "1"

        

    else:
        print("você respondeu não")
        acess = input("gostaria de acessar o estoque?:  ")
        if acess == "1":
            estoque = {"arroz": arrozP, "feijão": feijaoP }
            print(estoque)
            inicio = "1"





































