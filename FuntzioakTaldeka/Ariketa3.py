def Alderantizjarri():
    
    zenbakia = input("Sartu zenbaki oso bat 3 digituekin : ")
    
    if len(zenbakia) == 3 and zenbakia.isdigit():
       
        Zenbakia_Alderantziz = zenbakia[::-1]
        print("Zenbakia alderantziz:", Zenbakia_Alderantziz)
    else:
        print("Sartu zenbaki oso bat 3 dijituekin.")
    
Alderantizjarri()