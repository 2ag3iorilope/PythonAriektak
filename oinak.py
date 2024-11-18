oinak = int(input("Sartu distantzia oinetan: "))
pulgadak = int(input("Sartu distantzia pulgadetan: "))

total_pulgadak = oinak * 12 + pulgadak


zentimetroak = total_pulgadak * 2.54


print("Distantzia  " + str(oinak) + " oinetan eta " + str(pulgadak) + " pulgadetan  ondorengoa da zentimetroetan " + str(zentimetroak))