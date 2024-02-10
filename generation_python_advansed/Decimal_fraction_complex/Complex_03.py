# Дано натуральное число  n и два комплексных числа z1 и z2
# Напишите программу, которая вычисляет и выводит значение выражения
# z1 ** n + z2**n + сопряженное_z1**n + сопряженное_z2**(n + 1)


n, z1, z2 = int(input()), complex(input()), complex(input())

anaswer = z1**n + z2**n + z1.conjugate()**n + z2.conjugate()**(n+1)

print(anaswer)