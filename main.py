# Copyright Alexander Gorelin 2023

print ('                                                                                                  Taschenrechner ')
print ('                                                                                                                                                                                                                          ')
print ('ERKLÄHRUNG: tippe auf eine oder mehrere ziffern auf der Tastatur, dann auf ein rechenzeichen (Plus, minus, mal, geteilt durch). Anschliesend drückst du wieder eine oder mehrere ziffern, drückst Enter und das ergebniss erscheint.')
print ('                                                                                                                                                                                                                          ')
zahl1 = input('geben sie die erste zahl ein.')
a = zahl1
zeichen = input('geben sie ein mathematisches Symbol ein.')
zahl2 = input ('geben sie die zweite zahl ein')
b = zahl2
if zeichen == '+':
    print (a + b)
elif zeichen == '-':
    print (a-b)
elif zeichen == '*':
    print (a*b)
elif zeichen == '/':
    print (a/b)
else:
    print ('diese mathematische operation ist mir noch nicht bekannt')