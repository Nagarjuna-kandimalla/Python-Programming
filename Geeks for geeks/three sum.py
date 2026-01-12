from collections import Counter

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
            result=[]
            x=[]
            n = len(nums)
            for i in range (n):
                  #print("entering 1st loop") 
                for j in range(i+1, n):
                        #print("entering 2nd loop") 
                        
                        for k in range(j+1,n):
                              #print("entering 3rd loop") 
                              
                              #tried.append([nums[i],nums[j],nums[k]])

                              if (nums[i]+nums[j]+nums[k]==0):

                                    curr_trip = [nums[i], nums[j], nums[k]]
                                    if not any(Counter(x)==Counter(curr_trip) for x in result):
                                        result.append(curr_trip)
                                    #else: 
                                        #print(f"{Counter(x)} is equal to {Counter(curr_trip)}")
            print(f"{result}")   
                                    
                                   
            return result          

nums = [-11,-3,-6,12,-15,-13,-7,-3,13,-2,-10,3,12,-12,6,-6,12,9,-2,-12,14,11,-4,11,-8,8,0,-12,4,-5,10,8,7,11,-3,7,5,-3,-11,3,11,-13,14,8,12,5,-12,10,-8,-7,5,-9,-11,-14,9,-12,1,-6,-8,-10,4,9,6,-3,-3,-12,11,9,1,8,-10,-3,2,-11,-10,-1,1,-15,-6,8,-7,6,6,-10,7,0,-7,-7,9,-8,-9,-9,-14,12,-5,-10,-15,-9,-15,-7,6,-10,5,-7,-14,3,8,2,3,9,-12,4,1,9,1,-15,-13,9,-14,11,9]
obj = Solution()
final_result = []
final_result=obj.threeSum(nums)
print(f"final result is {final_result}")