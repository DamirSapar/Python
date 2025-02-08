def quantity(heads,legs):
    for x in range(heads+1):
        if(4*x+2*(heads-x)==legs):
            print(x,"rabbits", heads-x, "chickens")
        else:
            continue
heads=35
legs=94
quantity(heads,legs)