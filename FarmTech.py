import os

area_milho = []
area_cana = []
lavouras = [
    {
        'cultura': 'cafe', 
        'area': 15129.0,
        'insumo': 'Calcio',
        'qnt_insumo': 12, 
        'qnt_litros': 181.548
    },
    {
        'cultura': 'milho', 
        'area': 65840.0,
        'insumo': 'Fosfato',
        'qnt_insumo': 75, 
        'qnt_litros': (75*65840)/1000
    }
]

while True:
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
            "insumo":insumo,
            "qnt_insumo":qnt_insumo,
            "qnt_litros":qnt_litros
        })

    # Visualizar dados
    elif(user == 2):
        if not lavouras:
            print("Nao há lavouras cadastradas")
   
        else:
            os.system('cls')

            for i,lavoura in enumerate(lavouras):
                print(f"Indice -> {i} \nCultura: \t{lavoura["cultura"].capitalize()}")
                print(f"Area da lavoura: \t{lavoura["area"]}")
                print(f"Insumo:\t {lavoura["insumo"].capitalize()}")
                print(f"Quantidade do insumo (mL/metro):\t {lavoura["qnt_insumo"]}")
                print(f"Total de insumo usado em Litros:\t {lavoura["qnt_litros"]}\n\n")

    # Atualizar dados
    elif(user == 3):
        os.system('cls')
       
        for i,lavoura in enumerate(lavouras):
                print(f"Indice -> {i} \nCultura: \t{lavoura["cultura"].capitalize()}")
                print(f"Area da lavoura: \t{lavoura["area"]}")
                print(f"Insumo:\t {lavoura["insumo"].capitalize()}")
                print(f"Quantidade do insumo (mL/metro):\t {lavoura["qnt_insumo"]}")
                print(f"Total de insumo usado em Litros:\t {lavoura["qnt_litros"]}\n\n")

        id_lavoura = int(input("Digite o indice da lavoura: \t"))
        campo = input("Digite o campo a editar: \t")
        novo_valor = input("Digite o novo valor: \t")

        
        if 0 <= id_lavoura < len(lavouras):
            lavouras[id_lavoura][f"{campo}"] = novo_valor
            os.system('cls')
            print(f"Lavoura ID {id_lavoura} atualizado para {novo_valor}.")
        else:
            print("ID de lavoura inválido.")
            
    # Deletar dados
    elif(user == 4):
        os.system('cls')
        
        for i,lavoura in enumerate(lavouras):
                print(f"Indice -> {i} \nCultura: \t{lavoura["cultura"].capitalize()}")
                print(f"Area da lavoura: \t{lavoura["area"]}")
                print(f"Insumo:\t {lavoura["insumo"].capitalize()}")
                print(f"Quantidade do insumo (mL/metro):\t {lavoura["qnt_insumo"]}")
                print(f"Total de insumo usado em Litros:\t {lavoura["qnt_litros"]}\n\n")

        id_lavoura = int(input("Digite o indice da lavoura: \t"))
        if 0 <= id_lavoura < len(lavouras):
            lavoura_removida = lavouras.pop(id_lavoura)
            os.system('cls')
            print(f"Lavoura de {lavoura_removida["cultura"].capitalize()} removido com sucesso.")
        else:
            print("ID de lavoura inválido.")
    # Sair
    elif(user == 5):
        break

    else:
        print("Digite uma opção valida!")
    