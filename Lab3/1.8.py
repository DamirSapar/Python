def spy_game(nums):
    x=0
    y=0
    k=0
    d=0
    z=True

    for i in range(len(nums)):
        if nums[i]==0:
            x+=1
            k=i
        elif nums[i]==7:
            y+=1
            d=i
    if x>=2 and y>=1 and k<d:
        print(z)
    else:
        print(not(z))

spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 