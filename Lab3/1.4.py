def filter_prime(Numbers):
    lis=list(map(int,Numbers.split()))
    z=0
    k=1
    for x in lis:
        while k<=x:
            if x%k==0:
                z+=1
                k+=1
            else:
                k+=1
                continue
        if z==2:
            print(x)
            z=0
            k=1
        else:
            z=0
            k=1
Numbers="1 2 3 4 5 6 7 8 9 10 11 12 13"
filter_prime(Numbers)