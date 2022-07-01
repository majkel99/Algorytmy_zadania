def boyer_algorithm(txt, pat):
    NO_OF_CHARS = 256
    Char = [-1] * NO_OF_CHARS
    m = len(pat)
    n = len(txt)
    s = 0
    for i in range(m):
        Char[ord(pat[i])] = i;
    while (s <= n - m):
        j = m - 1
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1
        if j > 0:
            s += max(1, j - Char[ord(txt[s + j])])
        else:
            print("wzorzec znaleziono na pozycji: ", s)
            if s + m < n:
                s += m - Char[ord(txt[s + m])]
            else:
                s+=1

txt = "ABAAABCDABC"
pat = "ABC"
boyer_algorithm(txt, pat)

