class Proizvod:
    """Definira proizvod s nazivom, cijenom i dostupnom količinom."""

    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        """Ispisuje atribute proizvoda."""
        print(f"  > Proizvod: {self.naziv}, Cijena: {self.cijena} eur, Dostupno: {self.dostupna_kolicina} kom")
skladiste = [
    Proizvod("Stol", 150, 20),
    Proizvod("Stolica", 75, 50)
]


def dodaj_proizvod(proizvod_rjecnik):
    """
    Prima RJEČNIK, stvara objekt Proizvod i dodaje ga u listu 'skladiste'.
    """
    try:
        novi_proizvod = Proizvod(
            naziv=proizvod_rjecnik['naziv'],
            cijena=proizvod_rjecnik['cijena'],
            dostupna_kolicina=proizvod_rjecnik['dostupna_kolicina']
        )
        skladiste.append(novi_proizvod)
        print(f"[INFO] Dodan proizvod: {novi_proizvod.naziv}")
    except KeyError:
        print(f"[GREŠKA] Rječnik {proizvod_rjecnik} nema sve potrebne ključeve.")
    except Exception as e:
        print(f"[GREŠKA] Dogodila se greška: {e}")