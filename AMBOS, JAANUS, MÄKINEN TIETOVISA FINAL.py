print("Tervetuloa pelaamaan tietovisaa!")
while True:
    aloitusvalinta = input("Haluatko aloittaa? (kyllä/ei): ").lower()
    if aloitusvalinta != "kyllä":
        break

    kysymykset = ("Mikä maa on väkiluvultaan suurin maailmassa?: ",
                  "Kuka on tehnyt eniten maaleja jalkapallon Mestarien Liigassa?: ",
                  "Kuka oli Suomen ensimmäinen presidentti?: ",
                  "Kuka Noel Gallagher on?: ",
                  "Missä Euroopan kaupungissa Václavin aukio sijaitsee?:  ",
                  "Kuka on kirjoittanut kirjan 1984?: ",
                  "Mitä levyä on myyty eniten maailmassa?: ",
                  "Missä maassa on korkein elinajanodote?: ")

    vaihtoehdot = (("A. USA ",  "B. Intia ", "C. Kiina ", "D. Indonesia  "),
                   ("A. Lionel Messi ",  "B. Robert Lewandowski ", "C. Cristiano Ronaldo ", "D. Rául González "),
                   ("A. Lauri Kristian Relander  ",  "B. Kyösti Kallio ", "C. P. E. Svinhufvud", "D. K. J. Ståhlberg "),
                   ("A. Jalkapalloilija",  "B. Poliitikko", "C. Muusikko", "D. Kirjailija"),
                   ("A. Bratislavassa",  "B. Prahassa", "C. Budapestissa", "D. Krakovassa"),
                   ("A. George Orwell", "B. F. Scott Fitzgerald", "C. Aldous Huxley", "D. Mark Twain"),
                   ("A. AC/DC - Back in Black", "B. Pink Floyd - The Dark Side of the Moon", "C. Michael Jakcson - Thriller", "D. Fleetwood Mac - Rumours"),
                   ("A. Japani", "B. Sveitsi", "C. Italia", "D. Hong Kong"))

    oikeat_vastaukset = ("C", "C", "D", "C", "B", "A", "C", "D")
    veikkaukset = []
    pisteet = 0
    kysymysnumero = 0

    for kysymys in kysymykset:
        print("-----------------------")
        print(kysymys)
        for vaihtoehto in vaihtoehdot[kysymysnumero]:
            print(vaihtoehto)

        while True:
            vastaus = input("Anna vastaus (A, B, C, D): ").upper()
            if vastaus in ["A", "B", "C", "D"]:
                break
            else:
                print("Virheellinen vastaus. Anna vastaus A, B, C tai D.")

        veikkaukset.append(vastaus)
        if vastaus == oikeat_vastaukset[kysymysnumero]:
            pisteet += 1
            print("MAHTAVAA! OIKEIN MENI!")
        else:
            print("VALITETTAVASTI, VASTASIT VÄÄRIN.")
        kysymysnumero += 1

    print("-----------------------")
    print("--------TULOKSET-------")
    print("-----------------------")

    print("Veikkaukset: ", end="")
    for vastaus in veikkaukset:
        print(vastaus, end=" ")
    print()

    pisteet = int(pisteet / len(kysymykset) * 100)
    print(f"Sait kysymyksistä {pisteet} % oikein")

    valinta = input("Haluatko pelata uudestaan? (kyllä/ei): ").lower()
    if valinta != "kyllä":
        break
