def shannon_fano(data):
    if len(data) > 1:
        #sortuj malejąco
        data = sorted(data, reverse=True)
        left = []
        right = data
        sum_left = 0
        sum_right = 0
        n = 0
        for x in right:
            sum_right += x[0]
        while n < len(data):
            # Przerzucanie elementów z prawej tablicy do lewej tablicy, aż różnica prawdopodobieństwa będzie najmniejsza
            if abs((sum_left+right[0][0]) - (sum_right-right[0][0])) < abs(sum_left - sum_right):
                a = right.pop(0)
                left.append(a)
                sum_left += a[0]
                sum_right -= a[0]
                n += 1
            else:
                break
        # Do kodu każdej litery z lewej dopisz 0
        for i in left:
            code[i[1]] += "0"
        # Do kodu każdej litery z prawej dopisz 1
        for j in right:
            code[j[1]] += "1"
        shannon_fano(right)
        shannon_fano(left)



code = {"A": "", "B": "", "C": "", "D": "", "E": "", }
data = [(0.3, "A"), (0.1, "B"), (0.1, "C"), (0.2, "D"), (0.3, "E")]
shannon_fano(data)
print("Kod Shannona-Fano:", code)
tekst = "BACA"
print("Tekst:", tekst)
print("Zakodowany tekst: ", end="")
for l in tekst:
    print(code[l], end="")
