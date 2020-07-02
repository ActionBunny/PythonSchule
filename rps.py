# Stein Schere Papier
# 2 Spieler: einer hat QWE der andere 123(Numpad)
    # Eingabe geheim abgreifen und bestätigen ohne Enter
    # Eingaben werden nacheinander abgegriffen (geheim)
# Nach erfolgter Eingabe: Auswertung wer Gewonnen hat, Punktestand.   
    # Best of 5: Gewinner!
    # Prüfe auf Siegcondition
# wer schlägt was?

import getch as G

print("*** Willkommen zu UltimateRPS ***")
print("Kommand\t\tStein\tSchere\tPapier")
print("Spieler 1\tQ\tW\tE") # /t macht einen Tabstop in der Konsole
print("Spieler 2\t1\t2\t3")
print("*** Best of 5 gewinnt! ***")

score_pl1 = 0
score_pl2 = 0
# [Schere, Stein, Papier]
ins_pl1 = ['q','w','e']
ins_pl2 = ['1','2','3']
wins_pl1 = ['02','10','21']

def GetPlyInput(ins_pl):
    #Gibt mir den Index von oben wieder für Spieler 1 oder 2
    input_pl = ''

    # ist input valide -> nur q w e bzw 123
    while input_pl not in ins_pl :
        input_pl = str(G.getch())[2] # userinput

    input_pl = ins_pl.index(input_pl)

    return input_pl

while score_pl1<3 and score_pl2<3:
    print("Spieler 1* ",score_pl1,":",score_pl2," *Spieler 2")

    # Zug Spieler 1
    print("Spieler 1 am Stizzl")
    input_pl1 = GetPlyInput(ins_pl1)        

    # Zug Spieler 2
    print("Spieler 2 am Stizzl")
    input_pl2 = GetPlyInput(ins_pl2)

    str_inputs = '' + str(input_pl1) + str(input_pl2) # ergibt string aus 0 1 und 2
    # print(str_inputs)

    # Wer gewinnt?
    if input_pl1 == input_pl2: #Gleichstand
        # mache nichts
        print("Unentschieden")

    elif str_inputs in wins_pl1: #Win pl1
        #Gib pl1 einen Punkt
        score_pl1 += 1
    else: #win pl2   
        # gib pl2 einen punkt
        score_pl2 += 1

if score_pl1 > 2:
    print("Spieler 1 hat gewonnen!")
else:
    print("Spieler 2 hat gewonnen!")