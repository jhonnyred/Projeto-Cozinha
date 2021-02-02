#### PROJETO ASSISTENTE ####

#### MENU PRINCIPAL ####
import pickle
receituario = {}
estoque = pickle.load(open("estoque.pkl", "rb"))
inicio = "1"
while inicio == "1":
    print(" M para modificar o estoque")
    print(" V para visualizar o estoque")
    print(" A para apagar o produto em estoque")
    print(" R para o menu de receitas")
    print(" Q para fechar programa")
    menu = input("\n O que deseja fazer? ").upper()
    
    ## MENU PARA MODFIICAR ESTOQUE ##
    if menu == "M":
        procura = input("Qual modificação deseja fazer?:  ")

        procura = procura.lower()

        if procura in estoque:
            estoque[procura] = input("identifique a quantia: ")


        else:
            estoque[procura] = input("identifique a quantia: ")

    ## QUITAR PROGRAMA ##
    if menu == "Q":
        inicio = "0"

    ## APAGAR PRODUTO ##
    if menu == "A":
        produto = input("Qual produto deseja apagar? ").lower()

        if produto in estoque:
            del estoque[produto]

    pickle.dump(estoque, open("estoque.pkl", "wb"))

    ## MENU DE RECEITAS ##
    if menu == "R":
        print(" E para escrever uma receita")
        print(" L para livro de receitas")
        print(" M para modificar alguma receita")

        Rmenu = input("\n escolha uma opção: ").upper()

        if Rmenu == "E":
            
            newre = input(" Qual receita gostaria de adicionar? ").upper()

            if newre in receituario:
                print("\n Essa receita ja existe, se necessário modifique suas receitas\n ")
                menu == "R"
                
            else:
                receituario[newre] = {}
                
                while True:
                    b = input("\n deseja prosseguir? (S/N) ").upper()
                    
                    if b == "S":
                        ingred = input(" Digite o ingredite: ").lower()
                        receituario[newre][ingred] = input(" Coloque o montate necessário: ").lower()
                      
                    else:
                        break
        if Rmenu =="M":
            procura2 = input(" Qual receita deseja modificar? ").upper()

            if procura2 in receituario:
                print("\n")
                print(receituario[procura2])
                print("\n")

                while True:
                    c = input(" Deseja continuar? (S/N)").upper()

                    if c == "S":
                        procura3 = input(" Qual ingrediente gostaria de modificar? ").lower()

                        if procura3 in receituario[procura2]:
                            receituario[procura2][procura3] = input(" identifique a quantia: ").lower()

                        else:
                            print( "\n Esse ingrediente não está nessa receita\n ")
                            
                    else:
                        break

                    
                    



            else:
                print("\n Essa receita não existe\n ")
                menu == "R"


        if Rmenu =="L":
            print("\n")
            print(receituario)
            print("\n")


                        
    ## vISUALIZAÇÃO ##
    if menu == "V":
        print("\n visualização de estoque\n ")
        print(estoque)


































