def invest(amount, rate, time):
    print("Principal amount  :  $",amount)
    print("Annual rate : ",rate)
    for n in range (1, (time+1)):
        print(" Year ", n,"  :  ", amount*(1+rate))
        amount = amount*(1+rate)
