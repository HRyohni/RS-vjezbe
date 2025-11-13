from shop import proizvodi
from shop import narudzbe

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]


for p in proizvodi_za_dodavanje:
    proizvodi.dodaj_proizvod(p)


for prod in proizvodi.skladiste:
    prod.ispis()


narudzba_1_lista = [{"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},{"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1}]

nova_narudzba = narudzbe.napravi_narudzbu(narudzba_1_lista)

if nova_narudzba:
    nova_narudzba.ispis_narudzbe()

narudzba_2_lista = [{"naziv": "Tipkovnica", "cijena": 200, "narucena_kolicina": 500}]
narudzbe.napravi_narudzbu(narudzba_2_lista)

narudzba_3_lista = [{"naziv": "Projektor", "cijena": 800, "narucena_kolicina": 1}]
narudzbe.napravi_narudzbu(narudzba_3_lista)