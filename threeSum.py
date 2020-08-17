import collections
import itertools

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
    
    res.sort()
    resAUX = list(res for res,_ in itertools.groupby(res))
    i = 0
    j = 1
    to_remove = []
    while i < len(res)-1:
        while j < len(res):
            if collections.Counter(res[i]) == collections.Counter(res[j]):
                # res.remove(res[j])
                to_remove += [j]
            j += 1
        i += 1
        j = i+1
    to_remove = list(dict.fromkeys(to_remove))
    to_remove.sort()
    for e in reversed(to_remove):
        del res[e]
    return resAUX

threeSum([-1,0,1,2,-1,-4])
# threeSum([-13,5,13,12,-2,-11,-1,12,-3,0,-3,-7,-7,-5,-3,-15,-2,14,14,13,6,-11,-11,5,-15,-14,5,-5,-2,0,3,-8,-10,-7,11,-5,-10,-5,-7,-6,2,5,3,2,7,7,3,-10,-2,2,-12,-11,-1,14,10,-9,-15,-8,-7,-9,7,3,-2,5,11,-13,-15,8,-3,-7,-12,7,5,-2,-6,-3,-10,4,2,-5,14,-3,-1,-10,-3,-14,-4,-3,-7,-4,3,8,14,9,-2,10,11,-10,-4,-15,-9,-1,-1,3,4,1,8,1])