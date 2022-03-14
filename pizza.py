from matplotlib import cm

small = 25
medium = 30
large = 35

small_price = 4.9
medium_price = 8.9
large_price = 12.9

def GetArea(D,withoutBorder):
    R=D/2;
    S = 3.14*(R**2)
    if withoutBorder == True:
        S = S -(S - 3.14*((R-2)**2))
    return round(S,2)

def CMPerCoin(size,price,crust):
    print(round(GetArea(size,crust)/price,2))


CMPerCoin(small,small_price,False)
CMPerCoin(medium,medium_price,False)
CMPerCoin(large,large_price,False)
