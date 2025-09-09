import os
import pandas as pd

lavouras = [
    # {
    #     'cultura': 'cafe', 
    #     'area': 15129.0,
    #     'insumo': 'Calcio',
    #     'qnt_insumo': 12, 
    #     'qnt_litros': 181.548
    # },
    # {
    #     'cultura': 'milho', 
    #     'area': 65840.0,
    #     'insumo': 'Fosfato',
    #     'qnt_insumo': 75, 
    #     'qnt_litros': (75*65840)/1000
    # }
]

path_csv = "./output.csv"

while True:
    os.system('cls')

    print("===== FarmTech Solutions =====")
    
    print("1 - Inserir Dados")
    print("2 - Visualizar Dados")
    print("3 - Atualizar Dados")
    print("4 - Deletar Dados")
    print("5 - Sair")

    print("===============================")

    user = int(input("\nDigite a opção desejada:\t"))


    # Inserir dados
    if(user == 1):
        os.system('cls')

        cultura = input("Digite o nome da cultura:\t")
        comprimento = float(input("Qual o comprimento da lavoura? \t"))
        largura = float(input("Qual a largura da lavoura? \t"))
        ruas = int(input("Qual o numero de ruas existentes na lavoura?\t"))

        area = comprimento * largura

        area_total = area - (ruas * 0.5)    # De acordo com google, ruas de lavouras tem aproximadamente 0,5 metro

        insumo = input("Qual o insumo que pretende utilizar?\t")
        qnt_insumo = int(input("Qual a quantidade, em mL por metro, a ser pulverizada?\t"))

        qnt_litros = (qnt_insumo * area) / 1000

        
        print(f"\n\nSerá pulverizado ao todo {round(qnt_litros, 3)} litros de {insumo}, em todo os {area} m²")

        lavouras.append({
            "cultura":cultura,
            "area":area,
            "ruas":ruas,
            "insumo":insumo,
            "qnt_insumo":qnt_insumo,
            "qnt_litros":qnt_litros
        })

        if os.path.exists(path_csv):
            df = pd.read_csv(path_csv)

            df_novo = pd.DataFrame(lavouras)
            df_appended = pd.concat([df, df_novo], ignore_index=True)

            df_appended.to_csv(path_csv, index=False)
        
        else:
            df = pd.DataFrame(lavouras)
            df.to_csv(path_csv, index=False)
            
        

        

        input("\n\nPressione qualquer tecla para continuar\n")
        # print(df)




    # Visualizar dados
    elif(user == 2):
        os.system('cls')
        if os.path.exists(path_csv):
            df = pd.read_csv(path_csv)

            if not df.empty:
                print(df)

            else:
                print("Não foram cadastradas lavouras")
   
        else:
            print("Não foram cadastradas lavouras")
        
        input("\n\nPressione qualquer tecla para continuar\n")

    # Atualizar dados
    elif(user == 3):
        os.system('cls')

        if os.path.exists(path_csv):
            df = pd.read_csv(path_csv)
            print(df)
         
        id_lavoura = int(input("Digite o indice da lavoura: \t"))
        campo = input("Digite o campo a editar: \t")
        novo_valor = input("Digite o novo valor: \t")

        df.loc[id_lavoura, campo] = novo_valor

        df.to_csv(path_csv, index=False)

        input("\n\nPressione qualquer tecla para continuar\n")
            
    # Deletar dados
    elif(user == 4):
        os.system('cls')

        if os.path.exists(path_csv):
            df = pd.read_csv(path_csv)
            print(df)
            
            id_lavoura = int(input("Digite o indice da lavoura: \t"))
            df_del = df.drop(id_lavoura)

            df_del.to_csv(path_csv, index=False)
        
        input("\n\nPressione qualquer tecla para continuar\n")
    # Sair
    elif(user == 5):
        break

    else:
        print("Digite uma opção valida!")
    