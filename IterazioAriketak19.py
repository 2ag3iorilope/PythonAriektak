zenbakia1 = float(input("Sartu zenbaki hamartar bat: "))

while True:
    zenbakia2 = float(input("Sartu beste zenbaki hamartar bat: "))
    if zenbakia2 <= zenbakia1:
        print("Sartutako zenbakia ez da aurrekoa baino handiagoa.")
        break
    zenbakia1 = zenbakia2
