
def stres(rodzaj_pracy, tiki):
  pkt=0
  if rodzaj_pracy == 1:
      pkt += 10
  elif rodzaj_pracy == 2:
      pkt += 8
  elif rodzaj_pracy == 3:
      pkt += 7
  elif rodzaj_pracy == 4:
      pkt += 5
  elif rodzaj_pracy == 5:
      pkt += 4
  elif rodzaj_pracy == 6:
      pkt += 6
  elif rodzaj_pracy == 7:
      pkt += 3
  if tiki == 1:
      pkt += 10
  if tiki == 0:
      pkt += 0
  return pkt
