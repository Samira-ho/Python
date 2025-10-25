alu=float(input('Quantos dias alugado?'))
qui=float(input('Quantos Km rodados?'))
di=60*alu
va=0.15*qui
total=di+va
print('O total é de R${:.2f}'.format(total))