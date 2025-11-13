from . import proizvodi

sve_narudzbe = []


class Narudzba:
    """Definira narudžbu s listom naručenih proizvoda i ukupnom cijenom."""

    def __init__(self, naruceni_proizvodi, ukupna_cijena):

        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        """Ispisuje sve naručene proizvode i ukupnu cijenu."""

        dijelovi_ispisa = [f"{item['naziv']} x {item['narucena_kolicina']}" for item in self.naruceni_proizvodi]
        ispis_string = ", ".join(dijelovi_ispisa)

        print(f"Naručeni proizvodi: {ispis_string}, Ukupna cijena: {self.ukupna_cijena} eur.")


def napravi_narudzbu(naruceni_proizvodi):
    """
    Prima listu rječnika (narudžbu), provjerava argumente,
    provjerava dostupnost na skladištu i kreira Narudzba objekt.
    """

    if not isinstance(naruceni_proizvodi, list):
        print("[GREŠKA] Argument narudžbe mora biti lista.")
        return None

    if not naruceni_proizvodi:
        print("[GREŠKA] Lista narudžbe ne smije biti prazna.")
        return None

    for item in naruceni_proizvodi:
        if not isinstance(item, dict):
            print(f"[GREŠKA] Element '{item}' mora biti rječnik.")
            return None
        if not all(key in item for key in ['naziv', 'cijena', 'narucena_kolicina']):
            print(f"[GREŠKA] Rječnik {item} ne sadrži sve ključeve (naziv, cijena, narucena_kolicina).")
            return None

    for item_narudzbe in naruceni_proizvodi:
        naziv_trazim = item_narudzbe['naziv']
        kolicina_trazim = item_narudzbe['narucena_kolicina']

        proizvod_na_skladistu = None
        for p in proizvodi.skladiste:
            if p.naziv == naziv_trazim:
                proizvod_na_skladistu = p
                break

        if proizvod_na_skladistu is None:
            print(f"Proizvod {naziv_trazim} nije dostupan! (Nije na skladištu)")
            return None

        if proizvod_na_skladistu.dostupna_kolicina < kolicina_trazim:
            print(
                f"Proizvod {naziv_trazim} nije dostupan! (Traženo: {kolicina_trazim}, Dostupno: {proizvod_na_skladistu.dostupna_kolicina})")
            return None

    ukupna_cijena = sum(item['cijena'] * item['narucena_kolicina'] for item in naruceni_proizvodi)

    nova_narudzba = Narudzba(naruceni_proizvodi, ukupna_cijena)

    sve_narudzbe.append(nova_narudzba)

    print(f"\n[INFO] Narudžba uspješno kreirana! (Ukupno: {ukupna_cijena} eur)")


    return nova_narudzba