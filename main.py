print("Vítám vás v kalkulačce, zda chcete kalkulačku ukončit napište 'konec'.")
while True:
  cislo1 = float(input("Zadej první číslo:"))
  cislo2 = float(input("Zadej druhé číslo:"))
  operace = input("Zadej operaci '+, -, *, /, **':")
  s= "+"
  o= "-"
  n= "*"
  d= "/"
  m= "**"

  if operace == "+":
   print (cislo1+cislo2)
  elif operace == "-":
   print (cislo1-cislo2)
  elif operace == "*":
   print (cislo1*cislo2)
  elif (cislo1 == 0 or cislo2 == 0) and operace == "/":
    print ("Nelze dělit nulou")
  elif operace == "/":
    print (cislo1/cislo2)
  elif operace == "**":
    print (cislo1**cislo2)
  elif operace == "konec":
    print ("Děkuji za použití kalkulačky.")
    pokracovat = input("Chcete provést další výpočet? (ano/ne): ")
    if pokracovat == "ne":
      break
  else:
    print("neplatna operace")