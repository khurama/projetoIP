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
    existe = False
    tam=len(agenda)
    Nomes=listaNomes(chamadas)
    for e in Nomes:
      if e == nome:
        existe = True
        if existe:
          for i in range(tam):
            if agenda[i].find(nome)!=-1:
              agendasus=agenda[i][(len(nome)+13):]
              agendasus=agendasus.split(",")
              print("Agenda do suspeito %s:" %nome)
              for e in agendasus:
                print(e)
        else:
          print("Suspeito não encontrado.")
    return 

def listaNum(agenda):
    listaNum=[]
    for i in range(len(agenda)):
      if agenda[i].find("-")>=0:
        pos1 = agenda[i].find("-")
        pos2 = agenda[i].find(":")
        num=agenda[i][(pos1+1):pos2]
        listaNum.append(num)
    return listaNum

def listAgenda():
    listaNome = listaNomes(chamadas)
    listaNume = listaNum(agenda)
    for e in listaNome:
      nome = e
      saida=" "
      for i in range(len(agenda)):
        if agenda[i].find(nome)!=-1:
          agenda2=agenda[i][(len(nome)+13):]
          for ele in listaNume:
            num = ele
            if agenda2.find(num)!=-1:
              pos=listaNume.index(num)
              nome2=listaNome[pos]
              saida=saida+nome2+" "
      print("%s: %s"%(nome, saida))
    return 

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
  #area de testes

  if op == "1":
    nome=str(input("Nome do suspeito: "))
    print()
    #chamando a função imprimeAgenda
    imprimeAgenda(nome,agenda)
    print()
  elif op == "2":
    listAgenda()
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
