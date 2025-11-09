# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

# Entrada
# O arquivo de entrada contém um valor inteiro.

# Saída
# Imprima a saída conforme exemplo fornecido.


entrada = int (input())

anos = entrada // 365

resto_meses = int (entrada % 365)

meses = int (resto_meses // 30)

dias = int (resto_meses % 30)


print ( anos, "ano(s)")
print ( meses, "mes(es)")
print ( dias, "dia(s)")
