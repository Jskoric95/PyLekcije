print("Pozdrav, Ovo je automatski pretvarac valuta km u milje")

while True:
    print("Molim vas unesite kilometre koje želite pretvoriti u milje. Unesite samo broj:")

    km = input("Kilometri: ")

    km = float(km.replace(",",".")) #ako korisnik unese zarez s tockom, zamijeni za zarez

    milje = km * 0.621371

    print("{0} kilometri je {1}milja.".format(km,milje))

    izbor = input("Želite li pokusati novu pretvorbu? (y/n): ")

    if izbor.lower() != "y" and izbor.lower() != "yes":
        break