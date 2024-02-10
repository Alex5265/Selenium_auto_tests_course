# На вход программе подается Decimal число d.
# Напишите программу, которая вычисляет значение выражения

import decimal

d = decimal.Decimal(input())

x = d.exp() + d.ln() + d.log10() + d.sqrt()

print(x)