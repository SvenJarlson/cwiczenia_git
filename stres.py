rodzaj_pracy = int(input("Jaką pracę wykonujesz? Podaj odpowiednią liczbę: \n Praca umysłowa:1 \n Praca fizyczna na wysokości:2 \n Praca fizyczna pod ziemią:3 \n Praca fizyczna inna:4 \n Praca z dziećmi:5 \n Praca z chorymi:6 \n Inne:7"))
tiki = int(input("Czy posiadasz tiki nerwowe? Wpisz 1 jeśli tak, 0 jeśli nie"))

pkt=0
def stres (rodzaj_pracy, tiki):
  if rodzaj_pracy == 1:
      pkt =+ 10
  if rodzaj_pracy == 2:
      pkt =+ 8
  if rodzaj_pracy == 3:
      pkt =+ 7
  if rodzaj_pracy == 4:
      pkt =+ 5
  if rodzaj_pracy == 5:
      pkt =+ 4
  if rodzaj_pracy == 6:
      pkt =+ 6
  if rodzaj_pracy == 7:
      pkt =+ 3
  if tiki == 1:
      pkt =+ 10
  if tiki == 0:
      pkt =+ 0
