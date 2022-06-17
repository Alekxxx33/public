print('Witam w konwerter jednostek')
print('''Wpisz numer operacji której chcesz użyć
1.Z cali na centymetry
2.Z centymetrów na cale''')
numer=input('Numer operacji:')

if numer==1:
    a=input('Podaj długość w calach: ')
    print('Dlugość w centymetrach wynosi: ',a*2.54)
elif numer==2:
    a=input('Podaj długość w centymetrach: ')
    print('Dlugość w calach wynosi: ',a/2.54)
else:
    print('Zła cyfra')