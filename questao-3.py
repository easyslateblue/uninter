def metragem_limpeza():
  while(True):
    try:
      metragem = int(input("Entre com a metragem da casa: "))
      if metragem >= 30 and metragem < 300:
        return 60 + (0.3 * metragem)
      elif metragem >= 300 and metragem < 700:
        return 120 + (0.5 * metragem)
      else:
        print("!! Não aceitamos casas com metragem menor que 30m² ou maior que 700m² !!")
        continue
    except:
      print("!! Digite um número valido !!")

def tipo_limpeza():
  while(True):
    print("Entre com o tipo de Limpeza:")
    print("B - Básica - Indicada para sujeiras semanais ou quinzenais")
    print("C - Completa - Indicada para sujeiras antigas e/ou não rotineiras")
    tipo = input()
    mul = 0.0
    if tipo != "B" and tipo != "C":
      print("!!!!!!! Opção Inválida !!!!!!!")
      continue
    elif tipo == "B":
      print("Você selecionou a limpeza BÁSICA")
      mul = 1.0
    else:
      print("Você selecionou a limpeza COMPLETA")
      mul = 1.3
    break;
  return mul

def adicional_limpeza():
  total = 0.0
  while(True):
    print("Deseja mais algum adicional?")
    print("0- Não desejo mais nada (encerrar)")
    print("1- Passar 10 peças de roupas - R$ 10.00")
    print("2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00")
    print("3- Limpeza de 1 Geladeira/Freezer - R$ 20,00")
    try:
      adicional = int(input(">>"))
      if adicional == 1:
        total = total + 10.0
      elif adicional == 2:
        total = total + 12.0
      elif adicional == 3:
        total = total + 20.0
      elif adicional == 0:
        break
      else:
        raise Exception()
    except:
      print("!! Insira um número de 0 a 3 !!")
  return total

print("Bem-vindo ao Programa de Serviços de Limpeza do Tonny André")
print("********************************************************************************")
print("------------------------ Menu 1 de 3 - Metragem Limpeza ------------------------")
metragem = metragem_limpeza()
print("********************************************************************************")
print("------------------------ Menu 2 de 3 - Tipo de Limpeza -------------------------")
multiplicador = tipo_limpeza()
print("********************************************************************************")
print("---------------------- Menu 3 de 3 - Adicional de Limpeza ----------------------")
adicional = adicional_limpeza()
print("********************************************************************************")
print(f'TOTAL: R$ {metragem * multiplicador + adicional:.2f} + (metragem: {metragem:.2f} * tipo: {multiplicador:.2f} + adicional: {adicional:.2f})')
print("********************************************************************************")
