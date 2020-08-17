import collections

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
    return res

# threeSum([-1,0,1,2,-1,-4])
threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])