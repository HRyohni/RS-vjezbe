import re
def provjera_lozinke(lozinka):
    if 8 < len(lozinka) < 15:
        if "password" not in lozinka or "lozinka" not in lozinka:
            for slovo in lozinka:
                if not re.search(r"[A-B]", lozinka) and  not re.search(r"[a-b]", lozinka):
                    print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
                    break
            print("Lozinka je jaka!")
        else:
            print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
    else:
        print("Lozinka mora sadržavati između 8 i 15 znakova")

provjera_lozinke("1234asdASd2")




