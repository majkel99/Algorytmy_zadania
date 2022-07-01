def naive_algorithm(txt, pat):
    for i in range(len(txt)-len(pat)+1):
        j=0
        while(j<len(pat)):
            if txt[i+j]==pat[j]:
                j+=1
            else:
                break
            if j==len(pat):
                print("wzorzec znaleziono na pozycji: ", i)
text = "AAAAAAAAAAAAAAAAAB"
pattern = "AAAB"
naive_algorithm(text,pattern)