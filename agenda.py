lista_contactos = {"WILKER FLORES": 1111, "SAHED RIBEIRO": 1572,
                       "ANGELO CUNHA": 1564,
                       "ARMANDO PINHEIRO": 1510,
                       "BALANÇA": 1552,
                       "ISABEL MARTINS": 1512,
                       "BERNARDINO SANTOS": 1561,
                       "BETO KUNJUKA": 1558,
                       "CARLA PINHEIRO": 1559,
                       "CARLOS CRUZ": 1523,
                       "CARLOS VONHAFF": 1525,
                       "CLAUDIA JEREMIAS": 1565,
                       "CONTABILIDADE": 1560,
                       "CARLOS PINHEIRO": 1536,
                       "ERIKA SILVA": 1531,
                       "ERNESTO LEOPOLDO": 1508,
                       "DJAMILA REIS": 1568,
                       "FERNANDO TURECK": 1520,
                       "RAUL CRUZ": 1506,
                       "GASPAR COSTA": 1553,
                       "INFORMATICA": 1550,
                       "GRACINDA JORGE": 1541,
                       "JORGE PINHEIRO": 1511,
                       "GILSON GELEMBI": 1570,
                       "JOSE ERNESTO": 1529,
                       "SEBASTIAO HERVAS": 1505,
                       "CODESA": 1526,
                       "TRANSPORTES": 1501,
                       "MALENGUE DINZA": 1528,
                       "RECURSOS HUMANOS": 1527,
                       "MARIA WLAI": 1521,
                       "MOURA FERNANDES": 1509,
                       "NICO ARMADA": 1555,
                       "NICOLAU BAPTISTA": 1554,
                       "OFICINA": 1537,
                       "ORLANDO SANTANA": 1516,
                       "PARQUE DE TRANSPORTES": 1530,
                       "PARQUE DE EQUIPAMENTOS": 1522,
                       "EDSON JOSE": 1539,
                       "RECEPÇAO": 1571,
                       "SALA DE REUNIAO": 1557,
                       "SEGURANÇA CODESA": 1556,
                       "RUI CRUZ": 1502,
                       "TRAFEGO": 1513,
                       "TRASPORTE ESPECIAL": 1551,
                       "VICTOR LEAL": 1538,
                       "WEZA GONCALVES": 1569,
                       "LTI LOBITO": 1702,
                       "MELA COELHO": 1701,
                       "PAULA PASSOS": 1605,
                       "JULIA BARROS": 1112,
                       "AMANDIO PINHEIRO": 1103,
                       "ANA PAULA": 1200,
                       "BRUNO CANUTO": 1106,
                       "BRUNO PINHEIRO": 1102,
                       "KATIA CORREIA": 1104,
                       "MARIA DO CARMO": 1115,
                       "JORGE SILVA": 1130
                       }
def menu():
    print("")
    print("*** AGENDA DE CONTACTOS ***")
    print("")
    print("[1] Procurar Contactos")
    print("[2] Listar Todos")
    print("[3] Abandonar Sistema")
    sair = int(input(""))
    while sair == 1:
        return entrada()
    if sair == 2:
        return listagem()
    elif sair == 3:
        exit()

def entrada():
    print("Digite o nome de contacto que deseja procurar:")
    entrada_nome = input()
    entrada_nome = entrada_nome.upper()
    if entrada_nome in lista_contactos:
        print("A extensão de telefone de " + (entrada_nome) + " é: " + str(lista_contactos[entrada_nome]))
        print ("")
        return menu()
    else:
        print("Nome de contacto não encontrado!")
    return menu()

def listagem ():
    #for e in lista_contactos:
        #print(e)
    for nome, numero in lista_contactos.items():
        print(nome, numero)
menu()

def main():
    if __name__ == "__main__":
        main()