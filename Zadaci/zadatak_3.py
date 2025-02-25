print("Dobrodošli u Lov na Blago!")
print("Nalaziš se na pustom ostrvu, a pred tobom su dva puta.")
number = int(input("Unesi bilo koji cijeli broj: "))
if int(number) % 2 == 0:
    print("Tvoj broj je paran! Ideš putem preko džungle.")
    door_1 = int(input("Ispred tebe su tri vrata: 1, 2 ili 3. Koja biraš? "))
    if door_1 % 3 == 0:
        choice = input("""Naisao si na tigra, da li ces se sakriti ili pobjeci?
        Napisi 'S'za sakriti ili 'P' za pobjeci. """).upper()
        if choice == 'S':
            print("Igra se završila! Tigar te pronasao.")
        elif choice == "P":
            print("Igra se završila! Tigar te uhvatio. Nema spasa u džungli.")

    elif door_1 % 3 != 0:
        print("Igra se završila! Broj ti nije djeljiv sa 3, upao si u zamku!")

elif int(number) % 2 != 0:
    print("Tvoj broj je neparan! Ideš putem preko neobične plaže.")
    door_2 = int(input("Ispred tebe su tri vrata: 1, 2 ili 3. Koja biraš? "))
    if door_2 % 3 == 0:
       print("Sreća te poslužila! Broj ti je djeljiv sa 3, pronašao si tajnu prečicu i spasio se!")
    elif door_2 % 3 != 0:
       print("Igra se završila! Broj ti nije djeljiv sa 3, upao si u zamku!")