print("Bem-vindo a Loja do Sdtonny2013")
valor = float(input("Entre com valor do produto: "))
qt = float(input("Entre com valor do quantidade: "))
if qt >= 0 and qt < 11:
  frete = 30.0
elif qt >= 11 and qt < 101:
  frete = 60.0
elif qt >= 101 and qt < 1001:
  frete = 120.0
else:
  frete = 240.0
print("O valor sem frete foi: R$ " + str("{:.2f}".format(valor * qt)))
print("O valor com frete foi: R$ " + str("{:.2f}".format((valor * qt) + frete)) + "  (frete de R$ " + str("{:.2f}".format(frete)) + ")")
