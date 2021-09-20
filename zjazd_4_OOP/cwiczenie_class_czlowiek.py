"""
klasa Czlowiek:
atrybuty instancji:
imie, nazwisko, wiek
funkcje:
podaj_imie, zmien_imie, przedstaw_sie, podaj_wiek, zmien_wiek, podaj_nazwisko, zmien_nazwisko

"""

class Czlowiek:
    def __init__(self, imie=None, nazwisko=None, wiek=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def podaj_imie(self):
        self.imie = input('Podaj imie: ')
        self.nazwisko = input('Podaj nazwisko: ')
        self.wiek = input('Podaj wiek: ')
    def zmien_imie(self):
        self.imie = input('Podaj nowe imie: ')
        self.nazwisko = input('Podaj nowe nazwisko: ')
        self.wiek = input('Podaj nowe wiek: ')
    def przedstaw_sie(self):
        print(self.imie)
        print(self.nazwisko)
        print(self.wiek)


czlowiek = Czlowiek('Ola', 'Nowak', 30)
czlowiek.podaj_imie()
czlowiek.zmien_imie()
czlowiek.przedstaw_sie()