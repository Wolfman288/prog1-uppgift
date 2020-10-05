biljett = float(input("Hur mycket kostar biljeten? "))
antal_besök = float(input("Hur många gånger kommer du besöka gymmet på ett år? "))
årskort = float(input("Hur mycket kostar ett årskort? "))

if biljett * antal_besök < årskort:
    print("Årskort är inte värt för dig!")
else:
    print("Årskort är värt för dig!")