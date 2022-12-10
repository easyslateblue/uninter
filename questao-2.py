total = 0.0
ans = ""
print("Bem-Vindo a Sorveteria do Sdtonny2013")
while(True):
  tam = input("Entre com o TAMANHO do pote desejada (P/M/G): ")
  cod = input("Entre com o CÓDIGO do sabor desejado (TR/ES/PR): ")
  if tam != 'P' and tam != 'M' and tam != 'G':
    print("!!!!!!!  TAMANHO ou CÓDIGO INVÁLIDO(S) !!!!!!!")
    continue
  elif cod != 'TR' and cod != 'ES' and cod != 'PR':
    print("!!!!!!!  TAMANHO ou CÓDIGO INVÁLIDO(S) !!!!!!!")
    continue

  if cod == 'TR':
    ans = "Você pediu um sorvete sabor TRADICIONAL "
    if tam == 'P':
      ans =  ans + "P de R$ 6,00"
      total = total + 6.0
    elif tam == 'M':
      ans =  ans + "M de R$ 10,00"
      total = total + 10.0
    else:
      ans =  ans + "G de R$ 18,00"
      total = total + 18.0

  elif cod == 'ES':
    ans = "Você pediu um sorvete sabor ESPECIAL "
    if tam == 'P':
      ans =  ans + "P de R$ 7,00"
      total = total + 7.0
    elif tam == 'M':
      ans =  ans + "M de R$ 12,00"
      total = total + 12.0
    else:
      ans =  ans + "G de R$ 21,00"
      total = total + 21.0

  else:
    ans = "Você pediu um sorvete sabor PREMIUM "
    if tam == 'P':
      ans =  ans + "P de R$ 8,00"
      total = total + 8.0
    elif tam == 'M':
      ans =  ans + "M de R$ 14,00"
      total = total + 14.0
    else:
      ans =  ans + "G de R$ 24,00"
      total = total + 24.0

  print(ans)
  print("------------------------------------------------------")
  op = input("Deseja pedir mais alguma coisa? (S/N): ")
  if op == 'N':
    print("O total a ser pago é: " + str("{:.2f}".format(total)))
    break
