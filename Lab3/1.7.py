def has_33(nums):
    z=False
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            z=True
            break
       
    if z:
        print(True)
    else:
        print(False)
    

has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])