def aps_vrijednost(broj1, broj2):
    razlika = broj1 - broj2
    if razlika < 0:
        razlika = -razlika
    return razlika


x = aps_vrijednost(-100, -50)
print(x)
