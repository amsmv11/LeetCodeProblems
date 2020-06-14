class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        flag = 0
        length = len(nums1) + len(nums2)
        #a  = (length/2) % 1
        #print("middle length = " + str(length/2))

        #se houver meio (considerar apenas o numero do meio)
        if length/2 % 1 != 0: 
          length = int(length/2 + 0.5)
        #encontrar a media dos numeros nas posicoes length/2 e length/2 +1 
        else:
          flag = 1
          length = int(length/2 + 1)
        array = []

        for c in range(length):
          if len(nums1) > 0:
            if len(nums2) > 0:
              if nums1[0] < nums2[0]:
                array += [nums1[0]]
                nums1.pop(0)
              else:
                array += [nums2[0]]
                nums2.pop(0)
            else:
              array += [nums1[0]]
              nums1.pop(0)
          else:
            array += [nums2[0]]
            nums2.pop(0)


        if flag:
          return (array[-2] + array[-1])/2 

        else:
          return array[-1]
