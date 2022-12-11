funcionarios = {}
cont = 1

def cadastrar_funcionario(id):
  global cont
  print("********************************************************************************")
  print("-------------------------- MENU CADASTRAR FUNCIONÁRIO --------------------------")
  print(f'Código do Funcionario {id}')
  nome = input("Por favor entre com o NOME: ")
  setor = input("Por favor entre com o SETOR: ")
  salario = float(input("Por favor entre com o SALÁRIO (R$): "))
  funcionarios[id] = {}
  funcionarios[id]['nome'] = nome
  funcionarios[id]['setor'] = setor
  funcionarios[id]['salario'] = salario
  cont = cont + 1

def consultar_funcionarios():
  print("********************************************************************************")
  print("-------------------------- MENU CONSULTAR FUNCIONÁRIO --------------------------")
  while(True):
    print("Escolha a opção desejada:")
    print("1-Consultar todos os Funcionários")
    print("2-Consultar Funcionários por ID")
    print("3-Consultar Funcionários por SETOR")
    print("4-Retornar")
    op = int(input(">>"))
    if op == 1:
      print("------------------------------")
      for key in funcionarios:
        print(f"id : {key}")
        print(f"nome : {funcionarios[key]['nome']}")
        print(f"setor : {funcionarios[key]['setor']}")
        print(f"salario : {funcionarios[key]['salario']:.1f}")
      print("------------------------------")
    elif op == 2:
      id = int(input("Digite o ID do funcionário: "))
      print("------------------------------")
      print(f"id : {id}")
      print(f"nome : {funcionarios[id]['nome']}")
      print(f"setor : {funcionarios[id]['setor']}")
      print(f"salario : {funcionarios[id]['salario']:.1f}")
      print("------------------------------")
    elif op == 3:
      setor = input("Digite o setor do(s) funcionário(s): ")
      print("------------------------------")
      for key in funcionarios:
        if funcionarios[key]['setor'] == setor:
          print(f"nome : {funcionarios[key]['nome']}")
          print(f"setor : {funcionarios[key]['setor']}")
          print(f"salario : {funcionarios[key]['salario']:.1f}")
          print("------------------------------")
    elif op == 4:
      break

def remover_funcionario():
  print("********************************************************************************")
  cod = int(input("Digite o código do funcionário a ser removido: "))
  funcionarios.pop(cod);

print("Bem-vindo ao Controle de Funcionários do Tonny André")

while(True):
  print("********************************************************************************")
  print("-------------------------------- MENU PRINCIPAL --------------------------------")
  print("Escolha a opção desejada:")
  print("1-Cadastrar Funcionário")
  print("2-Consultar Funcionário(s)")
  print("3-Remover Funcionário")
  print("4-Sair")
  op = int(input(">>"))
  if op == 1:
    cadastrar_funcionario(cont)
  elif op == 2:
    consultar_funcionarios()
  elif op == 3:
    remover_funcionario()
  elif op == 4:
    break
  else:
    print("!! Insira um número de 1 até 4 !!")
