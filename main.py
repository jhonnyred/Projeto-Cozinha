#### PROJETO ASSISTENTE ####

#### MENU PRINCIPAL ####
import pickle
estoque = pickle.load(open("estoque.pkl", "rb"))
inicio = "1"
while inicio == "1":
    print(" M para modificar o estoque")
    print(" V para visualizar o estoque")
    print(" A para apagar o produto em estoque")
    print(" R para o menu de receitas")
    print(" Q para fechar programa")
    menu = input("\n O que deseja fazer? ").upper()
    
    ## P (pesagem) ##
    if menu == "M":
        procura = input("Qual modificação deseja fazer?:  ")

        procura = procura.lower()

        if procura in estoque:
            estoque[procura] = input("identifique a quantia: ")


        else:
            estoque[procura] = input("identifique a quantia: ")

    if menu == "Q":
        inicio = "0"

    if menu == "A":
        produto = input("Qual produto deseja apagar? ").lower()

        if produto in estoque:
            del estoque[produto]

    pickle.dump(estoque, open("estoque.pkl", "wb"))

    if menu == "R":
        print(" E para escrever uma receita")
        print(" L para livro de receitas")
        Rmenu = input(" diz ai oq vc quer")

        if Rmenu == "E":
            


    ## RECEITAS ##        

       
    ## Visualização ##
    if menu == "V":
        print("visualização de estoque")
        print(estoque)



































