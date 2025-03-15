print("indexování"[:5])
print("indexování"[-5:])
print("indexování"[::3])

kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26
kg_pocet = 80
km_pocet = 54
l_pocet = 5

kg_vysledek = kg_pocet * kg_lb
print(kg_vysledek)

km_vysledek = km_pocet * km_mile
print(km_vysledek)

l_vysledek = l_pocet * l_gal
print(l_vysledek)

print(kg_pocet, "kg", "je", kg_vysledek, "lb")

mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000
sleva_merc = 5000
cena_2_merc = int(mercedes) * 2
cena_merc_a_rolls = rolls_royce + mercedes

print("Sleva na Mercedes:", sleva_merc)
print("Cena za dva Mercedesy je:", cena_2_merc)
print("Cena za Mercedes a Rolls-Royce:", cena_merc_a_rolls)

jmeno = "Lukáš"
prijmeni = "Dvořák"
cele_jmeno = (jmeno + " " + prijmeni)
print(cele_jmeno)
delka_jmena = len(cele_jmeno)
print("Délka jména:", delka_jmena)
print("========\n",
    cele_jmeno,
    "\n========")
    
print("=" * delka_jmena)
print(cele_jmeno)
print("=" * delka_jmena)

