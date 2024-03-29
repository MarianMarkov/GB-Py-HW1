"""Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета."""
s = int(input())
while len(str(s)) != 6:
    s = int(input())

LH = s % 1000
RH = s // 1000
LHS = 0
RHS = 0

for i in range(len(str(LH))):
    LHS += LH % 10
    LH = LH //10
for i in range(len(str(RH))):
    RHS += RH % 10
    RH = RH //10

if LHS == RHS:
    print(s, "-> yes")
else:
    print(s, "-> no")