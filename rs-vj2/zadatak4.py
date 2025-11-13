import datetime
import math


class Automobil:
    def __init__(self, marka, model , godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza


    def ispis (self):
        print(self.marka, self.model, self.godina_proizvodnje)
    def starost (self):
        print(f"auto je star", datetime.datetime.now().year - self.godina_proizvodnje )


Automobil = Automobil("renault","twingo",2003,1230123)
Automobil.ispis()
Automobil.starost()


class Kalkulator:
    def __init__ (self,a,b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b
    def oduzimanje(self):
        return self.a - self.b
    def mnozenje(self):
        return self.a * self.b
    def dijeljenje(self):
        return self.a / self.b
    def potenciranje(self):
        return self.a**self.b
    def korjen(self):
        return self.a * math.sqrt(self.b)


class Student:
    def __init__ (self,ime,prezime,godine,ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene


    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)

    def __repr__(self):
        # Ova metoda služi za ljepši ispis objekta, npr. kad printamo
        # 'najbolji_student'
        return f"Student(ime='{self.ime}', prezime='{self.prezime}', prosjek={self.prosjek():.2f})"



studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
{"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
{"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
{"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
{"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
{"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}]

studenti_objekti = [Student(**s) for s in studenti]
najbolji_student = max(studenti_objekti, key=lambda student: student.prosjek())

class Krug:
    def __init__(self, r):
        self.r = r
    def opseg(self):
        return 2 * math.pi * self.r

    def povrsina(self):
        return math.pi * (self.r ** 2)

krugic = Krug(5)
print(f"Opseg kruga je: {krugic.opseg():.2f}")
print(f"Površina kruga je: {krugic.povrsina():.2f}")


class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"{self.ime} radi na poziciji: {self.pozicija}")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print(f"{self.ime} radi na poziciji: {self.pozicija} u odjelu: {self.department}")

    def give_raise(self, radnik, povecanje):
        print(f"\nMANAGER {self.ime}: Dajem povišicu od {povecanje} EUR radniku {radnik.ime}.")
        radnik.placa += povecanje