#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      stickphi00
#
# Created:     13.02.2017
# Copyright:   (c) stickphi00 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import randint

class Wuerfel(object):
    def __init__(self):
        self.augen = 0

    def werfen(self):
        self.augen = randint(1,6)

    def Wuerfel(self):
        return self.augen


class Konto(object):
    def __init__(self):
        self.stand = 100

    def auszahlen(self):
        if self.stand == 0:
            print('Du hast kein Geld mehr!')
        else:
            self.stand = self.stand - 1
            print('Dein Kontostand:', self.stand)

    def einzahlen(self, betrag):
        self.stand = self.stand + betrag
        print('Dein Kontostand:', self.stand)

    def Konto(self):
        print('Dein Kontostand:', self.stand)


class Spielbrett(object):
    def __init__(self):
       pass

    def setzen(self, gz):
        Felder = [1, 2, 3, 4, 5, 6]
        if gz in Felder:
            print('Du hast auf ', gz, 'gesetzt.')
            global Spielzahl
            Spielzahl = gz
        else:
            print('Du kannst nur auf die Zahlen 1-6 setzen.')
            exit()

    def Spielzahl(self):
        return Spielzahl


class Spiel(object):
    def __init__(self):
        global wuerfelA
        wuerfelA = Wuerfel()
        global wuerfelB
        wuerfelB = Wuerfel()
        global wuerfelC
        wuerfelC = Wuerfel()
        global s
        s = Spielbrett()
        global k
        k = Konto()

    def EinsatzSetzen(self):
        k.auszahlen()

    def SpielzahlSetzen(self, Zahl):
        gz = Zahl
        s.setzen(gz)

    def wuerfelWerfen(self):
        wuerfelA.werfen()
        wuerfelB.werfen()
        wuerfelC.werfen()
        print('Wuerfel 1: ', wuerfelA.Wuerfel())
        print('Wuerfel 2: ', wuerfelB.Wuerfel())
        print('Wuerfel 3: ', wuerfelC.Wuerfel())

    def GewinnAuszahlen(self):
        if wuerfelA.Wuerfel() == s.Spielzahl():
            k.einzahlen(1)
        elif wuerfelB.Wuerfel() == s.Spielzahl():
            k.einzahlen(1)
        elif wuerfelC.Wuerfel() == s.Spielzahl():
            k.einzahlen(1)
        else:
            print('Du hast diese Runde nicht richtig getippt.')
        if wuerfelA.Wuerfel() == s.Spielzahl() or wuerfelB.Wuerfel() == s.Spielzahl() or wuerfelC.Wuerfel() == s.Spielzahl():
            k.einzahlen(1)

# Spielprogramm
Runde = Spiel()
Runde.EinsatzSetzen()
rundezahl = int(input("Zahl:"))
Runde.SpielzahlSetzen(rundezahl)
Runde.wuerfelWerfen()
Runde.GewinnAuszahlen()
