ulazni_string = "3,9,13,4,42"
brojevi = [int(broj) for broj in ulazni_string.split(',')]
kvadrati = [str(broj ** 2) for broj in brojevi]
rezultat_string = ",".join(kvadrati)
print("string =", rezultat_string)