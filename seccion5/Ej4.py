# Si esta de vacaciones o es dia de descando puede asistir, de lo contrario no puede asistir 

vacaciones = False;
diaDescanso = False;

if not(vacaciones or diaDescanso):
    print('Puede assitir al juego')
else:
    print('NO puede assitir al juego')