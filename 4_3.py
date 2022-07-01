def rabin_karp_algorithm(text, pattern, q):
    C = 256
    m = len(pattern)
    n = len(text)
    Hpat=0
    Htxt=0
    h=1
    for i in range(m-1):
        h=(h*C)%q
    for i in range(m):
        Hpat=(C*Hpat+ord(pattern[i]))%q #hash value for pattern
        Htxt=(C*Htxt+ord(text[i]))%q #hash value for text
    for i in range(n-m+1):
        if Hpat==Htxt:
            for j in range(m):
                if text[i+j]==pattern[j]:
                    j+=1
                else:
                    break
            if j==m:
                print("wzorzec znaleziono na pozycji: " + str(i))
        if i < n-m:
            Htxt=(C*(Htxt-ord(text[i])*h)+ord(text[i+m]))%q
            if Htxt<0:
                Htxt+=q

text = "ABACDCBDACDC"
pattern = "ACDC"
q = 23
rabin_karp_algorithm(text, pattern, q)

