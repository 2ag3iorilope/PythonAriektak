SartutakoZenbaki = int(input("Sartu zenbaki bat bere faktoriala kalkulatzeko: "))

if SartutakoZenbaki == 0:
  faktoriala = 1
else:
  faktoriala = 1
  
i = 1
while (i <= SartutakoZenbaki):
    faktoriala = faktoriala * i
    i = i + 1

print(  str(SartutakoZenbaki) + " ren faktoriala : " + str(faktoriala) + " da")