def jakadieta:
    dieta=str(input('Jak się odżywiasz? Zdrowo , Normarlnie , czy Źle'))
    if dieta == 'Zdrowo':
        pkt=pkt*0.5
    elif dieta == 'Normalnie':
        pkt=pkt
    elif dieta == 'Źle':
        pkt=pkt*2
    else :
        print('Jak niby się odżywiasz? Porsze wpisać tak jak w pytaniu'
