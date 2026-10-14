#Gustavo S. Ferreira - Ciencias da computação 3 - Fei - semestre
#começo do projeto: 13/10/2026
import os #biblioteca importada/ limpar terminal/manipular arquivos
def p(texto):#função para subistituir print no código
    print(f"{texto}")

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def men1():
    while(True):#estrutura de repetição p/ menu
        p("calculadora de redes\n")
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

def cal_at():#calculo de atividade
  limpar()
  while(true): #automatizar o calculo do periodo/consider:ano bissexto, dia e mes 
    p("   Calculadora de atividade   \n")
    p("Digite o ano de inicio")
    an_in = input("input:")
    p("Digite o ano do ultimo periodo de atividade da rede")
    an_af = input("input:")
    
    p("tempo de atividade da rede ?")
    p("digite anos como numero e inteiro \n e meses como decimais ex: 1.11 ou 1.3 ano/mes ")
    moa = str(input("selec: ")).strip()

  
men1() #chama função
