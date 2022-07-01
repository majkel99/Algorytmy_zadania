plik = open("1_1.txt", "r")
zbior_txt = plik.read()
zbior = []
for num in zbior_txt.split(';'):
	num = num.replace(',','.')
	zbior.append(float(num))
maks = zbior[0]
for num in zbior:
	if num > maks:
		maks = num
print("Największa liczba: " + str(maks))