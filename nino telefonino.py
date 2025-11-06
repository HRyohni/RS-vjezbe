class ValidirajBrojTelefona:
    __POZIVNI_BROJEVI_LISTA = [
        # Fiksna mreža
        {"pozivni_broj": "01", "mjesto_operater": "Grad Zagreb i Zagrebačka županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "020", "mjesto_operater": "Dubrovačko-neretvanska županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "021", "mjesto_operater": "Splitsko-dalmatinska županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "022", "mjesto_operater": "Šibensko-kninska županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "023", "mjesto_operater": "Zadarska županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "031", "mjesto_operater": "Osječko-baranjska županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "032", "mjesto_operater": "Vukovarsko-srijemska županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "033", "mjesto_operater": "Virovitičko-podravska županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "034", "mjesto_operater": "Požeško-slavonska županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "035", "mjesto_operater": "Brodsko-posavska županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "040", "mjesto_operater": "Međimurska županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "042", "mjesto_operater": "Varaždinska županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "043", "mjesto_operater": "Bjelovarsko-bilogorska županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "044", "mjesto_operater": "Sisačko-moslavačka županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "047", "mjesto_operater": "Karlovačka županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "048", "mjesto_operater": "Koprivničko-križevačka županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "049", "mjesto_operater": "Krapinsko-zagorska županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "051", "mjesto_operater": "Primorsko-goranska županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "052", "mjesto_operater": "Istarska županija", "vrsta": "fiksna mreža"},
        {"pozivni_broj": "053", "mjesto_operater": "Ličko-senjska županija", "vrsta": "fiksna mreža"},

        # Mobilna mreža
        {"pozivni_broj": "091", "mjesto_operater": "A1 Hrvatska", "vrsta": "mobilna mreža"},
        {"pozivni_broj": "092", "mjesto_operater": "Telemach", "vrsta": "mobilna mreža"},
        {"pozivni_broj": "095", "mjesto_operater": "Telemach", "vrsta": "mobilna mreža"},
        {"pozivni_broj": "097", "mjesto_operater": "bonbon", "vrsta": "mobilna mreža"},
        {"pozivni_broj": "098", "mjesto_operater": "Hrvatski Telekom", "vrsta": "mobilna mreža"},
        {"pozivni_broj": "099", "mjesto_operater": "Hrvatski Telekom", "vrsta": "mobilna mreža"},

        # Posebne usluge
        {"pozivni_broj": "0800", "mjesto_operater": "Besplatni pozivi", "vrsta": "posebne usluge"},
        {"pozivni_broj": "060", "mjesto_operater": "Komercijalni pozivi", "vrsta": "posebne usluge"},
        {"pozivni_broj": "061", "mjesto_operater": "Glasovanje telefonom", "vrsta": "posebne usluge"},
        {"pozivni_broj": "064", "mjesto_operater": "Usluge s neprimjerenim sadržajem", "vrsta": "posebne usluge"},
        {"pozivni_broj": "065", "mjesto_operater": "Nagradne igre", "vrsta": "posebne usluge"},
        {"pozivni_broj": "069", "mjesto_operater": "Usluge namijenjene djeci", "vrsta": "posebne usluge"},
        {"pozivni_broj": "072", "mjesto_operater": "Jedinstveni pristupni broj za cijelu državu za posebne usluge",
         "vrsta": "posebne usluge"}
    ]
    validirani_brojevi =[]

    def __init__(self, broj):
        self.broj = broj

    def validiraj(self):

        self.broj = self.__makni_nepotrebno()
        self.broj = self.__ispravi_validaciju()
        if self.__check_pozivni_broj():
            if self.__check_number_length():
                return self.__sastavi_broj()
        return "greska"

            # makni ["+385","385","00385","(385)"]
    def __makni_nepotrebno(self):
        nepotrebno = ["+385","385","00385","(385)"]
        for x in nepotrebno:
            self.broj = self.broj.replace(x, '')
        return self.broj

        # ispravlja sve znakove zareze...
    def __ispravi_validaciju(self):
     for znak in self.broj:
      if not znak.isdigit():
       self.broj = self.broj.replace(znak, '')
     return self.broj

            ## provjerava dali postoji pozivni broj
    def __check_pozivni_broj (self):
     for ID,br in enumerate(self.__POZIVNI_BROJEVI_LISTA):
         if br["pozivni_broj"] in self.broj[0:4]:
             return  ID, br["pozivni_broj"]
     return False

            ##provjerava duzinu broja
    def __check_number_length(self):
        ID, pozivni_broj = self.__check_pozivni_broj()
        if 6 <= len(self.broj.replace(pozivni_broj, '')) <= 7:
            return True
        return False


            #" dodaj broj
    def __sastavi_broj(self):
        ID, poziv = self.__check_pozivni_broj()
        return {
            "pozivni_broj": self.__POZIVNI_BROJEVI_LISTA[ID]["pozivni_broj"],
            "broj_ostatak": self.__makni_nepotrebno().replace(poziv, ''),
            "vrsta": self.__POZIVNI_BROJEVI_LISTA[ID]["vrsta"],
            "mjesto": self.__check_mjesto(ID), # mobilan #poosb
            "operater": self.__check_mjesto(ID),  # fiks #posb
            "validan":True,
        }



    # provjeri mjesto ili operater
    def __check_mjesto(self, ID):
        if self.__POZIVNI_BROJEVI_LISTA[ID]["vrsta"] == "mobilna mreža" or "posebne usluge":
            return None
        else:
            return self.__POZIVNI_BROJEVI_LISTA[ID]["mjesto_operater"]

    def __check_operater(self, ID):
        if self.__POZIVNI_BROJEVI_LISTA[ID]["vrsta"] == "fiksna mreža" or "posebne usluge":
            return None
        else:
            return self.__POZIVNI_BROJEVI_LISTA[ID]["mjesto_operater"]



broj = "+3850721234567"
vald_broj = ValidirajBrojTelefona(broj)

print(vald_broj.validiraj())



