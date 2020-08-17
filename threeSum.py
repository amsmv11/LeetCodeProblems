def threeSum(nums):
    i = 0 
    j = 1 
    k = 2 
    res = []
    while i <= len(nums)-3:
        while j <= len(nums)-2:
            while k <= len(nums)-1:
                if (nums[i] + nums[j] + nums[k]) == 0:
                    res.append([nums[i],nums[j],nums[k]])
                k += 1
            j += 1
            k = j+1
        i += 1
        j = i+1
        k = i+2
    return res

threeSum([-1,0,1,2,-1,-4])