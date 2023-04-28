igpm21 = float (input("Digite o IGPM da renovação anterior: "))
igpm22 = float (input("Digite o IGPM da renovação atual: "))

while True:

    AGREGADO1_2021 = AGREGADO1_2022 = AGREGADO2_2021 = AGREGADO2_2022 = AGREGADO3_2021 = AGREGADO3_2022 = 0

    print ("-"*70)
    plano = float (input ("Digite a quantidade do item do plano: "))
    
    if (plano>1):

        p_plan1 = plano*(igpm21/100)
        plano21 = plano + p_plan1
        p_plan2 = plano21*(igpm22/100)
        plano22 = plano21 + p_plan2
        
        print (" -> Plano 2021: R$%.2f\n-> Plano 2022: R$%.2f" % (plano21, plano22))

    agr = 1        
    while agr<=3:

        agre22 = 0
        agre21 = 0

        print ("-"*70)
        agreQTD = float(input("Digite a quantidade do item do agregado: "))
    
        if (agr == 1):

            p_agre1 = agreQTD*(igpm21/100)
            agre21 = agreQTD + p_agre1
            p_agre2 = agre21*(igpm22/100)
            agre22 = agre21 + p_agre2
            AGREGADO1_2021 = agre21
            AGREGADO1_2022 = agre22

            print (" -> Agregado 2021: R$%.2f\n-> Agregado 2022: R$%.2f" % (agre21, agre22))
        elif (agr==2):
            p_agre1 = agreQTD*(igpm21/100)
            agre21 = agreQTD + p_agre1
            p_agre2 = agre21*(igpm22/100)
            agre22 = agre21 + p_agre2
            AGREGADO2_2021 = agre21
            AGREGADO2_2022 = agre22

            print (" -> Agregado 2021: R$%.2f\n-> Agregado 2022: R$%.2f" % (agre21, agre22))
        elif (agr == 3):
            p_agre1 = agreQTD*(igpm21/100)
            agre21 = agreQTD + p_agre1
            p_agre2 = agre21*(igpm22/100)
            agre22 = agre21 + p_agre2
            AGREGADO3_2021 = agre21
            AGREGADO3_2022 = agre22

            print (" -> Agregado 2021: R$%.2f\n-> Agregado 2022: R$%.2f" % (agre21, agre22))

        if(agr<3):
            print ("-"*70)
            identificador = int(input("Gostaria de saber o valor de outro AGREGADO?\n 1 - SIM \n 2 - NÃO\nR: "))

        if (identificador == 1):
            agr+=1
        elif (identificador == 2) or (agr == 3):
            agr = 4

    totalAGRE21 = AGREGADO1_2021+AGREGADO2_2021+AGREGADO3_2021
    totalAGRE22 = AGREGADO1_2022+AGREGADO2_2022+AGREGADO3_2022

    if (agr == 4):
    
        print ("-"*70)
        print ("VALORES TOTAIS - 2021: \n  -> PLANO: R$%.2f\n  -> AGREGADOS: R$%.2f" %(plano21, totalAGRE21))

        if (AGREGADO1_2021>1) and (AGREGADO2_2021>1):
            print ("    > AGREGADO 1: R$%.2f" %(AGREGADO1_2021))
        if (AGREGADO2_2021>1):
            print ("    > AGREGADO 2: R$%.2f" %(AGREGADO2_2021))
        if (AGREGADO3_2021>1):
            print ("    > AGREGADO 3: R$%.2f" %(AGREGADO3_2021))
        
        print ("  -> TOTAL: R$%.2f\n" % (plano21+totalAGRE21 ))
        print ("VALORES TOTAIS - 2022: \n  -> PLANO: R$%.2f\n  -> AGREGADOS: R$%.2f  " %(plano22, totalAGRE22))
    
        if (AGREGADO1_2022>1) and (AGREGADO2_2022>1):
            print ("    > AGREGADO 1: R$%.2f" %(AGREGADO1_2022))
        if (AGREGADO2_2022>1):
            print ("    > AGREGADO 2: R$%.2f" %(AGREGADO2_2022))
        if (AGREGADO3_2022>1):
            print ("    > AGREGADO 3: R$%.2f" %(AGREGADO3_2022))
        
        print ("  -> TOTAL: R$%.2f" % (plano22 + totalAGRE22))
        print ("\nPrograma encerrado, volte sempre!")

    print ("-"*70)
    cc=int(input("Gostaria de verificar outro contrato? \n 1 - SIM\n 2 - NÃO\n R: "))

    if (cc == 2):
        break
