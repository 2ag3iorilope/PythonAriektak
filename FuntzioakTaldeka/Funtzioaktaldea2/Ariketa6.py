def Alderantziztestua(testua):
    alderantziz = ""
    for karakterea in testua:
        alderantziz = karakterea + alderantziz
    return alderantziz

testua = "Kaixoo"

emaitza = Alderantziztestua(testua)
print(emaitza)