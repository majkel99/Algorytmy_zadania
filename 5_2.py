class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        # Kierunek drzewa (0/1)
        self.huff = ''

codes=dict()
#function to print the codes of symbols by traveling Huffman Tree
def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if (node.left):
        printNodes(node.left, newVal)
    if (node.right):
        printNodes(node.right, newVal)
    if (not node.left and not node.right):
        codes[node.symbol] = newVal
    return codes

#Funkcja potrzebna do uzyskania zakodowamego kodu
def Output_Encoded(data, coding):
    encoding_output = []
    for c in data:
        encoding_output.append(coding[c])
    string = ''.join([str(item) for item in encoding_output])
    return string

#Dekodowanie
def Encryption(data):
    symbols = {"A": 0.3, "B": 0.1, "C": 0.2, "D": 0.1, "E": 0.2, "F": 0.1}

    symbol_with_probs = symbols
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    print("symbole:", symbols)
    print("prawdopodobieństwa:", probabilities)

    nodes = []

    # Konwertowanie symboli i prawdopodobieństw w drzewo huffmana
    for symbol in symbols:
        nodes.append(node(symbol_with_probs.get(symbol), symbol))
    while len(nodes) > 1:
        # Sortujemy wszystkie nody
        nodes = sorted(nodes, key=lambda x: x.freq)
        # Wybieramy 2 najmniejsze nody
        right = nodes[0]
        left = nodes[1]
        # Przypisujemy wartości do tych node
        left.huff = 0
        right.huff = 1
        # łączymy 2 najmniejsze nody i tworzymy nowego noda który będzie ich rodzicem
        newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        # usuwamy te 2 nody i dodajemy ich rodzica
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    huffman_encoding = printNodes(nodes[0])
    print("kody z symbolami", huffman_encoding)
    encoded_output = Output_Encoded(data, huffman_encoding)
    return encoded_output, nodes[0]

#Odkodowanie
def Decryption(encoded_data, huffman_tree):
    tree_head = huffman_tree
    decoded_output = []
    for x in encoded_data:
        if x == '1':
            huffman_tree = huffman_tree.right
        elif x == '0':
            huffman_tree = huffman_tree.left
        try:
            if huffman_tree.left.symbol == None and huffman_tree.right.symbol == None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.symbol)
            huffman_tree = tree_head

    string = ''.join([str(item) for item in decoded_output])
    return string

data = "BACA"
encoding, tree = Encryption(data)
print("Zakodowany kod", encoding)
print("Odkodowany kod", Decryption(encoding, tree))