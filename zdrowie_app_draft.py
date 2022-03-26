from cwiczenia_git.stres import *

rodzaj_pracy = int(input("Jaką pracę wykonujesz? Podaj odpowiednią liczbę: \n Praca umysłowa:1 \n Praca fizyczna na wysokości:2 \n Praca fizyczna pod ziemią:3 \n Praca fizyczna inna:4 \n Praca z dziećmi:5 \n Praca z chorymi:6 \n Inne:7 \n"))
tiki = int(input("Czy posiadasz tiki nerwowe? Wpisz 1 jeśli tak, 0 jeśli nie \n"))

s = stres(rodzaj_pracy, tiki)
print(s)
