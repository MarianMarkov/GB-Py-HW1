"""Задача 2: Найдите сумму цифр трехзначного числа."""
a = int(input())
sum = 0
for i in range(len(str(a))):
    sum += a % 10
    a = a // 10
print(sum)
