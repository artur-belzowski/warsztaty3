"""Stwórz program, który na podstawie

tabeli inflacji wartości
oprocentowania kredytu,
kwoty początkowej kredytu
stałej wartości raty
wyliczy wartość zadłużenia w każdym miesiącu przez 2 nadchodzące lata.

Niech program wydrukuje dla każdego miesiąca następującą linię:
Twoja pozostała kwota kredytu to X, to Y mniej niż w poprzednim miesiącu.

Napisz program tak, by wysokość początkowego kredytu, oprocentowanie kredytu (ponad inflację) i kwota raty były pobierane ze standardowego wejścia (terminal).

Przykładowe wartości kredytu i formułę do jego wyliczenia znajdziesz w załączniku powyżej. Skopiuj z niego wartości inflacji dla każdego miesiąca.

Wyślij link do swojego repozytorium (nie spakowany kod). Repozytorium powinno zawierać więcej, niż jeden commit.
"""

szablon_podsumowania = "Miesiac: {} . Twoja pozostałą kwota kredytu to {}. to {} mniej niż w poprzednim miesiącu"

opr = float(input("Podaj oprocentowanie kredytu:"))
kwota_pocz = float(input("Podaj kwotę początkową:"))
kwota_raty = float(input("Podaj kwotę raty:"))

# szablon = "Kredyt na {} PLN. Oprocentowany {}%. Kwota raty {} PLN."
# print(szablon.format(kwota_pocz, opr , kwota_raty))

info_o_kredycie = f"Kredyt na {kwota_pocz} PLN. Oprocentowany {opr}%. Kwota raty {kwota_raty} PLN."
print(info_o_kredycie)


# Styczeń
miesiąc = 'Styczeń'
poprzednia_wartosc_poz = kwota_pocz
inflacja = 1.59282448436825
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc, nowa_wartosc_pozyczki, roz_w_kredycie))

# Luty

miesiąc = 'Luty'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = -0.453509101198007
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Marzec'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 2.32467171712441
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Kwiecień'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 1.26125440724877
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Maj'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 1.78252628571251
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Czerwiec'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 2.32938454145522
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Lipiec'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 1.50222984223283
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Sierpień'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 1.78252628571251
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Wrzesień'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 2.32884899407637
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Pażdziernik'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 0.616921348207244
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Listopad'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 2.35229588637833
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Grudzień'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 0.337779545187098
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Styczeń'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 1.57703524727525
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Luty'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = -0.292781442607648
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Marzec'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 2.48619659017508
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Kwiecień'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 0.267110317834564
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Maj'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 1.41795267229799
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Czerwiec'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 1.05424326726375
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Lipiec'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 1.4805201044812
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Sierpień'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 1.57703524727525
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Wrzesień'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = -0.0774206903147018
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Pażdziernik'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 1.16573339872354
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Listopad'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = -0.404186717638335
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))

miesiąc = 'Grudzień'
poprzednia_wartosc_poz = nowa_wartosc_pozyczki
inflacja = 1.49970852083123
nowa_wartosc_pozyczki = (1 + ((inflacja + opr) / (12 * 100))) * poprzednia_wartosc_poz - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roz_w_kredycie = poprzednia_wartosc_poz - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiąc,round(nowa_wartosc_pozyczki, 2), round(roz_w_kredycie, 2)))
