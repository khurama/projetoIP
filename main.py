
def lerArquivo(fileName="agendasuspeitos.txt"):
    file = open(fileName,"r")
    conteudo = file.readlines()
    for i in range(len(conteudo)):
        conteudo[i] = conteudo[i].replace("\n","")
    return conteudo

def listaNomes(chamadas):
  listaNomes=[]
  for i in range(len(chamadas)):
    if chamadas[i].find(":")>=0:
      pos = chamadas[i].find(":")
      nome = chamadas[i][0:pos:1]
      listaNomes.append(nome)
  return listaNomes
    
def imprimeAgenda(nome,agenda):
    tam=len(agenda)
    Nomes=listaNomes(chamadas)
    for e in Nomes:
      if e == nome:
        for i in range(tam):
          if agenda[i].find(nome)!=-1:
            agendasus=agenda[i][(len(nome)+13):]
            agendasus=agendasus.split(",")
            print("Agenda do suspeito %s:" %nome)
            for e in agendasus:
              print(e)
    return 

def pegaNum(nome,agenda):
    tam=len(agenda)
    for i in range(tam):
      if agenda[i].find(nome)>=0:
        ind=i
        pos=agenda[i].find(nome)
    if nome == "joao":
      res=agenda[ind][(len(nome)+1):(len(nome)+12)]
    elif nome == "pedro":
      res=agenda[ind][(len(nome)+1):(len(nome)+12)]
    elif nome == "antonio":
      res=agenda[ind][(len(nome)+1):(len(nome)+12)]
    return res

while True:
  #MENU
  print("Menu:")
  print("1- Ver agenda de um suspeito")
  print("2- Listar agenda apenas com suspeito incluídos")
  print("3- Visualizar reciprocidades")
  print("4- Visualizar contatos com alto nível de suspeição")
  print("5- Sair")
  op=str(input("Digite a opção desejada: "))
  print()
  #quebra do arquivo em duas listas agenda e chamadas
  conteudo=lerArquivo()
  pos=conteudo.index("chamadas")
  agenda=conteudo[0:pos]
  chamadas=conteudo[pos:]

  if op == "1":
    nome=str(input("Nome do suspeito: "))
    print()
    #chamando a função imprimeAgenda
    imprimeAgenda(nome,agenda)
    print()
  elif op == "2":
    listaNomes = listaNomes(chamadas)
    for nome in listaNomes:
      if nome == "joao":
        numPedro = pegaNum("pedro", agenda)
        numAntonio = pegaNum("antonio", agenda)
        agendaJoao = imprimeAgenda("joao",agenda)
        saida = "joao: "
        for i in range(len(agendaJoao)):
          if agendaJoao[i].find(numPedro)>=0:
            saida = saida + "pedro"
          if agendaJoao[i].find(numAntonio)>=0:
            saida = saida + ", antonio"
        print(saida)
      if nome == "pedro":
        numJoao = pegaNum("joao", agenda)
        numAntonio = pegaNum("antonio", agenda)
        agendaPedro = imprimeAgenda("pedro", agenda)
        saida = "pedro: "
        for i in range(len(agendaPedro)):
          if agendaPedro[i].find(numJoao)>=0:
            saida = saida + "joao"
          if agendaPedro[i].find(numAntonio)>=0:
            saida = saida + ", antonio"
        print(saida)
      if nome == "antonio":
        numJoao = pegaNum("joao", agenda)
        numPedro = pegaNum("pedro", agenda)
        agendaAntonio = imprimeAgenda("antonio", agenda)
        saida = "antonio: "
        for i in range(len(agendaAntonio)):
          if agendaAntonio[i].find(numJoao)>=0:
            saida = saida + "joao "
          if agendaAntonio[i].find(numPedro)>=0:
            saida = saida + " pedro"
        print(saida)
    print()
  elif op == "3":
    #chamar função reciproca
    print("3- Visualizar reciprocidades")
    print()
  elif op == "4":
    #chamar função nível de suspeição
    print("4- Visualizar contatos com alto nível de suspeição")
    print()
  elif op == "5":
    break
    print()
  else:
    print("Opção incorreta! Tente novamente.")
    print()
