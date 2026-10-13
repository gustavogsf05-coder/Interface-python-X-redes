#Gustavo S. Ferreira - Ciencias da computação 3 - Fei - semestre
#começo do projeto: 13/10/2026

def p(texto):#função para subistituir print no código
    print(f"{texto}")


def men1():
    while(True):#estrutura de repetição p/ menu
        p("calculadora de redes")
        p("1.atividade de rede")
        p("2.inatividade de rede")
        p("3.relatório geral")

        dec1 = input("selc: ").strip()
        print(f"[DEBUG] Você digitou: '{dec1}'")#estrutura de decisão p/ interno
        if dec1 == "1":
            p("atividade")
        elif dec1 == "2":
            p("inatividade")
        elif dec1 == "3":
            p("geral")
        else:
            break

men1() #chama função
