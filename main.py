# Copyright Alexander Gorelin 2023

print ('                                                                                                  Taschenrechner ')
print ('                                                                                                                                                                                                                          ')
print ('ERKLÄHRUNG: tippe auf eine oder mehrere ziffern auf der Tastatur, dann auf ein rechenzeichen (Plus, minus, mal, geteilt durch). Anschliesend drückst du wieder eine oder mehrere ziffern, drückst Enter und das ergebniss erscheint.')
print ('                                                                                                                                                                                                                          ')
zahl1 = int(input('geben sie die erste zahl ein.'))
zeichen = input('geben sie ein mathematisches Symbol ein.')
zahl2 = int(input ('geben sie die zweite zahl ein'))
if zeichen == '+':
    print (zahl1 + zahl2)
elif zeichen == '-':
    print (zahl1 - zahl2)
elif zeichen == '*':
    print (zahl1 * zahl2)
elif zeichen == '/':
    print (zahl1 / zahl2)
else:
    print ('diese mathematische operation ist mir noch nicht bekannt')